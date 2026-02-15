import os
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename

from extensions import db, login_manager
from models import User, Product,Cart

# ------------------
# APP CONFIG
# ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, "static", "uploads")

db.init_app(app)
login_manager.init_app(app)

# ------------------
# LOGIN MANAGER
# ------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------
# ROUTES
# ------------------
@app.route("/")
def home():
    return redirect(url_for("login"))
@app.route("/products", methods=["GET"])
@login_required
def products():
    search = request.args.get("search")
    max_price = request.args.get("price")

    query = Product.query
    if search:
        query = query.filter(Product.name.contains(search))
    if max_price:
        query = query.filter(Product.price <= max_price)

    return render_template("products.html", products=query.all())

# ------------------
# AUTH
# ------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            login_user(user)
            return redirect(url_for("products"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

# ------------------
# NEW USER LINK
# ------------------
@app.route("/new-user")
def new_user():
    # Redirect directly to register page
    return redirect(url_for("register"))

# ------------------
# ADD PRODUCT (ADMIN)
# ------------------
@app.route("/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    if not current_user.is_admin:
        return "Unauthorized", 403

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        image = request.files["image"]

        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        product = Product(
            name=name,
            price=price,
            image=filename
        )
        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products"))

    return render_template("add_products.html")
@app.route("/delete-product/<int:product_id>", methods=["POST"])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return "Unauthorized", 403

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products"))
@app.route("/add-to-cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    # Check if product already in cart
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product.id).first()

    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product.id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()
    return redirect(url_for("view_cart"))

@app.route("/remove-from-cart/<int:cart_id>", methods=["POST"])
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != current_user.id:
        return "Unauthorized", 403

    # Reduce quantity instead of deleting immediately
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    return redirect(url_for("view_cart"))
@app.route("/cart")
@login_required
def view_cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    grand_total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, grand_total=grand_total)
@app.route("/increase-quantity/<int:cart_id>", methods=["POST"])
@login_required
def increase_quantity(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != current_user.id:
        return "Unauthorized", 403

    cart_item.quantity += 1
    db.session.commit()
    return redirect(url_for("view_cart"))
@app.route("/checkout")
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    grand_total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("checkout.html", cart_items=cart_items, grand_total=grand_total)
@app.route("/place-order")
@login_required
def orderplaced():
    return render_template("orderplaced.html")
@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)

    avg_rating = db.session.query(func.avg(Review.rating))\
        .filter(Review.product_id == id).scalar()

    return render_template(
        'product_detail.html',
        product=product,
        avg_rating=round(avg_rating, 1) if avg_rating else 0
    )
@app.route('/add_review/<int:product_id>', methods=['POST'])
@login_required
def add_review(product_id):
    rating = int(request.form['rating'])
    comment = request.form['comment']

    review = Review(
        user_id=current_user.id,
        product_id=product_id,
        rating=rating,
        comment=comment
    )

    db.session.add(review)
    db.session.commit()

    flash("Review added successfully!", "success")
    return redirect(url_for('product_detail', id=product_id))
# ------------------
# MAIN
# ------------------
if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    with app.app_context():
        db.create_all()

        # create admin if not exists
        if not User.query.filter_by(username="admin").first():
            admin = User(
                username="admin",
                password="admin",
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)

logged_in = False
registered_users = ["admin", "employee1"]

def login_required(func):
    def wrapper(username):
        if not logged_in:
            print("❌ Access denied. Please login first.")
            return
        return func(username)
    return wrapper


def registration_required(func):
    def wrapper(username):
        if username not in registered_users:
            print("❌ User not registered.")
            return
        return func(username)
    return wrapper

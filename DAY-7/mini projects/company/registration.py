registered_users = ["admin", "employee1"]
def registration_required(func):
    def wrapper(username):
        if username not in registered_users:
            print("❌ User not registered.")
            return
        return func(username)
    return wrapper

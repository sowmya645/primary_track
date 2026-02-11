# main.py

from employee.view_employee import view_employee
import decorators.access as access

print("🔹 Trying without login")
view_employee("admin")

print("\n🔹 Logging in user...")
access.logged_in = True

print("\n🔹 Trying after login")
view_employee("admin") 

print("\n🔹 Trying unregistered user")
view_employee("unknown_user")

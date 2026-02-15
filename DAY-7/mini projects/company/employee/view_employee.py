# employee/view_employee.py

from decorators.access import login_required, registration_required

@registration_required
@login_required
def view_employee(username):
    print(f"✅ Employee details shown for {username}")

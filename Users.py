import re


class User:
    def __init__(self, user_name: str, email: str, password: str):
        self.user_name: str = user_name
        self.email: str = email
        self.password: str = password


class Employee(User):
    def __init__(self, user_name: str, email: str, password: str):
        super().__init__(user_name, email, password)

    @staticmethod
    def modify_name_employee_user(user, user_name: str):
        user.user_name = user_name

    @staticmethod
    def modify_email_employee_user(user, email: str):
        user.email = email

    @staticmethod
    def modify_password_employee_user(user, password: str):
        user.password = password


class Admin(User):
    def __init__(self, user_name: str, email: str, password: str):
        super().__init__(user_name, email, password)

    @staticmethod
    def create_admin_user(user_name: str, email: str, password: str):
        admin = Admin(user_name, email, password)
        if UserManagement.verify_email(admin.email) and UserManagement.verify_admin_in_list(admin.email):
            UserManagement.admin_users.append(admin)
            return True
        else:
            return False

    @staticmethod
    def create_employee_user(user_name: str, email: str, password: str):
        employee = Employee(user_name, email, password)
        if UserManagement.verify_email(employee.email) and UserManagement.verify_employee_in_list(email):
            UserManagement.employee_users.append(employee)
            return True
        else:
            return False

    # admin
    @staticmethod
    def modify_name_admin_user(user, user_name: str):
        user.user_name = user_name

    @staticmethod
    def modify_email_admin_user(user, email: str):
        user.email = email

    @staticmethod
    def modify_password_admin_user(user, password: str):
        user.password = password

    # employee
    @staticmethod
    def modify_name_employee_user(user: Employee, user_name: str):
        user.user_name = user_name

    @staticmethod
    def modify_email_employee_user(user: Employee, email: str):
        user.email = email

    @staticmethod
    def modify_password_employee_user(user: Employee, password: str):
        user.password = password


class UserManagement:
    admin_users: list[Admin] = []
    employee_users: list[Employee] = []

    @staticmethod
    def verify_email(email: str) -> bool:
        patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(patron, email):
            return True
        else:
            return False

    @staticmethod
    def verify_employee_in_list(email: str) -> bool:
        for employee in UserManagement.employee_users:
            if email == employee.email:
                return False
        return True

    @staticmethod
    def verify_admin_in_list(email: str) -> bool:
        for admin in UserManagement.admin_users:
            if email == admin.email:
                return False
        return True

    @staticmethod
    def verify_employee_credential(email: str, password: str) -> bool:
        for user in UserManagement.employee_users:
            if email == user.email and password == user.password:
                return True
        return False

    @staticmethod
    def verify_admin_credential(email: str, password: str) -> bool:
        for admin in UserManagement.admin_users:
            if email == admin.email and password == admin.password:
                return True
        return False

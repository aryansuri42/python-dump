import functools

user = {
    "username": "Aryan",
    "access_level": "admin"
}


def make_secure_function(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"{user['username']} does not have admin rights"
    return secure_function

@make_secure_function
def get_admin_password(panel):
    if panel=="admin":
        return "1234"
    elif panel=="billing":
        return "password"

    
print(get_admin_password(panel = "billing"))

student_attendance = {"rolf": 96, "bob": 90, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student} has {attendance}%")

def double(x):
    return x*2
list1 = [1,2,3,45,56]

users = [
    (0,"Bob","Password"),
    (1,"Rolf", "pw123")
]
username_mapping  = {user[1]: user for user in users}
username_input = input("Enter Username: ")
password_input = input("Input password: ")
_,username, password = username_mapping[username_input]
if password_input == password:
    print("Valid")
else:
    print("Not Valid")
    
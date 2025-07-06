username = input("กรุณากรอกชื่อของคุณ: ")
password = input("กรุณากรอกรหัสของคุณ: ")

admin_username = "admin"
admin_password = "Ad13n@23t"

if username == admin_username and password == admin_password:
    print("Welcome, admin")
else:
    print("You are not admin")

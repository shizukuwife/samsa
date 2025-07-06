#Credit_ATM = 15000
earning = int(input("กรอกรายได้ของคุณ (บาท): "))

if earning < 30000:
    print("ไม่สามารถทำบัตรได้")
elif earning <= 89999:
    print("บัตรเงิน")
elif earning <= 100000:
    print("บัตรทอง")
else:
    print("บัตร platinum")

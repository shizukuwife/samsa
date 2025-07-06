weight = int(input("กรุณากรอกนํ้าหนักของคุณ(kg) : "))
height = float(input("กรุณากรอกส่วนสูงของคุณ(m) : "))
BMI = weight/height**2
print(f"BMI is: {BMI:.1f}")
if (BMI<18.5) :
    print("Underweight")
elif (BMI<25) :
    print("Normal weight")
elif (BMI<30) :
    print("Overweight")
else :
    print("Obesity")
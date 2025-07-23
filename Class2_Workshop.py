#"WorkShop"

distance = int(input("ระยะทางคนส่ง :"))
pay = 0

if distance>4 and distance<=50 :
    pay = 10
elif distance>50 and distance<=100 :
     pay = 15
elif distance>100 and distance<=300 :
    pay = 25
elif distance>300 and distance<=500 :
    pay = 35
elif distance>500 :
    pay = 45
else :
    print("ไม่ส่งงับอ้วร")

print("ค่าส่ง =" , pay , "บาท")
#"WorkShop"

price = int(input("ระยะทางคนส่ง :"))
pay = 0

if price>4 and price<=50 :
    pay = 10
elif price>50 and price<=100 :
     pay = 15
elif price>100 and price<=300 :
    pay = 25
elif price>300 and price<=500 :
    pay = 35
elif price>500 :
    pay = 45
else :
    print("ไม่ส่งงับอ้วร")

print("ค่าส่ง =" , pay , "บาท")
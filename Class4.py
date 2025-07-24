#function

# def hello ():
#     print("Hello World")

# hello()

#_________________________________________________________________

# def add (a,b):
#     print(a+b)

# add(1,2) #ใส่ค่าไปตรงๆ

# x = 15
# y = 15
# add(x,y) #ประกาศตัวแปรแล้วเอาตัวแปรไปใส่ในฟังก์ชั่น

#_________________________________________________________________

# def introduction(name):
#     print("My name is :", name)
#     tell_age()

# def tell_age () :
#     age = input("ใส่อายุของคุณ : ")
#     print("อายุของคุณ =",age)

# introduction("Tonnam")

#_________________________________________________________________

# def spam ():
#     information = input("ใส่ข้อมูล : ")
#     value = int(input("ใส่จำนวนครั้งที่ต้องการวน : "))
#     for i in range(value):
#         print(information)

# spam()

#_________________________________________________________________

# def add (a,b) :
#     return a+b

# # print(add(1,2))

# x = 15
# y = 30
# result = add(x,y)
# print("ผลลัพธ์ :" , result)

#_________________________________________________________________

# x = ["Pangpond","Ton",2,3]

# sum = x[0] + x[1]
# print(sum)

# x[2] = 3
# sum = x[2] + x[3]
# print(sum)

# x[2] = "Ton"
# print(x[2])

# print(x[3] + x[2])

# x[4] = "Tonnam"
# print(x[4]) #ถ้าไม่มีindexตั้งแต่แรกใช้คำสั่งนี้เพิ่มข้อมูลไม่ได้ 

# x.append("best")
# print(x) #เพิ่มได้ทีละ1ตัวเท่านั้น

# x.pop(x[3])
# print(x) #ถ้าไม่ใส่indexจะลบตัวท้ายสุดออก

#_________________________________________________________________

# list = ["Pangpond","Ton",2,7]

# for i in list:
#     print(i)
#     if i == 2:
#         print("found 2!")

#_________________________________________________________________

# dict_a = {
#     "A":80,
#     "B":70,
# }
# dict_a["A"] = 99 #แก้ไขข้อมูล
# dict_a["C"] = 60 #เพิ่มข้อมูลใหม่
# print(dict_a)

#_________________________________________________________________

# students = [
#     {"name": "naming" , "id": 1},
#     {"name": "Tonnam" , "id": 2},
#     {"name": "Looktan" , "id": 3}
# ]

# for student in students:
#     print(student["name"])

#_________________________________________________________________



students = [
    {"name":"Pangpond" , "Money": 400},
    {"name":"Ton" , "Money": 1000},
    {"name":"Tonnam" , "Money": 100},
    {"name":"Naming" , "Money": 10000},
] #สร้างdicซ้อนในlist

def Check_Money (list_of_students): #สร้างฟังก์ชั่นชื่อCheck_Money(ตัวแปร)
    for student in list_of_students : #สร้างforloopตัวแปรstudentที่ดึงข้อมูลมาจากlist_of_students
        if student["Money"] > 500:
            print( student["name"] , "มีเงินมากกว่า500") 
        else:
            print(student["name"] , "มีเงินน้อยกว่า500")

Check_Money(students)





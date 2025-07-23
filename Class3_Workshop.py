#Workshop

Monster = 100
Wood_Sword = 5
Iron_Sword = 20
Diamond_Sword = 50
value = int(input("คุณต้องการตี Monster กี่รอบ : "))


while True :
    Play = int(input("คุณจะสู้ หรือ ลบเกม (สู้พิมพ์ 1/ลบเกมพิมพ์ 2) : "))

    if Play == 1 :
        print("คุณเลือกสู้")
        times = int(input("คุณต้องการจะตีกี่รอบ : "))
        for i in range(times):
            weapon = input("คุณต้องการใช้อาวุธใด (W=ดาบไม้/I=ดาบเหล็ก/D=ดาบเพรช) : ")
            
    elif Play == 2 :
        print("คุณเลือกลบเกม")
        break
    else :
        print("โปรดเลือกข้อมูลใหม่")
        
        
    #     if weapon == "W" :
    #         Monster -= 5

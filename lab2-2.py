score = int(input("รับค่าคะแนน:"))
if score >=80 and score <= 100:
    print("เกรด A")
elif score >=70 and score <= 79:
    print("เกรด B")
elif score >=60 and score <= 69:
    print("เกรด C")
elif score >=50 and score <= 59:
    print("เกรด D")
elif score >=0 and score <= 49:
    print("เกรด F")
else:
    print("กรุณากรอกข้อมูลใหม่ให้ถูกต้อง 0-100")
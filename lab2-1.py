#จงเขียนโปรแกรม รับค่าคะแนน ถ้าคะแนนมากกว่า 60 ให้แสดงค่า “ผ่าน” ถ้าคะแนนน้อยกว่า 60 ให้แสดงค่า “ไม่ผ่าน”
score = int(input("รับค่าคะแนน:"))
if score >= 60:
    print("ผ่าน")
else:
    print("ไม่ผ่าน")
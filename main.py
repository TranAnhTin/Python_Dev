name='Tin'
age=22
##print(f"Hi there, my name is {name}, age {age}")
print("Hi there, my name is {}, age {}".format(name,age))
PI=3.14
print(type(PI))
print(type(name))
import math
a=5
b=math.sqrt(a)
l=['Ford',1,2,False,"Mustang"]
l.append("Toyota")
print(l[-1])
l.insert(-9,'Mercedes')
l.insert(50,'Khanh Hoa')
print(l)
seta={"Lien Xo","My","Trung Quoc",1949,1975,1983,"My","my"}
print(seta)
s="""
Trăm năm trong cõi người ta
Chữ tài chữ mệnh khéo là ghét nhau
Trải qua một cuộc bể dâu
Những điều trông thấy mà đau đớn lòng
Lạ g bỉ sắc tự phong
Trời xanh quen thói má hồng đánh ghen
"""
##Đếm xem có bao nhieeu từ
print(len(s.split()))
##Mỗi từ xuat hien bao nhieu lan trong doan tho
count={}
Wc=s.split()
for word in Wc:
    if word in count:
        count[word]+=1
    else:
        count[word] = 1
print(count)
for i in range (1,101):
    print("%3d" %i,end=" ")
    if i%10==0:
        print()
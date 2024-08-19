# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:23:19 2024

@author: Kim Quyên

varl = 10
print("Giá trị varl = ", varl, "\n\tKiểu: ", type(varl))

var2 = float(varl)
print("Giá trị var2 = ", var2, "\n\tKiểu: ", type(var2))

var3 = 3 + 4j
print("Giá trị var3 = ", varl, "\n\tKiểu: ", type(var3))

var4 = complex(var2)
print("Giá trị var4 = ", var4, "\n\tKiểu: ", type(var4))


a = 10
b = 3

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)

x = 3
print("a ^ x = ", a ** x)

1.
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

x = (a+b+c+d)/4
print("Trung bình cộng là: ", x)


2.
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print("Tổng hai số là: ", (round(a + b, 3)))
print("Hiệu hai số là: ", (round(a - b, 3)))
print("Tích hai số là: ", (round(a * b, 3)))
print("Thương hai số là: ", (round(a / b, 3)))
print("Chia lấy dư: ", (round(a % b, 3)))
print("Chia lấy nguyên: ", (round(a // b, 3)))


3.
N = int(input("Số nguyên dương N có 2 chữ số: "))

10<=N<=99
hang_chuc = N%10
hang_donvi = N//10

tong = hang_chuc + hang_donvi

print("Tổng 2 chữ số N: ", hang_chuc,"+", hang_donvi, "=",tong)

4.
thoigian=(input("Nhập thời gian theo định dạng hh:mm:ss :"))
hh, mm, ss = map(int, thoigian.split(':'))
print("Đổi thời gian ra giây: ", hh*3600 + mm*60 + ss,"giây")


5. 
nam_sinh= int(input("Nhập năm sinh: "))

print("Bạn sinh năm: ", nam_sinh, "Tuổi của bạn là: ", 2024 - nam_sinh)

6.
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

print("PT bậc 2 có dạng: ", a,"X^2 +", b,"X +", c, "=0")

7.
print("=====MENU=====")
print("1. Hủ tiếu")
print("2. Cháo lòng")
print("3. Bánh canh")
print("4. Bún riêu")
print("5. Phở bò")
print("============")
print("Mời nhập lựa chọn: ")

-Bieu thuc A:
    import math

    p1 = pow(32, 0.2)
    p2 = pow(1/64, -0.25)
    p3 = pow(8/27, 1/3)

    A = p1 - p2 + p3

    print("Kết quả của biểu thức A là: ", (round(A, 3)))
"""

import math
a= float(input("Nhap a= "))
b= float(input("Nhap b= "))
a1= math.sqrt(a)
b1= math.sqrt(b)
a2= math.sqrt(math.sqrt(a))
b2= math.sqrt(math.sqrt(b))
ab= math.sqrt(math.sqrt(a*b))
print("Giá trị của biểu thức là: ", ((a1- b1)/(a2- b2))-((a1+ ab)/(a2+ b2)))
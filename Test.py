so= int(input("Nhập số:"))
x = 2
a = {}
while so%x == 0 and x<=so:
    a.add(x)
    x = x+1
if a == {}:
    print("Số Nguyên Tố")
else:
    print("Hợp Số")


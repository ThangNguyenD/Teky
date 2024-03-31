so= int(input("Nhập số:"))
def primenumber(p):
    x = 1
    Uoc = set()
    while so%x == 0 and x<p+1:
        Uoc.add(x)
        x = x+1
    if Uoc == {1,p}:
        print("Số Nguyên Tố")
    else:
        print("Hợp Số")
primenumber(so)       

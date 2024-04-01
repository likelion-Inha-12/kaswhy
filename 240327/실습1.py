def findingSolution(a, b, c):
    d = (b ** 2) - 4 * a * c

    if(d < 0):
        print("근이 존재하지 않습니다.")
        return
    elif (d == 0):
        x = (((-1) * b) + (d ** 0.5)) / (2*a)
        print("근 : %.2f\n중근을 갖습니다." %x)
    else:
        x1 = (((-1) * b) + (d ** 0.5)) / (2*a)
        x2 = (((-1) * b) - (d ** 0.5)) / (2*a)
        print("근: %.2f, %.2f\n" %(x1, x2))

first = findingSolution(1, 2, 1)
second = findingSolution(1, 2, 0)
third = findingSolution(1, 2, 3)
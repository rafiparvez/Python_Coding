def GCD(x,y):
    if x ==0:
        return y
    else:
        return GCD(y%x, x)

print(GCD(4,12))
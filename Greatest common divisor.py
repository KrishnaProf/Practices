
def GCD(a,b):
    assert int(a) == a and int(b) == b , 'The numbers must be integer only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

print(GCD(12,10))

#GCD(10,2) ==> GCD(2,0) ==> 2
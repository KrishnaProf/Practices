
def pairofnum(arr):
    for i in arr:
        for j in arr:
            print(str(i) + " " + str(j))

print(pairofnum([1,1]))

def printUnorderedpair(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            print(str(arr(i)) +","+ str(arr(j)))

print(printUnorderedpair([2,2]))
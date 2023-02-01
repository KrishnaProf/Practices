

def findPairs(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == target:
                print(list[i],list[j])

myList = [1,2,3,2,3,4,5,6,8]

findPairs(myList,6)
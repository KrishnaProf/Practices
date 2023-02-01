
numofDays = int(input('How many days avg you want? : '))

total = 0
temp = []
for i in range(0,numofDays):
    nextday = int(input('Day '+ str(i) + 'highest temperature : '))
    temp.append(nextday)
    total += temp[i]

avg = round(total/numofDays,2)
print('Average Temp : '+ str(avg))
print(temp)
above = 0
AboveTemp = []
for i in temp:
    if i > avg:
        above += 1
        AboveTemp.append(i)
print(str(above) + " day(s) above average ")
print(AboveTemp)


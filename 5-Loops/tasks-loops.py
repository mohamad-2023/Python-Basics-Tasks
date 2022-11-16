'''

while x>5: print(X)
for x in range(1,5)
input("inter")
int((input("insert"))
 loops in loop

 sometime need on loop

x = int (input ('Enter the Number'))
for x in range (1, x+1):
    print (x)
----------------

 # a is the number of rows and b is the numbers in row
a = int (input('Enter the number'))
for a in range (1,a+1):
    for b in range(1,a):
        print (b,end ='')

    print ('')

---------------------------



c = int(input('Enter the number'))
d = sum (list(range(1,c+1)))

print (d)
# some thing went wrong and to solve it convert the range into a list and
#print the result


------------------------------------

f=0
e = int (input ('Enter the number'))
for e in range (1,e+1):
    f+=e
print('\n')
print(f)

--------------------------------------

h = int(input('Enter the number'))
for k in range (1,11):
    l = k*h
    print (k ,'*', h ,'=',l)


---------------------------------

numbers= [12,75,150,180,145,525,50]
for m in numbers:
    if (m%5 ==0 and m<150):
        print (m)
        continue
    elif m >= 500 :
        break
    #some thiing went wrong


--------------------------------------------



#n = int (input('Enter the number')) with int did not work
n = str (input('Enter the number'))
#o=list( range(1,(len(n)+1))
p = len(n)
print (p)

----------------------------------------------



num = int(input('Enter the number'))
count = 0
while num != 0:
    num = num//10
    conut = count + 1

print ('Total digits are: ', count)




row = 5
numbers = 5

for row in range (5,0,-1):
    for i in range (numbers,0,-1):
        print (numbers, end ='')
    numbers -=1
    print ('')



    n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()






list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
ürint (new_list)




list1 = [10,20,30,40,50]
y = len(list1)
while (y-1) >= 0 :
    print (f'list1[y]')
    y -=1

#this does not work??





list1 = [10,20,30,40,50]
y = len(list1)
for x in range(0,y) :
    x = max(list1)
    c = list1[x]
    print (c)
    x -=1




list1 = [10,20,30,40,50]
y = len(list1)
for x in range(y-1,0):
    c = list1[x]
    print (c)
    x -=1






for x in range (-10,-(1+1)):
    print (x)







for i in range(5):
    print(i)
print ('Don!')








for x in range (25,51):
    for y in range (1,10):
        if (x%y)!=0 :
            print (x)
        else : continue
            





for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)




'''


a=0
b=1
for x in range (a,b+1,a+b):
    print (x,end='')






























































































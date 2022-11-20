'''
1.

x= 0
while x<=10:
    print(x)
    x+=1
    -----------------
    2.


x=0
for x<=10:
    print (x)
    x+=1

--------------------------------
3.


x= 0
while x<=10:
    print(x)
    
    if x<=5:
        break
    x+=1
    # print 5 and then stop
-----------------------------

4.


x=0
for x<=10:
    print (x)
    x+=1
    if x==5:
        continue
    # do not print 5


-------------------------------
5. Print multiplication table from 1 to 5


 #x inrange (1,6)
 #y in range (1,11)
for x in range (1,6):
    for y in range (1,11):
        i = x * y
        print (x*y,\t,'=', i)
    print (10* '*')
# there is a problem with '/t'


6. How to get numbeers from 10 to 20 using range?

i =  range (10,21)
i[4]


7. HOw to get numbers from 10 to 100 with 3 at each step using range

i = range(1,101,3)


8.Get a list of even numbers from 1 to 100 using for


even_list= []
for x in range (1,101):
    if x%2 ==0:
        even_list.append(x)

print(even_list)
# if we put ""     print(even_list)"" with attend for 'for' it gives paramids from the listes



9. Get a list of even numbers from 1 to 100 using while

even_list=[]
odd_list=[]
x = 1
while x <=100:
    if x%2 != 0:
        odd_list.append(x)
    else:
        even_list.append(x)

print(even_list)
print(odd_list)
# 'print(odd_list) did not work'


10. Get a list of even numbers from 1 to 100 using range

i thimk it is as ssme as 8 or 9


no  11 and 12 and 13 1nd 14 
'''




































    
    

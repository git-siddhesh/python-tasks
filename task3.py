'''take a list say  adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
write the program that will do
  i)  print only those numbers greater than 5
  ii)  also print those numbers those are less than or  equals to 2  ( <= 2 )
  iii)  store these answers in in two different list also
  '''

list=[]
n=int(input("Enter the no of elements:  "))
for i in range(0,n):
    element=int(input())
    list.append(element)

print("Original ",list)

y=[i for i in list if i>5 ]
print(y)

y2=[i for i in list if i<=2 ]
print(y2)


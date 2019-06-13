'''i)   print the number of repeated characters in descending order
ii)  print number of repeated words in descending order
iii)  if a word is repeating more than 5 times remove all those words
iv)  if a word is present only one times add the same word in that string but length must not increase more than 500 chars , you can remove any random thing for doing the same .
'''
import collections
string=""
leng=0
while leng<=30:
    s=input("Enter the string :  ")
    string=string+s+" "
    leng=len(string)

string2=string[:30]

d=collections.defaultdict(int)
for c in string2:
    d[c]+=1

for c in sorted(d,key=d.get,reverse=True):
    if d[c]>=1:
        print('\'%s\' %d' % (c,d[c]))

string2=string2.strip()
list=string2.split(" ")
dict1={i:list.count(i) for i in list}
for key,value in sorted(dict1,key=lambda item: item[1],reverse=True):
    print("%s: %s" % (key,value))
print(dict1)
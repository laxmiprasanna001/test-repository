str1="Hiii"
str2="Prasanna"
concatstr=str1+" "+str2
repeatstr=(str2+" ")*3
length=len(str2)
char=str2[0]
sclice=str2[1:4]
print(str1)
print(str2)
print(concatstr)
print(repeatstr)
print(len(str2))
print(char)
print(str2[1:4])
text=" Laxmi Prasanna  "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.split(','))
#print(text.replace('a','n'))
print(text.find('p'))
print(text.count('a'))
l=' '.join(['a','b'])
print(l)
print(text.startswith('H'))
print(text.endswith('H'))
t=['a','b','c','d','e','f']
r=t[-1:1:2]
print(r)
#list
list1=[1,2,3,4,5,6,7,8,9,10]
list1.reverse()
#sets
print(list1)
s1={1,2,3,4,5}
s2={3,4,5}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(type(s1))
s3={}
print(type(s3))
#dict
emp={'name':'prasanna','age':21,'dept':'SE','sal':100000,'loc':'hyd','email':'xxx'}
print(emp)
print(emp.keys())
print(emp.values())
print(emp.items())
print(emp['name'])
print(emp.get('name'))
#sort & sorted
ls1=['a','c','e','d']
ls2=ls1

print(type(ls1))
ls1.sort()#sorts and gives
print(ls1)
print(ls2)
print(ls1.sort())#it does not return any thing
ls3=sorted(ls2)
print(ls3)
strv="Hello World"

        
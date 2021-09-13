# # #calculate area and perimeter of rectangle
# # l=int(input("enter length"))
# # b=int(input("enter breadth"))
# # a=l+b
# # p=2*(l+b)
# # print("area of rectangle",a)
# # print("perimeter of rectangle",p)
# #
# # #calculate the amount ,10%discount,netamount
# # #price and quantity taken by user
# #
# # pr=int(input("enter price"))
# # q=int(input("enter quantity"))
# # amount=pr*q
# # discount=10*amount/100
# # net_amount=amount-discount
# # print("enter amount:",amount)
# # print("enter discount: ",discount)
# # print("enter netamount:",net_amount)
# #
# # #input radius of a circle ,calculate its area and circumference
# # r=int(input("enter radius"))
# # area=3.14*r*r
# # circumference=2*3.14*r
# # print("area of circle;",area)
# # print("'circumference of circlr:",circumference)
# #
# # #input principal,rate and time and calculate simple interest
# #
# # principal=int(input("enter principal"))
# # r=int(input("enter rate"))
# # time=int(input("enter time"))
# # s_i=principal*r*time/100
# # print("simple interest:",s_i)
# #
# # #swapping no
# #
# # a=int(input("enter 1st no"))
# # b=int(input("enter 2nd no"))
# # a=a+b
# # b=a-b
# # a=a-b
# # print("swapping no",a,b)
# #
# # #wap which will have a lis of value and then input a number and check if the value is present in the list or not and if present how many times.
# a=[2,4,7,9,8,8]
# num=int(input("enter the no."))
# if num in a:
#     print("no present in the list",a.count(num))
# else:
#     print("no not present in the list")
#
#
#
# #take 5 names and print in alphabetical order
# str=input("Enter 5 names")
# lst=str.split();
# lst.sort()
# print(lst)
#or
# name=[]
# for i in range(5):
#     n=str(input("enter name"))
#     name.append(n)
# print("enter name:",name)
# name.sort()
# print("enter the sorted list",name)

# #wap to input name and marks of 5 students.print name,higest marks,lowest marks
#
list1={"98:ankita","90:cj","89:gfhf","82:hghgh","70:uhj"}
print(max(list1))
print(min(list1))
#or
# name=[]
# marks=[]
# for i in range(5):
#     n=str(input("enter tne name"))
#     m=int(input("enter the marks"))
#     name.append(n)
#     marks.append(m)
# h=max(marks)
# p=min(marks)
# print("highest marks of student: ",h)
# print("lowest marks of student: ",p)
# for i in range(5):
#     if h==marks[i]:
#         print("enter name of student whose score highest marks",name[i])
#     elif p==marks[i]:
#         print("enter the student name whose score lowest marks",name[i])







#find the quadratic eq(error)
# import math
# a=float(input("enter the cofficient of a"))
# b=float(input("enter the cofficient of b"))
# c=float(input("enter the cofficient of c"))
# d=b*b-4*a*c
# if d<=0:
#     r1=(-b+math.sqrt(d))/(2*a)
#     r2=(-b-math.sqrt(d))/(2*a)
#     print("two real and unique roots",r1,r2)
# elif d==0:
#     r1=-b/(2*a)
#     print("root are real and same",r1)
# else:
#     print("root are not real")

#claculate area of triangle
# import math
# a=float(input("enter side of triangle"))
# b=float(input("enter  side of triangle"))
# c=float(input("enter  side of triangle"))
# s=(a+b+c)/2
# area=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("area of triangle",area)

#wap to input a value and insert it in the middle of an existing list
# xlist=[9,4,7,8,5]
# p=int(input("enter no"))
# xlist[3]=p
# print(xlist)
# #or
# p=[4,6,344,66,34]
# print(p)
# a=int(input("enter the number"))
# b=int(input("enter position"))
# p.insert(b,a)
# print("enter inserted list",p)
#reverse string
some=str(input("enter string"))

print(some[::-1])
#or
an=str(input("enter string"))
rev=""
for ch in an:
    rev=ch+rev
print(rev)
if an==rev:
    print("string is paliadrom ")
else:
    print("string is not palidromeff")
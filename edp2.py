#program -1: simple calculator:
x= input("input first number")
y= input("input second number")     
print("sum is:", int(x)+int(y))
print("difference is:", int(x)-int(y))
print("product is:", int(x)*int(y))
print("quotient is:", int(x)/int(y))
print("modulus is:", int(x)%int(y))

#program -2: sum and average of marks of 5 students:
a= input("input marks of student 1")
b= input("input marks of student 2")
c= input("input marks of student 3")
d= input("input marks of student 4")
e= input("input marks of student 5")
print("sum of all the marks is:", int(a)+int(b)+int(c)+int(d)+int(e))
print("average of all the marks is:", (int(a)+int(b)+int(c)+int(d)+int(e))/5)

#program -3: area of circle:
r= input("input radius of circle")
area= 3.14*int(r)*int(r)
print("area of circle is:", area)

#program -4: find area and perimeter of rectangle:
l= input("input length of rectangle")
b= input("input breadth of rectangle")
area= int(l)*int(b)
perimeter= 2*(int(l)+int(b))
print("area of rectangle is:", area)
print("perimeter of rectangle is:", perimeter)  


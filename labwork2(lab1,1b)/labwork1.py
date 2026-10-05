#ex1
print("ex1")


n= float(input("enter circle radious? "))
area = 3.14 * (n ** 2)
print("Circle area =" , n)




#ex2
print("\n ex2")


n = input("Enter the temperature? ")
print(n, "(C) = ",(float(n) * 9 / 5) + 32, "(F)")




#ex3
print("\n ex3")


n = int(input("enter a number? "))
if n > 1:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(n,"is a prime number")
    else:
        print(n,"is a NOT prime number")
else:
    print(n,"is NOT rime number")
    
    
    
    
#ex4
print("\n ex4")


n = int(input("Enter a number? "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n and n > 0:
    print(n,"is a perfect number")
else:
    print(n,"is a NOT perfect number")
    
    

#ex5
print("\n ex5")


my_list = ['Blue', 'Yellow', 'Black', 'Red', 'White']

color = input("What is your favorite color? ")

if color in my_list:
    
    print("Your colod is at index ",my_list.index(color), "in my list")
else:
    print("Sorry, I could not find your color")




#ex6
print("\n ex6")


print("Range 1: ", end="")
for i in range(0, 7, 1):
    print(i, end=" ")
    

print("\nRange 2: ", end="")
for i in range(1, 11, 3):
    print(i, end=" ")
    
print("\nRange 3: ", end="")
for i in range(5, 0, -1):
    print(i, end=" ")

print("\nRange 4: ", end="")
for i in range(6, -3, -2):
    print(i, end=" ")

print()




#ex7
print("\n ex7")


def remove_dollar_sign(s):
    s = s.replace("$","")
    return s
s = str(input("Type your strings: "))
new_s = remove_dollar_sign(s)
print(new_s)



#ex8
print("\n ex8")


list = [1, 4, 5, -1, 10]
new_list = []
for i in list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)




#ex9
print("\n ex9")


def factorial(n):
    S = 1
    for i in range(1, n + 1, 1): S = S * i
    return S
n = int(input("Enter the number: "))
print(factorial(n))




#ex10
print("\n ex10")


n = int(input("Enter a number: "))
def divisors(n):
    divisors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list
print(divisors(n))





#ex11
print("\n ex11")


import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = x2 - x1
b = y2 - y1
d = math.sqrt(a**2 + b**2)
print("the distance between two points:", d ,round(d,2))






#ex12
print("\n ex12")


m, n = map(int, input().split())
for i in range(n): print("*", end =" ")
print("")
for i in range(m - 2):
    for j in range (n):
        if j == 0 or j == n-1: print("*", end =" ")
        else: print(end =" ")
    print("")
for i in range(n): print("*", end =" ")
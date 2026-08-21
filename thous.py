# global facts 
# global rules 

# rules = True 
# facts = [["plant", "mango"], ["eating", "mango"], ["seed", "sprouts"]] 

# def assert_fact(fact): 
#     global facts 
#     global rules 
#     if not fact in facts: 
#         facts += [fact] 
#         rules = True 

# while rules: 
#     rules = False 
    
#     for A1 in facts[:]: 
       
#         if A1[0] == "seed": 
#             assert_fact(["plant", A1[1]]) 
        
       
#         if A1[0] == "plant": 
#             assert_fact(["fruit", A1[1]]) 
        
       
#         if A1[0] == "plant" and ["eating", A1[1]] in facts: 
#             assert_fact(["human", A1[1]]) 

# print(facts)



# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]


# numbers = [5, 3, 4, 1]
# selection_sort(numbers)
# print(numbers)

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j] > key:
#             arr[j + 1] = arr[j]

#             j -= 1
#         arr[j + 1] = key

# numbers = [5, 3, 4, 1]
# insertion_sort(numbers)
# print(numbers)

# def find_smallest(numbers):
#     smallest = numbers[0]

#     for num in numbers:
#         if num < smallest:
#             smallest = num

#     return smallest


# # Example
# numbers = [8, 3, 12, 1, 5]
# print("Smallest number:", find_smallest(numbers))

# numbers = [5, 3, 4, 1]
# smallest = numbers[0]
# for n in numbers:
#     if n < smallest:
#         smallest = n
# print(smallest)


numbers = [10, 20, 30, 40, 50]
target = 30

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("Found at index", i)
#         break
# else:
#     print("Not found")

stack = []

# stack.append(10)  # push
# stack.append(20)
# stack.append(30)

# print(stack)

# item = stack.pop() # pop
# print(item)
# print(stack)

# queue = []

# queue.append("asha")
# queue.append("ravi")
# queue.append("meera")

# person = queue.pop(0)  #



# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")



# 1. Get input from the user
# num1 = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # 2. Check operator and print the answer
# if op == "+":
#     print("Result:", num1 + num2)
# elif op == "-":
#     print("Result:", num1 - num2)
# elif op == "*":
#     print("Result:", num1 * num2)
# elif op == "/":
#     print("Result:", num1 / num2)
# else:
#     print("Wrong operator")


# year = int(input("enter the year:"))
# if year % 4 == 0:
#     print(year,"is leap year")
# else:
#     print(year,"not a leap year")     


# a = int(input("enter a number: "))
# b = int(input("enter another number: "))
# cal = input("enter operation: ")
# if cal == "+":
#     print("sum = ",a+b)
# if cal == "-":
#     print("min = ",a-b)
# if cal == "/":
#     print("div = ",a/b) 
# if cal == "*":
#     print("mul = ",a*b)       


# a = int(input("enter the number"))
# b = int(input("enter the number"))
# a,b = b,a
# print("after swapping: a =", a, "b =", b)                                                                                                                      




# for i in range(1,21):
    
#     if i % 2 == 0:
#         print("Even number",i)

#     else:
#         print("Odd number",i)     


# numbers = [5, 3, 4, 1]
# smallest = numbers[0]
# for n in numbers:
#     if n < smallest:
#         smallest = n
# print(smallest)

# number = int(input("Enter a number: "))
# divisor = int(input("Enter a divisor: "))

# if number % divisor == 0:
#     print("The number is divisible by the divisor")
# else:
#     print("The number is not divisible by the divisor")


# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# n.reverse()
# print(n)

# num =int(input("Enter a number: "))
# if num < 2:
#     print("Not a Prime number: ")

# else:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print("Prime number: ")
#     else:
#         print("Not a prime number: ")


# list = [10, -5, 3, -1, 7, 0, -2, 8]
# for i in list:
#     if i>0:
#         print(i)




# numbers = [1, -2, 3, -4, 5]

# positive_sum = sum(num for num in numbers if num > 0)

# print(positive_sum)






# numbers = [100, -5, 32, -100, 750, 0, -2, 81]

# count = sum(1 for num in numbers if num > 10)

# print(count)


# num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# sum = 0
# count = 0

# for i in num:
#     sum = sum + i
#     count = count + 1

# avg = sum / count
# print(avg)


# num = [1, 2, 8, 3, 7, 5, 6, 4, 11]

# for i in num:
#     if i %  2 ==0:
#         print("Even number: ",i)

#     else:
#         print("Odd number: ",i)


# list = [10, 23, 33, 40, 58, 67, 72, 81, 90, 100]
# total =0
# for i in list:
#     if i % 5 ==0:
#         total = total + 1
# print("total =",total)



# list = [10, -5, 3, -1, 7, 0, -2, 8]
# index = list.index(0)
# print(index)

# list = [100, -5, 32, -100, 750, 0, -2, 81 ]
# length = len(list)
# print(length)

# lst1 = [10, 23, 33, 40, 58, 67, 72, 81, 90, 100]
# lst2 = [100, 5, 32, 100, 750, 0, 2, 81, 87, 10 ]
# new_list = []

# for i in range(len(lst1)):
#     new_list.append(lst1[i] + lst2[i])

# print(new_list)


# lst = [10, 23, 33, 40, 58, 67, 72, 81, 90, 100]

# for i in lst:
    
#     if i % 2 == 0:
        # print(i, end = "  " )

# list = [10, 23, 33, 40, 58, 67, 72, 81, 90, 100 ]
# list[6] = 75
# print(list)           


# a = "hell, no"
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string(a))

# f = "dsfagbhdrt"
# print(len(f))

# a = int(input("enter num: "))
# b = int(input("enter 2 num: "))
# print("sum = ",a+b)

# p = [10, 45, 21, 90, 89, 35]
# p.append(44)
# p.insert(2,88)
# p.remove(21)
# print(p)

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }
# student["city"] = "Bangalore"
# student["age"] = 21
# del student["name"]
# print(student)

# a = "hell"
# b = "u"

# result = a + b

# print(result)

# list = [10, 21, 4, 5, 6, 1, 3, 18, 19, 25, 0, 77, 29, 96, 55, 17, 12, 81, 99, 100]
# even = 0
# odd = 0

# for num in list:
#     if num % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     result = num1 + num2

# elif operator == "-":
#     result = num1 - num2

# elif operator == "*":
#     result = num1 * num2

# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero"

# else:
#     result = "Invalid operator"

# print("Result:", result)

# input = [1, 0, 5, 0, 8, 3, 0]
# new_list = []

# for i in input:
#     if i == 0:
#         continue
#     new_list.append(i)

# print(new_list)

# k = [-2, 5, -7, 8, 3, 0]

# even = []
# odd = []

# for i in k:
#     if i % 2 == 0:
#         even.append(i)
#         continue

#     odd.append(i)

# print("Even:", even)
# print("Odd:"
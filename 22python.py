

name:THOUSIF
usn:KUB25EEE652
date:22/08/2026



# numbers = [3, 10, 15, 54, 75, 25, 23]
# for num in numbers:
#     if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
#         print(num)v
#     else:
#         print("None")



# arr = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
# min_index = arr.index(min(arr))
# max_index = arr.index(max(arr))
# arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
# print(arr)




# arr = [-1, 3, 34, -8, -9, 1]
# for i in range(len(arr)):
#     if arr[i] == -1:
#         arr[i] = 100
# print(arr)




# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# total_sum = sum(list1) + sum(list2)
# total_count = len(list1) + len(list2)
# average = total_sum / total_count
# print("Average:", average)



# num = int(input("Enter a number: "))
# if num % 3 == 0:
#     num = num + 5
# print("Result:", num)       


# num = [3, 10, 15, 54, 75, 25, 23]

# for i in num:
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)


# num = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# for i in num:
#     if i > 20:
#         print(i)


# num = [-1, 3, 34, -8, -9, 1]
# for i in num:
#     if i < 0:
#         print(i)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(num))

# num = int(input("Enter a number: "))
# if num % 3 == 0:
#     print(num * 5)

#take 2 num as input from user and cheak if the sum of two num is divisable by 5
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum = num1 + num2

# if sum % 5 == 0:
#     print("The sum is divisible by 5")
# else:
#     print("The sum is not divisible by 5")

# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)


#perform list operation
# numbers = [-1, 3, 34, -8, -9, 1]

# print("Original list:", numbers)

# # 1. Length
# print("Length:", len(numbers))

# # 2. Maximum
# print("Maximum:", max(numbers))

# # 3. Minimum
# print("Minimum:", min(numbers))

# # 4. Sum
# print("Sum:", sum(numbers))

# # 5. Sort ascending
# print("Ascending:", sorted(numbers))

# # 6. Sort descending
# print("Descending:", sorted(numbers, reverse=True))

# # 7. Add an element
# numbers.append(10)
# print("After append:", numbers)

# # 8. Remove an element
# numbers.remove(34)
# print("After remove:", numbers)

# # 9. Reverse the list
# numbers.reverse()
# print("After reverse:", numbers)




#[1,2,3,4,5,6,7,8,9]find the avg of list 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# avg = sum(numbers) / len(numbers)

# print("Average =", avg)




#Take the divisors from **1 to 10** and check whether the numbers **1, 5, 7, 8, 6, 9, 3 are divisible by each divisor. If a number is divisible, create a list containing those divisors.

# numbers = [1, 5, 7, 8, 6, 9, 3]

# for num in numbers:
#     divisors = []

#     for i in range(1, 11):
#         if num % i == 0:
#             divisors.append(i)

#     print(num, "->", divisors)




#**Take two numbers as input from the user. If a number is divisible by 5, square the number.**
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 % 5 == 0:
#     print("Square of", num1, "=", num1 ** 2)
# else:
#     print(num1, "is not divisible by 5")

# if num2 % 5 == 0:
#     print("Square of", num2, "=", num2 ** 2)
# else:
#     print(num2, "is not divisible by 5")





# #to find prime,even & odd num
# a = [10,3,5,6,7,8,24,3,5,6,7,89]

# even = []
# odd = []
# prime = []

# for n in a:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)

#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime.append(n)

# print("Even:", even)
# print("Odd:", odd)
# print("Prime:", prime)




#Remove the negative numbers and the numbers divisible by 3 from the list.
# numbers = [-1, 3, 34, -8, -9, 1]
# result = [x for x in numbers if x >= 0 and x % 3 != 0]
# print(result)


#For the list `[1, 2, 3, 4, 5, 6, 7, 8, 9]`, write a Python program to find the **sum, count, and average** of the numbers.

# numbers = list(range(1, 10))

# total = sum(numbers)
# count = len(numbers)
# average = total / count

# print("Sum:", total)
# print("Count:", count)
# print("Average:", average)


#Take the divisors from **1 to 10** and check whether the numbers `[1, 5, 7, 8, 6, 9, 3]` are divisible by each divisor. If a number is divisible, subtract **100** from it.
# numbers = [1, 5, 7, 8, 6, 9, 3]

# for divisor in range(1, 11):
#     for number in numbers:
#         if number % divisor == 0:
#             number -= 100
#         print(number, end=" ")
#     print()

#"university" count vowels in it python code
# word = "university"
# vowels = "aeiou"
# count = 0

# for ch in word:
#     if ch in vowels:
#         count += 1

# print("Number of vowels:", count)

#[10,3,5,6,7,8,9,24,3,5,6,7,89]  print 89 using index and add 59 to the list in 9th index
# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
# print(numbers[12])
# numbers.insert(9, 59)
# print(numbers)





##[-1,3,34,-8,-9,1] square elemnts of the list 
# numbers = [-1, 3, 34, -8, -9, 1]
# for i in numbers:
#     print(i ** 2)




##take 2 numbers as input and 2 floor division
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = a // b
# print("Floor division:", result)







##[10,3,5,6,7,8,9,24,3,5,6,7,89,7,8,54,621,57,24,3,5,6,4]find unique values
# numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89,7,8,54,621,57,24,3,5,6,4]
# unique_values = set(numbers)
# print(unique_values)
  
# import math
# # print(math.gcd(5 , 2))

# a=int(input("Enter a Num:"))

# # print(math.factorial(a ))

# print(math.sqrt(16))

'''
import math

# 1. वर्गमूल (square root)
print(math.sqrt(16))   # 👉 4.0

# 2. पावर (power)
print(math.pow(2, 3))  # 👉 8.0

# 3. फैक्टरियल
print(math.factorial(5))  # 👉 120

# 4. LCM (Least Common Multiple)
print(math.lcm(12, 18))   # 👉 36

# 5. GCD (Greatest Common Divisor)
print(math.gcd(12, 18))   # 👉 6

# 6. Pi constant
print(math.pi)            # 👉 3.141592653589793'''
#                                                     #if else 
# a=int(input("Enter a num"))
# #n = 1 - a

# if a == 0:
#     print(1)
# elif(a==1):
#     print(0)
# else:
#     print("Enter a Num 0 and 1")        

# a=int(input("Enter a num"))   #For loop                 
# if a==1 or a==0 :           # factorrial program in python usin for loop 
#     print (1)                   #pyhton me for loop "i in range use hota aur bracket me pahli value vha se suru hoti hai , second vali "
# else:                        #value par stop hota hai aur i ki value apne se badhati rahti hai. isme i++ nahi use hota  +1 use hota hai. 
#  fact=1
#  for i in range(1 , a+1):
#   fact = fact*i
#   #print(i) 
#  print(fact)

#                                #while loop
# a=int(input("Enter a num"))       #pyhton  me bhi while loop c ki tarh hota hai bas likne ka syntax badla rahta hai. 
# fact=1
# i=1
# while(i<=a):
#     fact=fact*i                   
#    # print(fact)
#     i=i+1
#     print(fact)
def fact(n):
 fact=1
 for i in range (1, n + 1):
    fact=fact*i
 print(fact)
n=int(input("Enter a Num:"))
fact(n)  


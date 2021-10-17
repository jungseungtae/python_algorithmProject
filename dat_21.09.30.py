# 조건문
# def if_test1(x):
#   if(x % 2 == 0):
#     print('x는 짝수')
#   else:
#     if(x % 2 == 1):
#       print('x는 홀수')
#     else:
#       print('x는 자연수가 아니다')
#
# if_test1(100)

# 반복문
# mysum = 0
# for i in range(1,11):
#   mysum = mysum + i**2
# else:
#   print(mysum)

# while
# x = 1
# sum = 0
# while(x <= 10):
#   sum = sum + x ** 2
#   x = x + 1
# print(sum)

# 반복문 in 조건문
# i = range(1,6)
# for j in i:
#   if(j == 3): continue
#   print(j, " ")

# i = range(1,6)
# for j in i:
#   if(j == 3): break
#   print(j, " ")

# 튜플은 수정 불가능() / 리스트 []
# def my_sums(a=0, b=10):
#   import numpy as np
#   sum1 = 0;
#   sum2 = 0
#   data = np.arange(a,b+1)
#   for i in data:
#     sum1 = sum1 + i
#     sum2 = sum2 + i**2
#   return sum1, sum2, len(data)
# print(my_sums(0, 20))
#
# a = my_sums(1,10)
# mm = a[0] / a[2]
#
# print(mm)


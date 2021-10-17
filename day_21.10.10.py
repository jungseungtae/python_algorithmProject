
# /* 제 5강 */

# # 1. class
# class Student:
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#
#   def capital_first(self):
#     return self.first.upper()
#
# aa = Student('John', 'Doe')
# bb = Student('Jane', 'Doe')
#
# print(aa.first, aa.last)
# print(bb.first, bb.last)
# print(aa.capital_first())
# print(bb.capital_first())
#
# # 2 상속
#
# class StudentGrade(Student):
#   def __init__(self, first, last, score):
#     super().__init__(first, last)
#     self.score = score
#
#   def grade(self):
#     if self.score < 80:
#       grade = 'B'
#     else:
#       grade = 'A'
#     return grade
#
# aa = StudentGrade('John', 'Doe', 75)
# bb = StudentGrade('Jane', 'Doe', 95)
#
# print(aa.score, aa.grade())
# print(bb.score, bb.grade())
# print(bb.capital_first())

# x = 10
# if(x > 5):
#   print(x)
# print('Bye')

# 3. 입출력

# import datetime
# def birthyear():
#   age = input('Enter age : ')
#   now = datetime.datetime.now()
#   curyear = now.year
#   b_year = curyear - int(age)
#   print('born.year = ', b_year)
#
# print(birthyear())

# 4. 파일 읽어오기
# (sep : 데이터의 구분자 값, header = 0 : 첫 행 컬럼명 적용, index_col : 검색 키 값 지정, usecols : 지정된 컬럼만 불러오기, encoding : 파일형식)
import pandas as pd

# df1 = pd.read_csv('C:/Users/jstco/Downloads/testdata/csv/user.csv', header = 0, sep = ' ', encoding = 'utf-8')
# print(df1.head(3))
# print(df1.tail(5))
# print(type(df1))

# df1 = pd.read_csv('C:/Users/jstco/Downloads/testdata/csv/user.csv', skiprows = 1, encoding = 'utf-8')
# print(df1)

# df1 = pd.read_csv('C:/Users/jstco/Downloads/testdata/csv/user.csv', header = 0, encoding = 'utf-8', usecols = ['userid'])
# print(df1.head(3))

# df2 = pd.read_csv('C:/Users/jstco/OneDrive/바탕 화면/user.txt', header = 0, sep = ' ', encoding = 'utf-8')
# print(df2)

# print(df2.head(3))

# df3 = pd.read_csv('C:/Users/jstco/OneDrive/바탕 화면/user.txt', header = 0, encoding = 'utf-8', usecols = ['userid'])
# print(df3)

# 5. 파일쓰기
# (pandas 모듈의 DataFrame 클래스의 to_csv 메소드 사용)

from pandas import DataFrame
# cars = {'make' : ['Hyundai', 'Kia', 'Ford', 'Chevrolet'],
#         'model' : ['Sonata', 'K5', 'Taurus', 'Impala'],
#         'price' : [3200, 3100, 3500, 3700]}
#
# df = pd.DataFrame(cars)
#
# write_text = df.to_csv('C:/Users/jstco/OneDrive/바탕 화면/새 폴더/cars.txt', sep = ' ', index = True, header = True)
#
# f = open('C:/Users/jstco/OneDrive/바탕 화면/새 폴더/cars.txt', 'w')
#
# write_csv = df.to_csv(f, sep = ',', index = None, header = True)
# f.close()

# df4 = pd.read_csv('C:/Users/jstco/OneDrive/바탕 화면/새 폴더/cars.txt', header = 0, encoding = 'utf-8', index_col = 'make')
# print(df4)
# print(df4.iloc[0, :])
# print(df4.loc['Hyundai'])

# myFile = open(r'C:\Users\jstco\OneDrive\바탕 화면\personal_info\10_박지우.txt')

# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readline())

# for i in myFile:
#   print(i)

import random
# print(random.random())

first_name_sample = '김이박최정강조윤장임'
middle_name_sample = '홍길동둘리고길동만이'
last_name_sample = '고길동둘리마이콜도우너'

alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"

# def random_name():
#   result = ''
#   result += random.choice(first_name_sample)
#   result += random.choice(middle_name_sample)
#   result += random.choice(last_name_sample)
#   return result
#
# for i in range(10):
#   print(random_name())

def random_string(length):
  result = ''
  for i in range(length):
    result += random.choice(alphabet_samples)
  return result

for i in range(5):
  print(random_string(5))
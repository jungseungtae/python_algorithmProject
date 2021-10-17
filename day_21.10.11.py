import pandas as pd
import stemgraphic as st
import matplotlib.pyplot as plt

# score = pd.read_csv('C:/Users/jstco/Downloads/파이썬 R/rpy/score.csv')
# score['total'] = score['midterm'] + score['final']
# gstat = score.groupby('gender')['total'].describe()
# print(gstat)
# print(gstat['mean'])
# print(gstat['std'])
# print(gstat['25%'])

# plt.boxplot(score.total)

# st.stem_graphic(score.total, scale = 10)
# plt.show()

# d = {'name': ['kim', 'lee', 'park'],
#      'height': [170, 160, 180],
#      'weight': [60, 55, 75]}
#
# df1 = pd.DataFrame(data = d)
#
# print(df1.iloc[0, [1, 2]])

# pay = 10000
# wt = 40
# op = pay * 1.5
#
# def myWage(hour):
#   if(hour > wt):
#     reg = hour * pay
#     otp = (hour - wt) * op
#     amount = reg + otp
#     return amount
#   else:
#     amount = hour * pay
#     return amount
#
# s_hours = input('Enter The Working Hour : ')
# f_hours = int(s_hours)
#
# toPay = myWage(f_hours)
#
# print('Pay : ', toPay)

class example:
  def __init__(self, name):
    self.name = name

  def hello(self):
    print('Hello ' + self.name + '!')
  def bye(self):
    print('Good-bye ' + self.name + '!')

greeting = example('Jung')

print(greeting.hello())
print(greeting.bye())
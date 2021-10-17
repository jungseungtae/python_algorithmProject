import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = pd.read_csv('C:/Users/jstco/Downloads/파이썬 R/rpy/score.csv')

# 1. head : 데이터의 첫 5개를 출력 또는 ()안에 원하는 갯수 입력
# print(score.head())

# 2. shape : 행, 열의 개수를 출력
# print(score.shape)

# 3. 새로운 변수생성
score['total'] = score['midterm'] +score['final']
# print(score.head(3))

# 4. mean() : 평균
# print(score['total'].mean())

# 5. std() : 표준편차
# print(score['total'].std())

# 6. median() : 중앙값
# print(score['total'].median())

# 7. quantile() : 사분위수
# print(score['total'].quantile(0.75))

# 8. 원하는 변수 지정하기
# 원하는 변수만 지정
cols = ['midterm', 'final', 'total']
# 지정된 변수 대입
score2 = score[cols]
# 지정된 변수만 출력
# print(score2.head(3))

# 9. 변수의 빈도수
import collections
# print(collections.Counter(score['gender']))

# 10. 기술통계량 출력
# print(score2.describe())

# 11. 원하는 변수를 기준으로 기술통계량 구하기
gstat = score.groupby('gender')['total'].describe()
# print(gstat)

# 12. 저장된 변수는 별도로 사용가능
# print(gstat['mean'])
# print(gstat['std'])
# print(gstat['25%'])

# 13. agg : 그룹별 통계
## 성별을 기준으로한 그룹별 통계
gstat_total = score.groupby('gender')['total']
## 데이터를 변수에 저장은 하나 호출 함수가 없으면 출력되지 않는다.
# print(gstat_total)
## 따라서 아래와 같이 원하는 값을 각각 호출해야함.
# print(gstat_total.mean(), gstat_total.size())
# print(gstat_total.size())
# print(gstat_total.std())
# print(gstat_total.min())
# print(gstat_total.max())

## 위와 같이 작업하는 것을 한번에 처리할 수 있는 함수가 agg
# agg 함수는 지정 데이터를 중심으로 여러 가지 작업을 동시에 수행할 수 있다.
# print(gstat_total.agg(['size', 'mean', 'std', 'min', 'max']))

gresult = gstat_total.agg(['size', 'mean', 'std', 'min', 'max'])

# print(gresult)
## loc를 사용하여 기준 컬럼의 데이터로 각각 호출 가능
# print(gresult.loc['f'])
# print(gresult.loc['m'])

# researchpy 모듈을 이용한 그룹별 통계량
import researchpy as rp
# print(rp.summary_cont(score['total']))
a = rp.summary_cont(score.groupby(['gender'])['total'])
# print(a)
# print(a['Mean'])
# print(a['SD'])

# 줄기잎 그림
import stemgraphic as st
# st.stem_graphic(score.total, scale = 10)
# plt.show()

# 상자그림
import seaborn as sns
sns.set(style = 'whitegrid')
# sns.boxplot(x = 'total', data = score)
# sns.boxplot(y = 'total', data = score)
# scorebox = sns.boxplot(x = 'gender', y = 'total', data = score)
# plt.show()

# 히스토그램
# plt.hist(score.total)
ftotal = score.loc[score.gender == 'f', 'total']
mtotal = score.loc[score.gender == 'm', 'total']
args = dict(alpha = 0.5, bins = 10)
plt.hist(ftotal, **args, color = 'b', label = 'female')
plt.hist(mtotal, **args, color = 'r', label = 'male')
plt.gca().set(title = 'Frequency Histogram of Score.total', ylabel = 'Frequency')
plt.legend()

plt.show()
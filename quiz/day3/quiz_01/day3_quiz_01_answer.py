#다음 퀴즈를 수행하시오.
#Q1. pandas 모듈을 pd로 불러오시오.
import pandas as pd

#Q2. "bike_rental.csv"와 "bike_weather.csv"를 pandas 모듈을 활용하여 불러오고 객체 종류를 확인하시오.
#(불러온 파일을 각각 rental, weather 객체에 저장하시오.)
rental = pd.read_csv("bike_rental.csv")
weather = pd.read_csv("bike_weather.csv")

#Q3. rental과 weather 객체의 첫 5개 row를 출력하시오.
rental.head()
weather.head()

#Q4. rental과 weather 객체의 마지막 2개 row를 출력하시오.
rental.tail()
weather.tail()

#Q5. rental과 weather 객체의 차원을 확인하시오.
rental.ndim
weather.ndim

#Q6. rental과 weather 객체의 row와 column개수를 확인하시오.
rental.shape
weather.shape

#Q7. rental과 weather 객체의 column 이름을 확인하시오
rental.columns
weather.columns


#Q8. weather 객체에 rental 객체를 column 기준으로 concat() 함수를 
# 활용하여 병합하시오.
#(데이터를 병합하여 df 객체에 저장하시오.)
# 1)
df = pd.concat([weather, rental], axis = 1)
df.head()

# 2)
df = pd.concat([weather, rental.iloc[:, 1:]], axis = 1)
df.head()


#Q9. df 객체의 결측치 개수는 총 몇 개인가?
# 1)
na_sum = 0
for n in range(df.shape[1]):
    na_sum = na_sum + df.iloc[:, n].isna().sum()
print(na_sum)

# 2)
def na_counter(x):
    return x.isna().sum()
df.apply(na_counter, 0)
sum(df.apply(na_counter, 0))

# 3) 
df.apply(lambda x: x.isna().sum())
sum(df.apply(lambda x: x.isna().sum()))

# 4)
sum(df.isna().sum())

#Q10. casual 변수와 registered 변수의 합이 
#     count변수의 합과 같다는 것을 증명하시오.
# 1)
sum(df["casual"] + df["registered"] == df["count"]) == len(df)

# 2)
sum(df["casual"] + df["registered"] - df["count"]) == 0

#Q11. 정기권 이용자의 자전거 대여[registered] 총합이 
#     가장 많은 계절[season]은 언제인가?
#     (1: 봄, 2: 여름, 3: 가을, 4: 겨울)
cnt = df[["season", "registered"]].groupby("season").sum()
cnt[cnt.iloc[:, 0] == max(cnt.iloc[:, 0])].index[0]
# 가을.

#Q12. 날씨[weather] 번호의 비중이 
#   두 번째로 높은 것의 비중을 
#   소수점 넷 째 자리까지 반올림하여 기술하시오.
df["weather"].value_counts()
df["weather"].value_counts(normalize = True)
df["weather"].value_counts(normalize = True)[2]
round(df["weather"].value_counts(normalize = True)[2], 4)

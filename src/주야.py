import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 파일 경로 자동 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', '도로교통공단_사망 교통사고 정보_20231231.csv')

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv(file_path, encoding='euc-kr')  
df.columns = df.columns.str.strip()

# 데이터 집계
weekday_counts = df['주야'].value_counts().reindex(['주', '야'])
weekday_counts.index = [label.replace(' ', '\n', 1) for label in weekday_counts.index]

# 시각화
plt.figure(figsize=(10, 6))
bars = plt.bar(weekday_counts.index, weekday_counts.values, color='skyblue')
plt.title('주야별 사망 교통사고 건수')
plt.show()

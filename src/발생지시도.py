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

# 데이터 불러오기
df = pd.read_csv(file_path, encoding='euc-kr')  
df.columns = df.columns.str.strip()

# 데이터 집계 (전국 시도 순서 고정)
target_cities = ['서울','경기', '경남', '경북', '세종', '충남', '충북', '전북', '전남','대구', '인천', '광주', '부산', '제주','울산', '대전','강원' ]
weekday_counts = df['발생지시도'].value_counts().reindex(target_cities)

# 시각화
plt.figure(figsize=(15, 7))
plt.bar(weekday_counts.index, weekday_counts.values, color='orange')
plt.title('지역별 사망 교통사고 현황')
plt.show()

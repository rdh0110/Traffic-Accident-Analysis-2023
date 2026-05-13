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

# 요일 순서 고정 (월~일)
weekday_counts = df['요일'].value_counts().reindex(['월', '화','수','목','금','토','일'])

# 시각화
plt.figure(figsize=(10, 6))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o', linestyle='-', color='red')
plt.title('요일별 사망 교통사고 추이')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 1. 파일 경로 자동 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', '도로교통공단_사망 교통사고 정보_20231231.csv')

# 2. 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf" 
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=font_prop.get_name())

# 3. 데이터 불러오기
df = pd.read_csv(file_path, encoding='euc-kr')  
df.columns = df.columns.str.strip()

# 4. 주야 및 요일별 복합 집계
day_counts = df[df['주야'] == '주']['요일'].value_counts().reindex(['월', '화', '수', '목', '금', '토', '일'])
night_counts = df[df['주야'] == '야']['요일'].value_counts().reindex(['월', '화', '수', '목', '금', '토', '일'])

combined_data = pd.DataFrame({'주간': day_counts, '야간': night_counts})

# 5. 시각화
ax = combined_data.plot(kind='bar', figsize=(12, 7), color=['#ffcc00', '#333366'], edgecolor='black')
plt.title('요일 및 주야별 사망 교통사고 현황', fontsize=16, pad=20)
plt.xlabel('요일', fontsize=12)
plt.ylabel('사고 건수', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='시간대')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

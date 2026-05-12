import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import tkinter as tk
from tkinter import filedialog
     

# 1. 파일 선택 창 띄우기 (사용자 편의성)
root = tk.Tk()
root.withdraw()
print("분석할 CSV 파일을 선택해주세요...")

file_path = filedialog.askopenfilename(
    title="교통사고 데이터(CSV) 선택",
    filetypes=[("CSV files", "*.csv")]
)
 
# 한글 폰트 설정 (Malgun Gothic 사용)
font_path = "C:/Windows/Fonts/malgun.ttf" 
font_prop = fm.FontProperties(fname=font_path, size=12)

# CSV 파일에서 데이터 불러오기(인코딩을 euc-kr로 변경)
df = pd.read_csv(file_path, encoding='euc-kr')  

# 열 이름 확인 및 공백 제거
df.columns = df.columns.str.strip()

# 요일별 사고 수 계산
weekday_counts = df['요일'].value_counts().reindex(['월', '화', '수', '목', '금', '토', '일'])

# 주야별 사고 수 계산
day_night_counts = df['주야'].value_counts().reindex(['주', '야'])

# 주야를 주어진 요일에 맞춰 반복적으로 재구성
day_counts = df[df['주야'] == '주']['요일'].value_counts().reindex(['월', '화', '수', '목', '금', '토', '일'])
night_counts = df[df['주야'] == '야']['요일'].value_counts().reindex(['월', '화', '수', '목', '금', '토', '일'])

# 두 데이터를 하나의 DataFrame으로 합치기
combined_data = pd.DataFrame({'주간': day_counts, '야간': night_counts})

# 막대그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 조정
bars = combined_data.plot(kind='bar', ax=plt.gca(), color=['skyblue', 'lightgreen'], legend=True)

# 그래프 제목 및 축 레이블 설정
plt.title('요일에 따른 주간 및 야간 교통사고 발생 수', fontproperties=font_prop)
plt.xlabel('요일', fontproperties=font_prop)
plt.ylabel('사고 수', fontproperties=font_prop)

# 각 막대 위에 수치 표시
for bar in bars.patches:
    yval = bar.get_height()  # 막대의 높이(값)
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), 
             ha='center', va='bottom', fontproperties=font_prop)

# x축 레이블 설정
plt.xticks(rotation=0, fontproperties=font_prop)

# 범례 폰트 설정
plt.legend(prop=font_prop)  # 범례의 폰트를 Malgun Gothic으로 설정

plt.tight_layout()  # 레이아웃 조정
plt.show()  # 그래프 표시

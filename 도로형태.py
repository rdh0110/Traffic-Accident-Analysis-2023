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
df = pd.read_csv(file_path , encoding='euc-kr')  


# 열 이름 확인 및 공백 제거
df.columns = df.columns.str.strip()

# 요일별 빈도수 계산
weekday_counts = df['도로형태_대분류'].value_counts().reindex(['단일로', '교차로','기타'])

# x축 레이블을 두 줄로 나누기
weekday_counts.index = [label.replace(' ', '\n', 1) for label in weekday_counts.index]

# 막대그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 조정
bars = plt.bar(weekday_counts.index, weekday_counts.values, color='skyblue')  # 막대그래프 생성

# 각 막대 위에 수치 표시
for bar in bars:
    yval = bar.get_height()  # 막대의 높이(값)
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), 
             ha='center', va='bottom', fontproperties=font_prop)

plt.xlabel('도로형태_대분류', fontproperties=font_prop) 
plt.ylabel('빈도수', fontproperties=font_prop)  
plt.title('도로형태에 따른 교통사고 발생 수', fontproperties=font_prop)  # 그래프 제목
plt.xticks(rotation=0, fontproperties=font_prop)  
plt.tight_layout()  # 레이아웃 조정
plt.show()  # 그래프 표시

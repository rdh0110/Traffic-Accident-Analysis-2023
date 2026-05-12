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

# 도로형태와 가해자 법규 위반 각각의 빈도수 계산
road_types = ['단일로', '교차로', '기타']
offender_types = ['안전운전 의무 불이행', '신호위반', '보행자 보호의무 위반', 
                  '중앙선 침범', '교차로 통행방법 위반', '안전거리 미확보', '기타']

# 도로형태와 각 가해자 법규 위반의 발생 수를 저장할 리스트
data = []

# 도로형태와 가해자 법규 위반을 조합하여 사고 수를 계산
for road in road_types:
    for offender in offender_types:
        count = df[(df['도로형태_대분류'] == road) & (df['가해자법규위반'] == offender)].shape[0]
        data.append([road, offender, count])

# DataFrame으로 변환
combined_data = pd.DataFrame(data, columns=['도로형태', '가해자법규위반', '사고수'])

# 그래프 설정
fig, ax = plt.subplots(figsize=(12, 8))

# 각 도로형태별로 막대 위치 설정
bar_width = 0.2  # 막대 너비
x = range(len(offender_types))  # x축 위치 리스트

# 각 도로형태에 대한 막대 그리기
for i, road in enumerate(road_types):
    road_data = combined_data[combined_data['도로형태'] == road]
    ax.bar([j + i * bar_width for j in x], 
           road_data['사고수'], 
           width=bar_width, 
           label=road)

# 그래프 제목 및 축 레이블 설정
plt.title('도로형태에 따른 가해자 법규 위반별 교통사고 발생 수', fontproperties=font_prop)
plt.xlabel('가해자 법규 위반', fontproperties=font_prop)
plt.ylabel('사고 수', fontproperties=font_prop)

# x축 레이블 설정
plt.xticks([r + bar_width for r in range(len(offender_types))], offender_types, fontproperties=font_prop)

# 범례 추가 및 폰트 설정
legend = plt.legend(title='도로형태', prop=font_prop, loc='upper right')
for text in legend.get_texts():
    text.set_fontproperties(font_prop)
legend.get_title().set_fontproperties(font_prop)  # 범례 제목 폰트 설정

# 각 막대 위에 수치 표시
for i in range(len(offender_types)):
    for j in range(len(road_types)):
        height = combined_data[(combined_data['도로형태'] == road_types[j]) & 
                               (combined_data['가해자법규위반'] == offender_types[i])]['사고수'].values[0]
        ax.text(i + j * bar_width, height, int(height), ha='center', va='bottom', fontproperties=font_prop)

plt.tight_layout()  # 레이아웃 조정
plt.show()  # 그래프 표시

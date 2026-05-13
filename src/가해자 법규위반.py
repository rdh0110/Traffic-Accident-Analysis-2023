import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 1. 파일 경로 설정
# 현재 파이썬 파일의 위치를 기준으로 상위 폴더의 'data' 폴더 내 CSV 파일을 지칭합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', '도로교통공단_사망 교통사고 정보_20231231.csv')

# 2. 한글 폰트 전역 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 3. 데이터 불러오기 및 전처리
try:
    df = pd.read_csv(file_path, encoding='euc-kr')
    df.columns = df.columns.str.strip() # 컬럼명 공백 제거
except FileNotFoundError:
    print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: {file_path}")
    exit()

# 4. 데이터 가공
target_labels = ['안전운전 의무 불이행', '신호위반', '보행자 보호의무 위반', 
                 '중앙선 침범', '교차로 통행방법 위반', '안전거리 미확보', '기타']

# 데이터 집계 및 순서 정렬 (reindex를 사용해 항목 유지 및 순서 고정)
counts = df['가해자법규위반'].value_counts().reindex(target_labels, fill_value=0)

# x축 레이블 가독성 높이기 (긴 텍스트 줄바꿈)
counts.index = [label.replace(' ', '\n', 1) for label in counts.index]

# 5. 시각화 (그래프 그리기)
plt.figure(figsize=(12, 7), facecolor='#f8f9fa') 

# 세련된 색상 적용
bars = plt.bar(counts.index, counts.values, color='#4a90e2', edgecolor='#2c3e50', linewidth=1)

# 막대 위에 숫자 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{int(yval):,}', 
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# 그래프 세부 정보 설정
plt.title('2023년 가해자 법규위반별 사망 교통사고 현황', fontsize=18, pad=25)
plt.xlabel('법규 위반 항목', fontsize=13, labelpad=15)
plt.ylabel('발생 건수 (건)', fontsize=13, labelpad=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)

plt.tight_layout()

# 6. 결과 출력
print(f"분석 완료! 사용된 파일: {file_path}")
plt.show()

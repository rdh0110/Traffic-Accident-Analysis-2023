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

if not file_path:
    print("파일이 선택되지 않아 프로그램을 종료합니다.")
else:
    # 2. 한글 폰트 전역 설정 (깔끔하게 한 번만 설정)
    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name) # 이제 모든 글자에 한글이 자동 적용됨
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

    # 3. 데이터 불러오기 및 전처리
    df = pd.read_csv(file_path, encoding='euc-kr')
    df.columns = df.columns.str.strip() # 컬럼명 공백 제거

    # 4. 데이터 가공
    target_labels = ['안전운전 의무 불이행', '신호위반', '보행자 보호의무 위반', 
                     '중앙선 침범', '교차로 통행방법 위반', '안전거리 미확보', '기타']
    
    # 데이터 집계 및 순서 정렬
    counts = df['가해자법규위반'].value_counts().reindex(target_labels, fill_value=0)

    # x축 레이블 가독성 높이기 (긴 텍스트 줄바꿈)
    counts.index = [label.replace(' ', '\n', 1) for label in counts.index]

    # 5. 시각화 (그래프 그리기)
    plt.figure(figsize=(12, 7), facecolor='#f8f9fa') # 배경색 살짝 추가
    
    # 세련된 색상 적용 (기본 skyblue보다 조금 더 깊은 색)
    bars = plt.bar(counts.index, counts.values, color='#4a90e2', edgecolor='#2c3e50', linewidth=1)

    # 막대 위에 숫자 표시
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{int(yval):,}', 
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 그래프 세부 정보 (폰트 설정을 빼도 잘 나옵니다!)
    plt.title('2023년 가해자 법규위반별 사망 교통사고 현황', fontsize=18, pad=25)
    plt.xlabel('법규 위반 항목', fontsize=13, labelpad=15)
    plt.ylabel('발생 건수 (건)', fontsize=13, labelpad=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7) # 격자 추가로 가독성 향상
    plt.xticks(fontsize=11)
    
    plt.tight_layout()
    
    # 6. 결과 출력
    print(f"분석 완료! 선택된 파일: {file_path}")
    plt.show()

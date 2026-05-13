import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 1. 파일 경로 자동 설정 (src 폴더 기준 상위 data 폴더)
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', '도로교통공단_사망 교통사고 정보_20231231.csv')

# 2. 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf" 
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False

# 3. 데이터 불러오기
try:
    df = pd.read_csv(file_path, encoding='euc-kr')  
    df.columns = df.columns.str.strip()
except FileNotFoundError:
    print("데이터 파일을 찾을 수 없습니다. data 폴더를 확인해주세요.")
    exit()

# 4. 데이터 가공 및 집계 로직
road_types = ['단일로', '교차로', '기타']
offender_types = ['안전운전 의무 불이행', '신호위반', '보행자 보호의무 위반', 
                  '중앙선 침범', '교차로 통행방법 위반', '안전거리 미확보', '기타']

data = []
for road in road_types:
    for offender in offender_types:
        count = len(df[(df['도로형태_대분류'] == road) & (df['가해자법규위반'] == offender)])
        data.append([road, offender, count])

combined_data = pd.DataFrame(data, columns=['도로형태', '가해자법규위반', '사고수'])

# 5. 시각화
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
x = range(len(offender_types))

for i, road in enumerate(road_types):
    road_data = combined_data[combined_data['도로형태'] == road]
    ax.bar([j + i * bar_width for j in x], road_data['사고수'], width=bar_width, label=road)

plt.title('도로형태에 따른 가해자 법규 위반별 교통사고 발생 수', pad=20)
plt.xlabel('가해자 법규 위반', labelpad=15)
plt.ylabel('사고 수', labelpad=15)
plt.xticks([r + bar_width for r in range(len(offender_types))], offender_types)
plt.legend(title='도로형태')
plt.tight_layout()
plt.show()

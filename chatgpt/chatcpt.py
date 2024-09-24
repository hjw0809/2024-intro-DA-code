import csv
from datetime import datetime

# 파일 경로 지정
file_path = 'chatgpt\seoul.csv'

# 초기 변수 설정
max_temp = float('-inf')
max_temp_date = None

# 'euc-kr' 인코딩으로 파일 읽기
with open(file_path, mode='r', encoding='euc-kr') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 스킵

    for row in reader:
        try:
            date = datetime.strptime(row[1], '%Y-%m-%d')  # 날짜 열
            temp = float(row[5])  # 최고기온(℃) 열

            if temp > max_temp:
                max_temp = temp
                max_temp_date = date

        except ValueError:
            continue  # 변환 오류가 있는 경우 건너뜀

# 결과 출력
if max_temp_date:
    print(f"서울에서 가장 높은 기온이 기록된 날짜: {max_temp_date.strftime('%Y-%m-%d')}")
    print(f"기온: {max_temp}°C")

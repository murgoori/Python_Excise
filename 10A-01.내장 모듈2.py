# -*- coding: utf-8 -*-
"""
============================================================
파이썬 표준 라이브러리, 즉 기본 제공 모듈 수업 예제
============================================================

[학습 목표]
1. 모듈(module)이 무엇인지 이해하고 import로 불러올 수 있다.
2. math, random, datetime, time, os, sys, json, collections 모듈의 대표 기능을 사용할 수 있다.
3. 단순한 함수 사용에서 시작해 작은 문제 해결 프로그램으로 확장할 수 있다.
4. 난수, 날짜 계산, 파일 경로, JSON 저장, 데이터 집계가 실제 프로그램에서 어떻게 연결되는지 이해한다.
"""

# 표준 라이브러리는 파이썬 설치만 되어 있으면 바로 import해서 사용 가능
import json
import math
import os
import random
import statistics
import sys
import time
from collections import Counter, defaultdict, deque
from datetime import date, datetime, timedelta
from pathlib import Path

# ------------------------------------------------------------
# 공통 도우미 함수
# ------------------------------------------------------------
def border(title, sign="=", width=72):
    line = sign * width
    print("\n" + line)
    print(title)
    print(line)

def get_base_dir():
    """예제 파일을 저장할 폴더 경로 생성

    __file__ : 현재 실행 중인 파이썬 파일의 경로
    다만, 주피터 노트북이나 일부 온라인 실행 환경에서는 __file__이 없을 수 있음.
    그래서 try-except를 사용해 __file__이 없으면 현재 작업 폴더 Path.cwd()를 사용.
    """
    try:
        base_dir = Path(__file__).resolve().parent
    except NameError:
        base_dir = Path.cwd()

    data_dir = base_dir / "내장 모듈2_lesson_data"
    data_dir.mkdir(exist_ok=True)   # 폴더가 이미 있으면 오류를 내지 않고 넘어감
    return data_dir

DATA_DIR = get_base_dir()

# ------------------------------------------------------------
# 1. math: 수학 계산을 도와주는 모듈
# ------------------------------------------------------------
def lesson_math():
    # --------------------------------------------------------
    # [함수 설명]
    # math 모듈 : 원주율, 제곱근, 올림/내림, 두 점 사이 거리, 삼각함수 등
    # --------------------------------------------------------
    border("1. math 모듈 - 게임 맵과 체육대회에서 만나는 수학")

    # [기초] 원의 넓이 구하기
    # math.pi는 원주율 pi 값을 담고 있는 상수.
    # **는 거듭제곱 연산자. radius ** 2는 radius의 제곱.
    radius = 5
    area = math.pi * (radius ** 2)
    print(f"[기초] 반지름 {radius}m인 원형 무대의 넓이: {area:.2f}㎡")

    # [기초] 반올림과 올림/내림
    # round(x, 2) : 소수 둘째 자리까지 반올림.
    # math.sqrt() : 제곱근
    # math.ceil은 올림, math.floor는 내림.
    pizza_area = math.pi * (10 ** 2)
    print(f"[기초] 피자 넓이 원본값: {pizza_area}")
    print(f"[기초] 피자 넓이 반올림: {round(pizza_area, 2)}")
    print(f"[기초] 필요한 포장지 한 변 길이 올림: {math.ceil(math.sqrt(pizza_area))}cm")
    print(f"[기초] 소수점 아래를 버린 넓이: {math.floor(pizza_area)}㎠")

    # [중급] 두 점 사이의 거리 구하기
    # 게임 맵에서 플레이어와 보스 몬스터 사이의 거리 구하기.
    # 피타고라스 정리: sqrt((x2-x1)^2 + (y2-y1)^2)
    player_x, player_y = 2, 3
    boss_x, boss_y = 11, 15
    distance_by_sqrt = math.sqrt((boss_x - player_x) ** 2 + (boss_y - player_y) ** 2)

    # math.hypot(a, b) : a, b는 밑변과 높이 두 변의 길이. hypotenuse(빗변)
    distance_by_hypot = math.hypot(boss_x - player_x, boss_y - player_y)
    print(f"[중급] 플레이어와 보스의 거리 sqrt 방식: {distance_by_sqrt:.2f}")
    print(f"[중급] 플레이어와 보스의 거리 hypot 방식: {distance_by_hypot:.2f}")

    # [중급] 각도와 라디안(1라디안 : 호의 길이와 반지름의 길이가 같게 되는 만큼의 각)
    # sin, cos, tan은 각도를 그대로 쓰지 않고 라디안(radian)을 사용.
    # 45도는 math.radians(45)로 먼저 변환.
    angle_degree = 45
    angle_radian = math.radians(angle_degree)
    sin_value = math.sin(angle_radian)
    cos_value = math.cos(angle_radian)
    print(f"[중급] {angle_degree}도의 sin 값: {sin_value:.3f}")
    print(f"[중급] {angle_degree}도의 cos 값: {cos_value:.3f}")

    # [응용] 농구공이 날아간 위치 예측하기
    # x방향 이동량과 y방향 이동량을 삼각함수
    speed = 20          # 공을 던진 힘, 임의 단위
    throw_angle = 30    # 던지는 각도
    rad = math.radians(throw_angle)
    x_power = speed * math.cos(rad)     # 빗변에 대한 밑변의 비율(가로 방향의 비율)
    y_power = speed * math.sin(rad)     # 빗변에 대한 높이의 비율(세로 방향의 비율)
    print(f"[응용] {throw_angle}도로 던진 공의 가로 방향 힘: {x_power:.2f}")
    print(f"[응용] {throw_angle}도로 던진 공의 세로 방향 힘: {y_power:.2f}")

    # [미니 과제]
    # 1. player_x, player_y, boss_x, boss_y 값을 바꾸어 거리를 다시 계산하기.
    # 2. throw_angle을 15, 30, 45, 60도로 바꿔서 x_power와 y_power의 변화값 비교하기.

# ------------------------------------------------------------
# 2. random: 무작위 선택과 난수 생성
# ------------------------------------------------------------
def lesson_random():
    # [함수 설명]
    # random 모듈은 예측하기 어려운 값 생성.
    # 사용 : 게임 아이템 뽑기, 발표자 선정, 팀 배정, 메뉴 추천
    
    border("2. random 모듈 - 뽑기, 팀 배정, 아이템 드롭")

    # 컴퓨터의 난수는 완전한 진짜 무작위가 아니라 알고리즘으로 만든 의사 난수.

    # random.seed(값)을 사용하면 같은 난수 순서 사용.
    random.seed(2026)

    # [기초] 주사위 굴리기
    # randint(a, b)는 a 이상 b 이하의 무작위 정수
    dice = random.randint(1, 6)
    print(f"[기초] 주사위 한 번 굴리기: {dice}")

    # [기초] 리스트에서 하나 고르기
    lunch_menus = ["김치볶음밥", "돈가스", "마라탕", "비빔밥", "떡볶이", "카레라이스"]
    today_lunch = random.choice(lunch_menus)
    print(f"[기초] 오늘의 급식 추천 메뉴: {today_lunch}")

    # [중급] 중복 없이 여러 개 고르기
    # sample(목록, 개수)
    students = ["민준", "서연", "도윤", "지우", "하준", "하린", "지호", "서아"]
    presenters = random.sample(students, 2)
    print(f"[중급] 오늘 발표자 2명, 중복 없음: {presenters}")

    # [중급] 중복을 허용해 여러 개 고르기
    # choices(목록, k=개수)
    # weights(가중치)를 이용해서 빈도수 조정
    item_names = ["일반 포션", "고급 포션", "희귀 검", "전설 펫"]
    item_weights = [60, 30, 9, 1]           # 숫자가 클수록 나올 확률 상승 .
    dropped_items = random.choices(item_names, weights=item_weights, k=10)
    print(f"[중급] 몬스터 10마리 사냥 후 아이템: {dropped_items}")

    # [중급] 순서 섞기
    # shuffle은 원본 리스트 자체의 순서 변경
    team_members = students.copy()          # 복사본 생성
    random.shuffle(team_members)
    print(f"[중급] 무작위로 섞은 학생 순서: {team_members}")

    # [응용] 2명씩 팀 만들기
    teams = []
    for i in range(0, len(team_members), 2):    # 2명 간격으로
        teams.append(team_members[i:i + 2])     # 2명(리스트)을 team(2차원 리스트)에 추가
    print("[응용] 2명씩 랜덤 팀 배정:")
    for team_number, team in enumerate(teams, start=1):
        print(f"  {team_number}팀: {team}")

    # [응용] 뽑기 결과를 Counter와 연결해 빈도 분석
    item_counter = Counter(dropped_items)       # Dicionary와 비슷하게 {값:갯수} 형식으로 저장
    print(f"[응용] 아이템별 획득 개수: {item_counter}")

    # [미니 과제]
    # 1. item_weights를 바꾸어 전설 펫의 빈도수 높이기.
    # 2. 학생 수가 홀수일 때 마지막 팀은 몇 명이 되는지 확인.

# ------------------------------------------------------------
# 3. datetime: 날짜와 시간 계산
# ------------------------------------------------------------
def lesson_datetime():
    # --------------------------------------------------------
    # [함수 설명]
    # datetime 모듈은 날짜와 시간을 계산하기 위한 표준 도구.
    # date, datetime, timedelta 같은 객체로 변경
    # --------------------------------------------------------
    border("3. datetime 모듈 - 학교 행사 D-Day 계산")

    # "2026-05-20" <= 문자열 
    # 날짜 계산을 하려면 date 또는 datetime 객체로 변경해야 함.

    # [기초] 현재 날짜와 시간 가져오기
    now = datetime.now()
    print(f"[기초] 현재 날짜와 시간 원본: {now}")

    # strftime은 날짜와 시간을 원하는 형식의 문자열로 바꾸는 메서드.
    # %Y: 4자리 연도, %m: 2자리 월, %d: 2자리 일
    # %H: 24시간제 시, %M: 분, %S: 초
    formatted_now = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    print(f"[기초] 보기 좋게 바꾼 현재 시각: {formatted_now}")

    # [기초] 요일을 한글로 출력하기
    # weekday()는 월요일을 0, 화요일을 1, ..., 일요일을 6으로 알려 준다.
    weekday_names = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    print(f"[기초] 오늘의 요일: {weekday_names[now.weekday()]}")

    # [중급] 날짜끼리 빼기
    # 날짜끼리 빼면 timedelta 객체 생성. timedelta는 '기간'을 나타냄.
    today = date.today()    # 오늘 날짜 : 2026-05-27
    festival_day = today + timedelta(days=30)       # 30일 뒤의 날짜
    days_left = festival_day - today                # 남은 기간(일,시:분:초) : 30 days, 0:00:00
    print(f"[중급] 학교 축제일: {festival_day}")
    print(f"[중급] 학교 축제까지 남은 날: D-{days_left.days}")

    # [중급] 특정 날짜 직접 만들기
    # date(연도, 월, 일) 형식으로 날짜 객체 생성.
    club_start = date(today.year, 3, 2)
    club_end = date(today.year, 12, 24)
    club_period = club_end - club_start
    print(f"[중급] 올해 동아리 활동 기간: {club_period.days}일")

    # [응용] 시험 일정표에서 가장 가까운 시험 찾기
    exam_schedule = {
        "1차 지필평가": today + timedelta(days=12),
        "수행평가 발표": today + timedelta(days=5),
        "2차 지필평가": today + timedelta(days=48),
    }

    nearest_exam_name = None
    nearest_exam_day = None
    nearest_days = None

    for exam_name, exam_day in exam_schedule.items():
        diff = (exam_day - today).days
        if nearest_days is None or diff < nearest_days:
            nearest_exam_name = exam_name
            nearest_exam_day = exam_day
            nearest_days = diff

    print(f"[응용] 가장 가까운 일정: {nearest_exam_name}, 날짜: {nearest_exam_day}, D-{nearest_days}")

    # [미니 과제]
    # 1. 자신의 생일까지 며칠 남았는지 계산하는 코드 작성.
    # 2. exam_schedule에 새로운 시험이나 발표 일정 추가.

# ------------------------------------------------------------
# 4. time: 실행 시간 측정과 잠깐 멈추기
# ------------------------------------------------------------
def lesson_time():
    # --------------------------------------------------------
    # [함수 설명]
    # time 모듈은 프로그램이 실행되는 동안 흐르는 시간, 타이머
    # 잠깐 멈추기, 코드 실행 시간 측정에 자주 사용된다.
    # --------------------------------------------------------
    border("4. time 모듈 - 타이머와 코드 속도 측정")

    # time은 '흐르는 시간', '잠깐 멈추기', '실행 시간 측정'에 사용.

    # [기초] 현재 시각 출력하기
    # localtime은 현재 지역 시간 정보를 구조화된 형태로 반환.
    current_time = time.localtime()
    formatted_time = time.strftime("%H시 %M분 %S초", current_time)
    print(f"[기초] 현재 시각: {formatted_time}")

    # [기초] sleep으로 잠깐 멈추기
    # sleep(초)는 프로그램을 해당 초만큼 정지.
    print("[기초] 1초 타이머 시작!")
    time.sleep(1)
    print("[기초] 1초가 지났습니다.")

    # [중급] 코드 실행 시간 측정하기
    # perf_counter는 비교적 정밀하게 측정.
    start = time.perf_counter()

    total = 0
    for number in range(1, 100_001):        # # 밑줄(_)은 숫자를 보기 좋게 쓰기 위한 표시. 100_001은 100001과 같은 값.
        total += number

    end = time.perf_counter()
    elapsed = end - start
    print(f"[중급] 1부터 100000까지 더한 값: {total}")  # 5000050000
    print(f"[중급] 반복문 실행 시간: {elapsed:.6f}초")  # 0.002457

    # [응용] 리스트 컴프리헨션과 반복문 속도 비교, 제곱값 리스트에 저장하는 속도 비교
    start_loop = time.perf_counter()        # 현재 시간 저장 : 23186.3466051 <= 저장된 값 예시
    squares_loop = []
    for x in range(1, 50_001):
        squares_loop.append(x ** 2)
    end_loop = time.perf_counter()          # 

    start_comprehension = time.perf_counter()
    squares_comprehension = [x ** 2 for x in range(1, 50_001)]  # 리스트 컴프리핸션은 for문보다 반복문 속도 빠름
    end_comprehension = time.perf_counter()

    print(f"[응용] for 반복문 리스트 생성 시간: {end_loop - start_loop:.6f}초")
    print(f"[응용] 리스트 컴프리헨션 생성 시간: {end_comprehension - start_comprehension:.6f}초")
    print(f"[응용] 두 결과가 같은가? {squares_loop == squares_comprehension}")
    
    # [미니 과제]
    # 1. range의 크기를 10000, 100000, 1000000으로 변경해서 실행 시간 비교.
    # 2. sleep 시간을 3초로 바꾸어 카운트다운 프로그램 제작.

# ------------------------------------------------------------
# 5. os: 운영체제와 파일/폴더 다루기
# ------------------------------------------------------------
def lesson_os():
    # --------------------------------------------------------
    # [함수 설명]
    # os 모듈은 파이썬 프로그램이 운영체제와의 소통 기능
    # 현재 작업 폴더 확인, 파일 목록 가져오기, 파일 정보 확인,환경 변수 읽기 등 컴퓨터의 실제 파일 시스템과 연결되는 기능.
    # 주의: os.system은 운영체제 명령을 직접 실행하므로, 사용자 입력을 그대로 넣으면 위험할 수 있다.
    border("5. os 모듈 - 내 컴퓨터의 폴더와 파일 살펴보기")

    # [기초] 현재 작업 디렉터리 확인
    current_dir = os.getcwd()           # get Current Working Directory
    print(f"[기초] 현재 작업 디렉터리: {current_dir}")

    # [기초] 운영체제 종류 확인
    # os.name은 Windows에서는 'nt', macOS/Linux에서는 'posix'인 경우가 많음.
    print(f"[기초] os.name 값: {os.name}")

    # [기초] 현재 폴더 파일 목록 보기
    # os.listdir('.')에서 '.'은 현재 폴더를 뜻한다.
    files = os.listdir('.')                         # 현재 폴더내의 파일 목록 저장
    print("[기초] 현재 폴더의 일부 항목:")
    for filename in files[:5]:
        print(f"  - {filename}")

    # [중급] 파일 존재 여부, 크기, 수정 시각 확인
    memo_path = DATA_DIR / "school_memo.txt"
    memo_path.write_text("파이썬 표준 라이브러리 수업 메모\n", encoding="utf-8")

    # os.path 함수는 문자열 경로를 받는 경우가 많음.
    # Path 객체도 대부분 자동으로 처리되지만, str()로 바꾸면 더 명확해짐.
    memo_path_str = str(memo_path)
    if os.path.exists(memo_path_str):
        size = os.path.getsize(memo_path_str)
        modified_timestamp = os.path.getmtime(memo_path_str)
        modified_time = datetime.fromtimestamp(modified_timestamp)
        print(f"[중급] {memo_path.name} 파일이 존재합니다.")
        print(f"[중급] 파일 크기: {size} bytes")
        print(f"[중급] 마지막 수정 시각: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # [중급] 환경 변수 읽기
    # 환경 변수는 운영체제가 프로그램에 알려 주는 설정값
    # 예: 사용자 이름, 홈 폴더, 임시 폴더 등
    home_dir = os.environ.get("HOME") or os.environ.get("USERPROFILE")
    print(f"[중급] 사용자 홈 폴더: {home_dir}")

    # [응용] os.system 
    # 아래 코드는 운영체제별 화면 지우기 명령
    clear_command = "cls" if os.name == "nt" else "clear"
    print(f"[응용] 이 운영체제에서 화면 지우기 명령은 보통 '{clear_command}'입니다.")
    print("[응용] os.system(clear_command)는 가능하지만, 초보 단계에서는 꼭 필요한 경우에만 사용합니다.")
    # os.system(clear_command)

    # [미니 과제]
    # 1. DATA_DIR 폴더 안에 자기 이름이 들어간 txt 파일 생성하기.
    # 2. 현재 폴더의 파일 중 .py로 끝나는 파일만 출력.

# ------------------------------------------------------------
# 6. sys: 파이썬 실행 환경 정보
# ------------------------------------------------------------
def lesson_sys():
    # --------------------------------------------------------
    # [함수 설명]
    # sys 모듈은 현재 실행 중인 파이썬 인터프리터 자체의 정보를 제공.
    # 파이썬 버전, 실행 플랫폼, 명령줄 인수, import 경로 등를 살펴본다.
    # --------------------------------------------------------
    border("6. sys 모듈 - 파이썬 인터프리터 정보 확인")

    # [기초] 파이썬 버전 확인
    print(f"[기초] 파이썬 버전: {sys.version}")

    # [기초] 실행 플랫폼 확인
    # sys.platform은 win32, darwin, linux 
    print(f"[기초] 실행 플랫폼: {sys.platform}")

    # [중급] 명령줄 인수 확인
    # 터미널에서 python 파일명.py apple banana 처럼 실행하면
    # sys.argv에는 ['파일명.py', 'apple', 'banana']처럼 저장.
    print("[중급] 명령줄 인수 sys.argv:")
    for index, argument in enumerate(sys.argv):
        print(f"  sys.argv[{index}] = {argument}")

    # [중급] 모듈 검색 경로 확인
    # import를 할 때 파이썬은 sys.path에 들어 있는 폴더들을 차례대로 찾아본다.
    print("[중급] 파이썬이 모듈을 찾는 경로 중 앞의 5개:")
    for path in sys.path[:5]:
        print(f"  - {path}")

    # [응용] 실행 환경에 따라 다른 안내문 출력하기
    if sys.platform.startswith("win"):
        message = "Windows 환경입니다. 명령 프롬프트 또는 PowerShell에서 실행할 수 있습니다."
    elif sys.platform == "darwin":
        message = "macOS 환경입니다. 터미널에서 실행할 수 있습니다."
    else:
        message = "Linux 또는 기타 Unix 계열 환경입니다. 터미널에서 실행할 수 있습니다."
    print(f"[응용] {message}")

    # sys.exit() : 프로그램 즉시 종료.
    # sys.exit("프로그램을 종료합니다.")

    # [미니 과제]
    # 1. 터미널에서 이 파일 뒤에 자신의 이름을 붙여 실행하고 sys.argv 결과 확인하기.
    # 2. sys.path에 어떤 폴더들이 들어 있는지 출력 개수를 늘려 확인하기.

# ------------------------------------------------------------
# 7. json: 데이터를 문자열 또는 파일로 저장하기
# ------------------------------------------------------------
def lesson_json():
    # --------------------------------------------------------
    # [함수 설명]
    # JSON은 JavaScript Object Notation의 약자이다.
    # 파이썬의 딕셔너리와 리스트 구조를 저장하거나 다른 프로그램과 주고받기 쉬운 JSON 형식으로 변환
    # 게임 랭킹, 사용자 설정, 설문 결과, 웹 API 데이터 처리 등에 사용
    border("7. json 모듈 - 게임 랭킹과 설문 결과 저장")

    # [기초] 파이썬 딕셔너리를 JSON 문자열로 바꾸기
    student_profile = {
        "name": "김파이",
        "grade": 1,
        "favorite_subjects": ["정보", "수학", "체육"],
        "is_club_member": True,
    }

    # 객체(Dictionary)를 JSON 문자열로 변환
    # dumps의 s는 string. 
    # ensure_ascii=False는 한글이 \uac00 같은 코드로 변환되지 않고 바로 보임.
    json_text = json.dumps(student_profile, ensure_ascii=False, indent=4)
    print("[기초] 딕셔너리를 JSON 문자열로 변환:")
    print(json_text)

    # [기초] JSON 문자열을 다시 파이썬 객체 Dictionary 로 변환
    restored_profile = json.loads(json_text)
    print(f"[기초] JSON 문자열을 다시 변환한 자료형: {type(restored_profile)}")     # <class 'dict'>
    print(f"[기초] 복원한 이름: {restored_profile['name']}")

    # [중급] 게임 랭킹 데이터를 JSON 파일로 저장하기
    ranking_data = {
        "game_title": "Python High School Quest",
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "players": [
            {"nickname": "LoopMaster", "score": 9800, "level": 25},
            {"nickname": "BugHunter", "score": 8700, "level": 22},
            {"nickname": "ListWizard", "score": 9100, "level": 24},
        ],
    }

    json_file = DATA_DIR / "game_ranking.json"
    with open(json_file, "w", encoding="utf-8") as file:
        # dump는 파일에 직접 저장한다. dumps는 문자열로 만든다.
        json.dump(ranking_data, file, ensure_ascii=False, indent=4)

    print(f"[중급] JSON 파일 저장 완료: {json_file}")

    # [중급] JSON 파일 읽기
    with open(json_file, "r", encoding="utf-8") as file:
        loaded_ranking = json.load(file)

    print("[중급] JSON 파일에서 읽은 랭킹:")
    for player in loaded_ranking["players"]:
        print(f"  - {player['nickname']}: {player['score']}점, Lv.{player['level']}")

    # [응용] 랭킹 데이터에서 1등 찾기
    # max 함수의 key 옵션을 사용하면 리스트 안의 딕셔너리 중 특정 값을 기준으로 최댓값을 찾을 수 있다.
    top_player = max(loaded_ranking["players"], key=lambda player: player["score"])
    print(f"[응용] 현재 1등: {top_player['nickname']} ({top_player['score']}점)")

    # [주의] JSON은 파이썬의 모든 자료형을 그대로 저장하지는 않는다.
    # 예를 들어 튜플은 JSON으로 저장하면 리스트처럼 변한다.
    tuple_data = {"position": (3, 5)}
    tuple_json = json.dumps(tuple_data)
    tuple_restored = json.loads(tuple_json)
    print(f"[주의] 튜플을 JSON으로 저장 후 읽으면: {tuple_restored}, 자료형: {type(tuple_restored['position'])}")

    # [미니 과제]
    # 1. ranking_data에 자신의 닉네임과 점수를 추가해 보자.
    # 2. 점수가 높은 순서대로 players를 정렬해 출력해 보자.

# ------------------------------------------------------------
# 8. collections: 자료를 더 편하게 다루는 컨테이너
# ------------------------------------------------------------
def lesson_collections():
    # --------------------------------------------------------
    # [함수 설명]
    # collections 모듈은 리스트와 딕셔너리보다 편리한 자료구조를 제공한다.
    # Counter는 개수 세기, defaultdict는 자동 그룹 만들기,
    # deque는 빠른 대기열 처리에 적합하다.
    #
    # [수업 흐름]
    # 1. Counter로 간식 투표 결과를 집계한다.
    # 2. 문자열을 split한 뒤 단어 빈도를 분석한다.
    # 3. defaultdict(list)로 동아리별 학생 명단을 만든다.
    # 4. deque로 앞에서 꺼내는 대기열을 구현한다.
    # 5. 게임 전투 로그를 몬스터별 승패 기록으로 정리한다.
    # --------------------------------------------------------
    border("8. collections 모듈 - 채팅 로그와 대기열 분석")

    # collections 모듈은 리스트, 딕셔너리 같은 기본 자료구조를 더 편리하게 만든 도구들을 제공한다.
    # 여기서는 Counter, defaultdict, deque를 사용한다.

    # [기초] Counter로 개수 세기
    # Counter는 리스트 안에 같은 값이 몇 번 나오는지 세어 주는 딕셔너리 비슷한 객체이다.
    snack_votes = ["초코우유", "딸기우유", "초코우유", "바나나우유", "초코우유", "딸기우유"]
    vote_counter = Counter(snack_votes)
    print(f"[기초] 간식 투표 결과: {vote_counter}")
    print(f"[기초] 가장 인기 있는 간식 1개: {vote_counter.most_common(1)}")

    # [중급] 문자열에서도 Counter 사용 가능
    # 공백을 기준으로 단어를 나누면 단어 빈도 분석을 할 수 있다.
    chat = "파이썬 재미있다 파이썬 어렵다 하지만 파이썬 쓸모있다 재미있다"
    words = chat.split()
    word_counter = Counter(words)
    print(f"[중급] 채팅 단어 빈도: {word_counter}")

    # [중급] defaultdict로 그룹 만들기
    # 일반 딕셔너리는 없는 key에 바로 append하면 오류가 난다.
    # defaultdict(list)는 새 key가 등장하면 자동으로 빈 리스트를 만들어 준다.
    club_members = [
        ("밴드부", "민준"),
        ("코딩부", "서연"),
        ("밴드부", "도윤"),
        ("축구부", "지우"),
        ("코딩부", "하린"),
    ]

    club_dict = defaultdict(list)
    for club_name, student_name in club_members:
        club_dict[club_name].append(student_name)

    print("[중급] 동아리별 학생 명단:")
    for club_name, member_names in club_dict.items():
        print(f"  - {club_name}: {member_names}")

    # [중급] deque로 대기열 만들기
    # 리스트의 pop(0)은 앞에서 꺼낼 때 느릴 수 있다.
    # deque는 양쪽 끝에서 넣고 빼는 작업이 빠른 자료구조이다.
    waiting_queue = deque(["1번 손님", "2번 손님", "3번 손님"])
    waiting_queue.append("4번 손님")      # 오른쪽 끝에 추가
    first_customer = waiting_queue.popleft()  # 왼쪽 끝에서 꺼내기
    print(f"[중급] 먼저 입장한 사람: {first_customer}")
    print(f"[중급] 남은 대기열: {list(waiting_queue)}")

    # [응용] 게임 로그 분석하기
    battle_log = [
        ("슬라임", "승리"),
        ("고블린", "승리"),
        ("슬라임", "승리"),
        ("드래곤", "패배"),
        ("고블린", "패배"),
        ("슬라임", "승리"),
    ]

    monster_counter = Counter()
    result_by_monster = defaultdict(Counter)

    for monster, result in battle_log:
        monster_counter[monster] += 1
        result_by_monster[monster][result] += 1

    print(f"[응용] 몬스터별 만난 횟수: {monster_counter}")
    print("[응용] 몬스터별 승패:")
    for monster, result_counter in result_by_monster.items():
        print(f"  - {monster}: {dict(result_counter)}")

    # [미니 과제]
    # 1. battle_log에 새로운 전투 기록을 추가해 보자.
    # 2. 가장 많이 만난 몬스터를 most_common으로 찾아보자.

# ------------------------------------------------------------
# 9. pathlib: 파일 경로를 객체처럼 다루기 - 보강 모듈
# ------------------------------------------------------------
def lesson_pathlib():
    # --------------------------------------------------------
    # [함수 설명]
    # pathlib 모듈은 파일 경로를 문자열이 아니라 Path 객체로 다루게 해 준다.
    # os.path보다 코드가 읽기 쉽고, 폴더와 파일을 연결할 때 / 연산자를
    # 사용할 수 있어 초보자도 경로 구조를 이해하기 쉽다.
    #
    # [수업 흐름]
    # 1. DATA_DIR 폴더 안에 저장할 파일 경로를 만든다.
    # 2. write_text와 read_text로 텍스트 파일을 쓰고 읽는다.
    # 3. glob으로 특정 확장자의 파일만 찾는다.
    # 4. append 모드로 파일 끝에 내용을 추가한다.
    # --------------------------------------------------------
    border("9. pathlib 모듈 - 파일 경로를 더 읽기 쉽게 다루기")

    # pathlib은 os.path보다 현대적인 파일 경로 처리 도구이다.
    # 문자열을 +로 연결하지 않고 / 연산자로 경로를 이어 붙일 수 있어 읽기 쉽다.

    # [기초] Path 객체 만들기
    note_file = DATA_DIR / "club_note.txt"
    print(f"[기초] 저장할 파일 경로: {note_file}")

    # [기초] 텍스트 파일 쓰기와 읽기
    note_file.write_text("코딩부 오늘의 목표: 표준 라이브러리 익히기\n", encoding="utf-8")
    note_text = note_file.read_text(encoding="utf-8")
    print(f"[기초] 파일에서 읽은 내용: {note_text.strip()}")

    # [중급] 폴더 안의 특정 확장자 파일 찾기
    # glob("*.json")은 현재 폴더에서 .json으로 끝나는 파일을 찾는다.
    json_files = list(DATA_DIR.glob("*.json"))
    print("[중급] DATA_DIR 안의 JSON 파일:")
    for path in json_files:
        print(f"  - {path.name}")

    # [응용] 파일이 있으면 내용 추가하기
    # open의 'a' 모드는 append, 즉 기존 내용 뒤에 덧붙이는 모드이다.
    with open(note_file, "a", encoding="utf-8") as file:
        file.write("다음 목표: 나만의 모듈 만들기\n")

    print("[응용] 내용 추가 후 전체 파일 내용:")
    print(note_file.read_text(encoding="utf-8"))

    # [미니 과제]
    # 1. DATA_DIR 안에 diary.txt를 만들고 오늘 배운 내용을 저장해 보자.
    # 2. glob("*.txt")로 텍스트 파일 목록을 출력해 보자.

# ------------------------------------------------------------
# 10. statistics: 평균, 중앙값 등 통계 계산 - 보강 모듈
# ------------------------------------------------------------
def lesson_statistics():
    # --------------------------------------------------------
    # [함수 설명]
    # statistics 모듈은 평균, 중앙값, 최빈값, 표준편차 같은
    # 기본 통계값을 쉽게 구할 수 있게 해 준다.
    # 수행평가 점수, 설문 결과, 게임 점수 분석처럼 숫자 데이터를 이해하는 첫 단계에 활용하기 좋다.
    #
    # [수업 흐름]
    # 1. 점수 리스트를 준비한다.
    # 2. mean과 median으로 평균과 중앙값을 비교한다.
    # 3. mode로 가장 자주 나온 값을 찾는다.
    # 4. pstdev로 점수의 흩어짐 정도를 확인한다.
    # 5. 평균 이상인 점수만 골라 새 리스트를 만든다.
    # --------------------------------------------------------
    border("10. statistics 모듈 - 수행평가 점수 분석")

    # statistics는 평균, 중앙값, 최빈값, 표준편차 같은 기본 통계를 쉽게 계산해 준다.
    
    scores = [88, 92, 75, 100, 67, 88, 91, 83, 95, 88]

    # [기초] 평균과 중앙값
    # 평균은 모든 값을 더한 뒤 개수로 나눈 값이다.
    # 중앙값은 데이터를 크기순으로 정렬했을 때 가운데에 있는 값이다.
    mean_score = statistics.mean(scores)
    median_score = statistics.median(scores)
    print(f"[기초] 점수 목록: {scores}")
    print(f"[기초] 평균 점수: {mean_score:.2f}")
    print(f"[기초] 중앙값: {median_score}")

    # [중급] 최빈값
    # 최빈값은 가장 자주 등장한 값이다.
    mode_score = statistics.mode(scores)
    print(f"[중급] 가장 많이 나온 점수: {mode_score}")

    # [중급] 표준편차
    # 표준편차는 데이터가 평균에서 얼마나 흩어져 있는지 나타내는 값이다.
    # 값이 작을수록 점수들이 평균 근처에 모여 있고, 클수록 차이가 크다.
    stdev_score = statistics.pstdev(scores)
    print(f"[중급] 표준편차: {stdev_score:.2f}")

    # [응용] 평균 이상 학생 수 세기
    above_average = []
    for score in scores:
        if score >= mean_score:
            above_average.append(score)

    print(f"[응용] 평균 이상 점수 개수: {len(above_average)}개")
    print(f"[응용] 평균 이상 점수 목록: {above_average}")

    # [미니 과제]
    # 1. scores에 자신의 모둠 점수를 넣고 평균, 중앙값, 표준편차를 구해 보자.
    # 2. 90점 이상 점수만 뽑아 honor_scores 리스트를 만들어 보자.

# ------------------------------------------------------------
# 전체 실행 함수
# ------------------------------------------------------------
def main():
    border("파이썬 표준 라이브러리 수업 예제 시작", "#")

    lesson_math()               # math: 원주율, 제곱근, 거리 계산, 삼각함수 등 수학 계산 연습
    lesson_random()             # random: 주사위, 메뉴 추천, 발표자 뽑기, 아이템 확률, 팀 배정
    lesson_datetime()           # datetime: 현재 날짜, 날짜 형식 바꾸기, 요일, D-Day, 일정 계산
    lesson_time()               # time: 현재 시각 출력, sleep 타이머, 코드 실행 시간 측정
    lesson_os()                 # os: 현재 폴더 확인, 파일 목록, 파일 정보, 운영체제 환경 변수
    lesson_sys()                # sys: 파이썬 버전, 실행 플랫폼, 명령줄 인수, 모듈 검색 경로
    lesson_json()               # json: 딕셔너리/list를 JSON 문자열과 파일로 저장하고 다시 읽기
    lesson_collections()        # collections: Counter, defaultdict, deque로 데이터 집계와 대기열 처리
    lesson_pathlib()            # pathlib: Path 객체로 파일 경로 만들기, 파일 읽기/쓰기, 확장자 검색
    lesson_statistics()         # statistics: 평균, 중앙값, 최빈값, 표준편차, 평균 이상 데이터 찾기

    border("수업 예제 종료", "#")
    print(f"예제에서 만든 파일은 이 폴더에 저장되었습니다: {DATA_DIR}")

# 다른 파일에서 import할 때는 자동 실행되지 않음.
if __name__ == "__main__":
    main()
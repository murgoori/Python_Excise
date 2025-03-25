'''
[ 아래 과제 해결 ]

# 서술형수행평가 방식.(MAX : 20점)

가. 파일명, 실행 함수, 주석문								    - 8점

나. 탑승자 정보는 리스트에 저장(user)			                - 3점
    - 이름

다. 놀이기구 정보 딕셔너리에 저장.(rides)						- 3점
    - 이름(키값), 탑승가격, 탑승제한 나이

라. 함수 작성(find_rides)	                                  - 3점
    - 탑승 가능한 놀이기구가 있는지 여부 확인
    - 놀이기구 이름 존재 여부, 나이, 키 제한 확인
    - 리턴값 : True/False

마. 탑승 내역을 파일에 저장.(파일명 : "log.txt")			    - 3점
    - 탑승자 이름, 놀이기구, 탑승일시

바. 추가 기능 : 창의적인 추가 기능								- 3점

* 주의사항 : 각 항목에 해당되는 부분 중 가장 중요한 부분 1곳에 주석문으로 해당 항목을 표시해야 함.(표시 하지 않은 곳은 채점 대상 아님)
   예시)   abc=list();			// 나. 리스트에 저장
'''

# ------------------------------
# 놀이기구 정보 => 딕셔너리에 저장
# ------------------------------
ride1_name = "롤러코스터"
ride1_price = 5000
ride1_min_age = 12

ride2_name = "범퍼카"
ride2_price = 3000
ride2_min_age = 10

ride3_name = "자이로드롭"
ride3_price = 6000
ride3_min_age = 15

ride4_name = "회전목마"
ride4_price = 2000
ride4_min_age = 5

ride5_name = "바이킹"
ride5_price = 5500
ride5_min_age = 14

# 최소 탑승 키
min_height = 100

# ------------------------------
# 사용자 입력 받기 => 사용자 이름을 리스트에 저장
# ------------------------------
input_name = input("이름 입력: ")
age = int(input("나이 입력: "))
height = int(input("키(cm) 입력: "))
ride_choice = input("놀이기구를 선택(롤러코스터, 범퍼카, 자이로드롭, 회전목마, 바이킹): ")

# ------------------------------
# 놀이기구 정보 찾기
# ------------------------------
if ride_choice == ride1_name:
    min_age = ride1_min_age
    price = ride1_price
elif ride_choice == ride2_name:
    min_age = ride2_min_age
    price = ride2_price
elif ride_choice == ride3_name:
    min_age = ride3_min_age
    price = ride3_price
elif ride_choice == ride4_name:
    min_age = ride4_min_age
    price = ride4_price
elif ride_choice == ride5_name:
    min_age = ride5_min_age
    price = ride5_price
else:
    print("입력한 놀이기구가 존재하지 않습니다.")
    exit()

# ------------------------------
# 탑승 조건 검사 및 결과 출력
# ------------------------------
print("🎇" * 20)
print("🎇🎇  놀이기구 탑승 가능 확인 시스템 🎇🎇")
print("🎇" * 20)
if age >= min_age and height >= min_height:
    print(f"{input_name}님은 {ride_choice}에 탑승 가능합니다!")
    print(f"탑승 요금: {price}원")
else:
    print(f"죄송합니다. {input_name}님은 {ride_choice}에 탑승할 수 없습니다.")

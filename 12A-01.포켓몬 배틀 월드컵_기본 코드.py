# ============================================================
# [프로젝트] 포켓몬 배틀 월드컵 - requests API 실습
# ============================================================
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============================================================
# 1. requests 기본 요청
# ============================================================
def request_json(url):
    """
    URL에 요청을 보내고 JSON 데이터 반환

    requests.get(url) : 웹 서버에 데이터를 요청
    response : 서버가 보내준 응답 결과
    response.status_code : 요청이 성공했는지 실패했는지 알려주는 숫자
    - 200: 정상 성공
    - 404: 요청한 주소를 찾을 수 없음
    - 500: 서버 내부 오류
    response.json() : JSON 형태의 문자열 데이터를 딕셔너리 또는 리스트로 변환
    """

    try:
        response = requests.get(url, timeout=10, verify=False)

        print(f"[요청 주소] {url}")
        print(f"[응답 코드] {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("[요청 실패] 데이터를 가져오지 못했습니다.")
            return None

    except requests.exceptions.RequestException as error:
        print("[오류] 웹 요청 중 문제가 발생했습니다.")
        print(error)
        return None

# ============================================================
# 2. 포켓몬 목록 가져오기
# ============================================================
def get_pokemon_list(limit=20):

    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=0"   # offset : 시작값, limit : 가져올 값의 갯수
    data = request_json(url)

    if data is None:
        return []                       # 빈 리턴값

    pokemon_list = data["results"]      # data 딕셔너리에서 "results"키의 value(포케몬 이름, URL 딕셔너리 형식 저장)를 저장
    return pokemon_list

# ============================================================
# 3. 포켓몬 목록 일부 출력하기
# ============================================================
def print_pokemon_list(pokemon_list, count=10):    
    print()
    print("=" * 60)
    print("포켓몬 목록")
    print("=" * 60)

    for index, pokemon in enumerate(pokemon_list[:count], start=1):
        print(f"{index}. {pokemon['name']}")

    print("=" * 60)

# ============================================================
# requests 단계별 실행 함수
# ============================================================
def step_01_request_pokemon_list(limit=20):

    print()
    print("============================================================")
    print("requests로 포켓몬 목록 가져오기")
    print("============================================================")

    pokemon_list = get_pokemon_list(limit)
    print_pokemon_list(pokemon_list, count=limit)

    return pokemon_list

if __name__ == "__main__":
    step_01_request_pokemon_list(limit=20)

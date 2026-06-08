############################################################
# 1. [난이도: 하] requests 기본 사용 - 웹 페이지 HTML 가져오기
############################################################
def lesson_01_requests_basic():
    import requests     # 웹사이트나 API에 요청을 보내기 위한 외부 라이브러리
    import urllib3

    # verify=False를 사용할 때 출력되는 보안 경고 숨기기
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("1. [난이도: 하] requests 기본 사용 - 웹 페이지 HTML 가져오기")
    print("=" * 60)

    url = "https://www.naver.com"       # 접속 URL

    # requests.get(): 지정한 URL에 GET 요청 전송
    # verify=False : 학교 네트워크의 SSL 인증서 오류 회피
    response = requests.get(url, verify=False)
    
    # response.status_code : 200(정상), 404(페이지를 찾을 수 없음), 500(서버 내부 오류), 403(권한 없음)
    if response.status_code == 200:    
        print("요청 성공! 웹 페이지 내용을 가져왔습니다.")
        # response.text : 서버가 보내 준 HTML 문서 저장, 앞부분 1000자만 출력
        print(response.text[:1000])
    else:
        print(f"요청 실패! 상태 코드: {response.status_code}")

############################################################
# 2. [난이도: 하] httpbin GET 요청 및 JSON 형식 출력
############################################################
def lesson_02_httpbin_get():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("2. [난이도: 하] httpbin GET 요청 연습 - 요청 결과 확인")
    print("=" * 60)

    # httpbin.org : requests 연습용으로 만든 사이트
    # 연습 예시: GET, POST, 헤더 확인, 응답 코드 테스트
    # URL: https://httpbin.org
    response = requests.get("https://httpbin.org/get", verify=False)

    print(response.json())      # JSON 형태를 파이썬 자료형으로 변환해서 출력

############################################################
# 3. [난이도: 하] JSONPlaceholder 게시글 제목 5개 출력
############################################################
def lesson_03_json_posts():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("3. [난이도: 하] JSONPlaceholder 게시글 제목 5개 출력")
    print("=" * 60)

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",       # List 형식(배열)
        verify=False
    )
    
    posts = response.json()                 # JSON 데이터를 파이썬 자료형으로 변환 
    print("자료형 확인:", type(posts))      # <class 'list'>
    
    for post in posts[:5]:
        print(f"[{post['id']}] {post['title']}")

############################################################
# 4. [난이도: 하] 고양이 상식 API - JSON 딕셔너리 이해
############################################################
def lesson_04_cat_fact():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # SSL 인증서 검증 비활성 및 경고 숨김

    print()
    print("=" * 60)
    print("4. [난이도: 하] 고양이 상식 API - JSON 딕셔너리 이해")
    print("=" * 60)

    # catfact.ninja/fact는 고양이 상식 1개를 JSON 형식으로 보내 주는 공개 API.
    response = requests.get("https://catfact.ninja/fact", verify=False)

    # JSON 데이터를 파이썬 형식(딕셔너리)로 변환.
    cats = response.json()

    print(cats)
    print()
    print(f"{cats['fact']}\n{cats['length']}")
    print()

    # 딕셔너리를 for문으로 반복
    for cat in cats:
        print(f"{cat}: {cats[cat]}")

############################################################
# 5. [난이도: 중] 포켓몬 정보 찾아보기 - 입력값으로 API 검색
############################################################
def lesson_05_pokemon_info():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("5. [난이도: 중] 포켓몬 정보 찾아보기 - 입력값으로 API 검색")
    print("=" * 60)

    name = input("알고 싶은 포켓몬 이름을 입력하세요: ").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        print("이름:", data["name"])
        print("키:", data["height"])        # PokeAPI의 height는 데시미터(dm) 단위
        print("몸무게:", data["weight"])    # PokeAPI의 weight는 헥토그램(hg) 단위
    else:
        print("해당 포켓몬이 존재하지 않아요.")

############################################################
# 6. [난이도: 중] 이름으로 나이 예측 - query string 사용
############################################################
def lesson_06_agify_age():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("6. [난이도: 중] 이름으로 나이 예측 - query string 사용")
    print("=" * 60)

    name = input("이름을 입력하세요: ")
    url = f"https://api.agify.io/?name={name}"

    response = requests.get(url, verify=False)
    data = response.json()

    print(f"{data['name']}의 예상 나이는 {data['age']}세입니다.")

############################################################
# 7. [난이도: 중] 자신의 IP와 나라 및 도시 알아보기
############################################################
def lesson_07_ip_info():
    import requests
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("7. [난이도: 중] 자신의 IP와 나라 및 도시 알아보기")
    print("=" * 60)

    response = requests.get("https://ipinfo.io/json", verify=False)

    if response.status_code == 200:
        data = response.json()
        print(f"당신의 IP 주소: {data['ip']}")
        print(f"도시: {data['city']}")
        print(f"나라: {data['country']}")
    else:
        print("❌ 위치 정보를 가져오지 못했어요.")

############################################################
# 8. [난이도: 중] Books to Scrape 책 제목 추출 - HTML 스크래핑 입문
############################################################
def lesson_08_books_to_scrape():
    import requests
    from bs4 import BeautifulSoup       # HTML을 분석해서 태그를 쉽게 찾아주는 도구

    print()
    print("=" * 60)
    print("8. [난이도: 중] Books to Scrape 책 제목 추출 - HTML 스크래핑 입문")
    print("=" * 60)

    # 설명: 책 가격, 평점, 이미지 등 스크래핑 연습을 위해 만든 사이트
    url = "http://books.toscrape.com/"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")   # 가져온 HTML 문서를 BeautifulSoup으로 분석할 수 있게 변형
                                                    # "html.parser" : HTML 분석기 사용
    
    titles = soup.select("h3 a")        # 책 제목이 들어 있는 태그 추출. <h3> 태그 안에 있는 <a> 태그 찾아서 리스트로 저장
        # titles는 BeautifulSoup의 태그 객체
        # titles = [
        #   <a href="..." title="A Light in the Attic">A Light in the ...</a>,
        #   <a href="..." title="Tipping the Velvet">Tipping the Velvet</a>,
        #   <a href="..." title="Soumission">Soumission</a>
        #   ...
        # ]

    print(titles)
    for t in titles:            # t는 <a> 태그 자체
        print(t["title"])       # <a> 태그 안의 "title" 속성 값을 꺼내기

############################################################
# 9. [난이도: 중] Books to Scrape 책 제목과 가격 추출
############################################################
def lesson_09_books_title_price():
    import requests
    from bs4 import BeautifulSoup

    print()
    print("=" * 60)
    print("9. [난이도: 중] Books to Scrape 책 제목과 가격 추출")
    print("=" * 60)

    url = "http://books.toscrape.com/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")  # article.product_pod는 책 한 권의 정보를 담고 있는 영역.
                                                    # <article> 태그 중 class가 product_pod인 태그를 찾음
                # books = [
                #     <article class="product_pod">
                #         <h3>
                #             <a href="..." title="A Light in the Attic">A Light in the ...</a>
                #         </h3>
                #         <p class="price_color">£51.77</p>
                #     </article>,
                #     <article class="product_pod">
                #         <h3>
                #             <a href="..." title="Tipping the Velvet">Tipping the Velvet</a>
                #         </h3>
                #         <p class="price_color">£53.74</p>
                #     </article>,
                # ]

        for i, book in enumerate(books, start=1):
            title = book.select_one("h3 a")["title"]        # 책 제목은 h3 안의 a 태그 title 속성 1개만을 찾음
            price = book.select_one("p.price_color").get_text().strip() # 책 가격은 p.price_color 태그 안
        
            print(f"{i}. {title} - {price}")
    else:
        print("요청 실패!")
        print("상태 코드:", response.status_code)
        
############################################################
# 10. [난이도: 상] MovieChart 영화 순위 추출
############################################################
def lesson_10_moviechart_ranking():
    import requests                     # 웹페이지 가져오는 도구
    import urllib3                      # 보안 경고 메세지 숨기는 기능이 포함된 도구
    from bs4 import BeautifulSoup       # HTML 분석 도구

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("10. [난이도: 상] MovieChart 영화 순위 추출")
    print("=" * 60)
    ############################################################
    # 1. 기본 설정

    url = "https://m.moviechart.co.kr/info/current"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        ############################################################
        # 2. 전체 텍스트에서 영화 제목 추출하기

        movie_title_tags = soup.select("h3 a")      # 영화 제목은 <h3> 태그 안의 <a> 태그
            # movie_title_tags = [
            #     <a href="...">영화 제목 1</a>,
            #     <a href="...">영화 제목 2</a>,
            #     <a href="...">영화 제목 3</a>
            # ]

        movie_titles = []                       # 영화 제목 리스트

        for tag in movie_title_tags:
            title = tag.get_text().strip()      # 태그 안의 글자만 꺼내고 앞뒤 공백 제거
            
            if title == "":                     # 빈 문자열 제외
                continue
            if title == "Image":                # Image 같은 불필요한 텍스트는 제외.
                continue
            if title not in movie_titles:       # 중복 값이 없을 경우에만 추가
                movie_titles.append(title)

        ############################################################
        # 3. 전체 텍스트에서 관객 수와 개봉일 후보 추출하기

        text = soup.get_text(separator="\n")        # 글자만 가져옴(태그 제외), 글자를 줄바꿈으로 구분
        print(text)
        lines = []

        for line in text.split("\n"):               # 줄바꿈을 기준으로 잘라서 line 저장
            line = line.strip()

            if line != "":                          # 공백이 아니면 추가
                lines.append(line)
                    # lines = [
                    #     "범죄도시4",
                    #     "개봉일 2024.04.24",
                    #     "11,500,000 명",
                    #     "파묘",
                    #     "개봉일 2024.02.22",
                    #     "11,900,000 명"
                    # ]                

        audience_list = []                          # 관객 수 리스트
        open_date_list = []                         # 개봉일 리스트

        for line in lines:
            if line.endswith("명"):                 # 마지막 글자가 '명'이면
                audience_list.append(line)          # 관객 수 리스트에 추가
            if line.startswith("개봉일"):           # '개봉일'로 시작하면
                open_date_list.append(line)         # 개봉일 리스트에 추가

        ############################################################
        # 4. 결과 출력하기

        print("--- 영화 순위 ---")

        if movie_titles:                            # 영화 제목이 1개라도 있으면
            for i, title in enumerate(movie_titles, start=1):
                # 관객 수와 개봉일은 제목 순서와 같은 순서로 들어온다고 보고 매칭.

                audience = ""
                if i - 1 < len(audience_list):
                    audience = audience_list[i - 1]

                open_date = ""
                if i - 1 < len(open_date_list):
                    open_date = open_date_list[i - 1]

                print(f"{i}위: {title}")
                if audience != "":
                    print(f"   누적 관객 수: {audience}")
                if open_date != "":
                    print(f"   {open_date}")

                print()                             # 빈 줄 출력

        else:
            print("영화 제목을 찾지 못했습니다.")
            print("디버깅용으로 h3 a 태그 내용을 출력합니다.")
            print("-" * 60)

            for tag in movie_title_tags:
                print(tag.get_text().strip())

            print("-" * 60)

    else:
        print("요청 실패!")
        print("상태 코드:", response.status_code)

############################################################
# 11. [난이도: 상] 하키팀 시즌별 통계 데이터 승률 순위 만들기
############################################################

def lesson_11_hockey_team_stats_ranking():
    """
    - 여러 페이지에 나뉜 하키팀 시즌별 통계 데이터를 가져온다.
    - HTML 표에서 팀명, 연도, 승, 패, 승률을 추출한다.
    - 승률(pct)을 기준으로 내림차순 정렬하여 순위를 새로 계산한다.

    정렬 기준:
    1. 승률 pct가 높은 순서
    2. 승률이 같으면 승 wins가 많은 순서
    3. 그래도 같으면 패 losses가 적은 순서

    """

    import requests
    import urllib3
    from bs4 import BeautifulSoup

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print()
    print("=" * 60)
    print("11. [난이도: 상] 하키팀 시즌별 통계 데이터 승률 순위 만들기")
    print("=" * 60)

    ############################################################
    # 1. 기본 설정
    base_url = "https://www.scrapethissite.com/pages/forms/"    # 하키팀 시즌별 통계 데이터 사이트
    max_page = 3                        # 앞의 3페이지만 가져옴
    all_records = []                    # 여러 페이지에서 수집한 기록을 저장할 리스트
        # 예시
        # all_records = [
        #     {"team": "Boston Bruins", "year": "1990", "wins": 44, "losses": 24, "pct": 0.55},
        #     {"team": "Buffalo Sabres", "year": "1990", "wins": 31, "losses": 30, "pct": 0.388},
        #     {"team": "Calgary Flames", "year": "1990", "wins": 46, "losses": 26, "pct": 0.575}
        # ]        

    ############################################################
    # 2. 여러 페이지 반복 요청하기
    for page_num in range(1, max_page + 1):
        print(f"{page_num}페이지 데이터를 가져오는 중...")

        # page_num은 몇 번째 페이지를 가져올지 정하는 요청 조건
        # 실제 주소 예:
        # https://www.scrapethissite.com/pages/forms/?page_num=1
        params = {
            "page_num": page_num
        }

        response = requests.get(
            base_url,
            params=params,
            verify=False
        )

        if response.status_code != 200:
            print(f"{page_num}페이지 요청 실패! 상태 코드:", response.status_code)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.select("tr.team")           # <tr>태그의 class 명 'team' : 하키팀 한 시즌 기록이 들어 있는 행
            # rows = [
            #     <tr class="team">
            #         <td class="name">Boston Bruins</td>
            #         <td class="year">1990</td>
            #         <td class="wins">44</td>
            #         <td class="losses">24</td>
            #         <td class="pct">0.550</td>
            #     </tr>,
            #     <tr class="team">
            #         <td class="name">Buffalo Sabres</td>
            #         <td class="year">1990</td>
            #         <td class="wins">31</td>
            #         <td class="losses">30</td>
            #         <td class="pct">0.388</td>
            #     </tr>
            # ]

        if not rows:
            print(f"{page_num}페이지에서 팀 데이터를 찾지 못했습니다.")
            continue

        ############################################################
        # 3. 한 페이지 안의 팀 데이터 추출하기

        for row in rows:
            name = row.select_one("td.name").get_text().strip()     # 팀명 추출
            year = row.select_one("td.year").get_text().strip()     # 시즌 연도 추출
            wins = row.select_one("td.wins").get_text().strip()     # 승수 추출
            losses = row.select_one("td.losses").get_text().strip() # 패수 추출
            pct = row.select_one("td.pct").get_text().strip()       # 승률 추출    

            ########################################################
            # 문자열 데이터를 숫자로 변환하기
            wins_number = int(wins)                                 # 정렬과 계산을 하려면 int 또는 float로 변환
            losses_number = int(losses)
            pct_number = float(pct)

            record = {                                              # 한 팀의 한 시즌 기록을 딕셔너리에 저장
                "team": name,
                "year": year,
                "wins": wins_number,
                "losses": losses_number,
                "pct": pct_number
            }

            all_records.append(record)                              # 딕셔너리를 리스트에 저장

    ############################################################
    # 4. 승률 기준으로 순위 계산하기
    
    ranked_records = sorted(            # 정렬 후(작은 값 우선), 새 리스트 생성
        all_records,
        key=lambda record: (            # key=lambda record: (...)는 정렬 기준, lambda는 이름 없는 간단한 함수
            -record["pct"],             # 승률이 높은 팀이 앞으로 오도록 음수로 변경
            -record["wins"],            # 승률이 같으면 승수가 많은 팀이 앞으로 오도록 변경(음수로 변경).
            record["losses"]            # 승률과 승수가 같으면 패수가 적은 팀이 앞으로 오도록 변경.
        )
    )

    ############################################################
    # 5. 결과 출력하기
    
    print()
    print("--- 승률 기준 하키팀 시즌별 통계 순위 ---")
    print("주의: 이 순위는 원본 페이지에 있는 순위가 아니라, 승률 기준으로 새로 계산한 순위입니다.")
    print()
    print(f"{'순위':<5} {'팀명':<25} {'연도':<8} {'승':>5} {'패':>5} {'승률':>8}")
    print("-" * 70)

    for rank, record in enumerate(ranked_records[:30], start=1):    # 앞에서부터 30개만 출력.
        print(
            f"{rank:<5} "
            f"{record['team']:<25} "
            f"{record['year']:<8} "
            f"{record['wins']:>5} "
            f"{record['losses']:>5} "
            f"{record['pct']:>8.3f}"
        )

    print("-" * 70)
    print("수집한 전체 기록 수:", len(all_records))
    print("정렬 기준: 승률 높은 순서 → 승수 많은 순서 → 패수 적은 순서")

############################################################
# 12. [난이도: 상] Quotes to Scrape 명언과 작가 추출
############################################################
def lesson_12_quotes_to_scrape():
    import requests
    from bs4 import BeautifulSoup

    print()
    print("=" * 60)
    print("12. [난이도: 상] Quotes to Scrape 명언과 작가 추출")
    print("=" * 60)

    url = "http://quotes.toscrape.com/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.select("div.quote")                               # div.quote는 명언 하나의 전체 영역
                                                                        #<div> 태그이면서 class가 quote인 태그
            # quotes = [
            #     <div class="quote">
            #         <span class="text">“The world as we have created it...”</span>
            #         <span>
            #             by <small class="author">Albert Einstein</small>
            #         </span>
            #     </div>,

            #     <div class="quote">
            #         <span class="text">“It is our choices...”</span>
            #         <span>
            #             by <small class="author">J.K. Rowling</small>
            #         </span>
            #     </div>
            # ]                                                                        

        for i, quote in enumerate(quotes, start=1):

            text = quote.select_one("span.text").get_text().strip()         # 명언 문장은 span.text 안
            author = quote.select_one("small.author").get_text().strip()    # 작가 이름은 small.author 안

            print(f"{i}. {text}")
            print(f"   - {author}")
            print()
    else:
        print("요청 실패!")
        print("상태 코드:", response.status_code)

############################################################
# main 함수: 모든 섹터를 한 곳에서 관리
############################################################
def main():
    while True:
        print()
        print("=" * 60)
        print("requests / BeautifulSoup / JSON API 실습 메뉴")
        print("=" * 60)
        print("1. [하] requests 기본 사용 - 웹 페이지 HTML 가져오기")
        print("2. [하] httpbin GET 요청 연습 - 요청 결과 확인")
        print("3. [하] JSONPlaceholder 게시글 제목 5개 출력")
        print("4. [하] 고양이 상식 API - JSON 딕셔너리 이해")
        print("5. [중] 포켓몬 정보 찾아보기 - 입력값으로 API 검색")
        print("6. [중] 이름으로 나이 예측 - query string 사용")
        print("7. [중] 자신의 IP와 나라 및 도시 알아보기")
        print("8. [중] Books to Scrape 책 제목 추출 - HTML 스크래핑 입문")
        print("9. [중] Books to Scrape 책 제목과 가격 추출")
        print("10. [상] MovieChart 영화 순위 추출")
        print("11. [상] 하키팀 시즌별 통계 승률 순위 만들기")
        print("12. [상] Quotes to Scrape 명언과 작가 추출")
        print("0. 종료")
        print("=" * 60)

        choice = input("실행할 섹터 번호를 입력하세요: ").strip()
        if choice == "1":
            lesson_01_requests_basic()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "2":
            lesson_02_httpbin_get()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "3":
            lesson_03_json_posts()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "4":
            lesson_04_cat_fact()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "5":
            lesson_05_pokemon_info()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "6":
            lesson_06_agify_age()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "7":
            lesson_07_ip_info()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "8":
            lesson_08_books_to_scrape()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "9":
            lesson_09_books_title_price()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "10":
            lesson_10_moviechart_ranking()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "11":
            lesson_11_hockey_team_stats_ranking()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "12":
            lesson_12_quotes_to_scrape()
            input("\n계속하려면 Enter 키를 누르세요...")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 0부터 12 사이의 번호를 입력하세요.")
            input("\n계속하려면 Enter 키를 누르세요...")

if __name__ == "__main__":
    main()
import requests
import os

def req2dataframe():
    _, data = req() # 생략할 때 사용
    l = data.get('boxOfficeResult').get('dailyBoxOfficeList') 
    #l = data['BoxOfficeResult']['dailyBoxOfficeList']
    for i in l:
        print("\n")
        for j in i:
            print(f"{j} : {i[j]}")
    return l

def req(a='20230101'):
    url = gen_url(a)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    #print("##########################################################")
    #print(data)
    #print("##########################################################")
    #print(type(req2dataframe()))
    return code, data

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

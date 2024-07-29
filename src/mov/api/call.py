import requests
import os
import pandas as pd

def list2df():
    l = req2list()
    df = pd.DataFrame(l)
    #print(df)
    return df

def req2list() -> list:
    _, data = req() # 생략할 때 사용
    l = data.get('boxOfficeResult').get('dailyBoxOfficeList') 
    #l = data['BoxOfficeResult']['dailyBoxOfficeList']
    #for i in l:
    #    print("\n")
    #    for j in i:
    #        print(f"{j} : {i[j]}")
    return l

def get_key():
    #"""영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(a='20230101'):
    url = gen_url(a)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    #print("##########################################################")
    #print(data)
    #print("##########################################################")
    #print(type(req2dataframe()))
    print(data)
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

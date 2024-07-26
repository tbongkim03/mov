import requests

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "27868e75909908b7ea9b1918770d4541"
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

def req():
    print("req")

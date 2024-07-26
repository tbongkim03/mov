from mov.api.call import gen_url

def test_gen_url():
    url = gen_url()

    assert url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f3e6e155cfbe1f23ab59dce46ce6818b&targetDt=20120101"
    assert True
    assert "http" in url

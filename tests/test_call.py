from mov.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd
def test_비밀키숨기기():
    key = get_key()
    #print('1')
    assert "key"

def test_유알엘테스트():
    url = gen_url()
    #print('2')
    #assert "http" in url
    url = gen_url('20241231')
    print(url)
    assert '20241231' in url

def test_req():
    code, data = req()
    #print('3')
    assert code == 200

    code, data = req('20230101')
    assert code == 200

def test_r2d():
    l = req2list() 
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'
    #assert False
    #print('4')

def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns
    #print('5')

def test_save2df():
    df = save2df(load_dt='20241231')
    print("\n")
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns 

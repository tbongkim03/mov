# mov

### install
```bash
# main
$ pip install git+https://github.com/tbongkim03/mov.git
```


### start dev
```bash
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install

$ pytest

$ # option
$ pdm venv create
```

### setting env
``bash
cat ~/.zshrc | tail -n 3

# MYENV
export MOVIE_API_KEY="<key>"
```

### 트러블 슈팅
- [ ] 영화진흥위원회 가입 및 키생성
```bash
{'faultInfo': {'message': '유효하지않은 키값입니다.', 'errorCode': '320010'}}
```

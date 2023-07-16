# IT 뉴스 봇
RSS 피드를 통해 IT 관련 뉴스를 제공하는 봇 애플리케이션입니다.

IT 뉴스 봇은 [@it_newsbot@silicon.moe](https://social.silicon.moe/@it_newsbot)로 서비스 중입니다.

## 설치 방법
1. (권장) venv를 준비합니다.
2. 필요한 디펜던시를 설치합니다. (예 : pip3 install -r requirements.txt)
3. config.json을 열어 필요한 항목들을 채워 넣습니다.
4. crontab에 run.py를 등록합니다. 보통 1시간 간격(0 * * * *)이면 충분합니다.

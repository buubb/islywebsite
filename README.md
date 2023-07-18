# github 협업 전 필수 setting

1. 지금의 프로젝트를 fork 해주세요.
2. 티켓을 구분할 수 있도록 이슈를 등록해주세요.
3. fork 받은 프로젝트를 clone 후 작업 브랜치를 만들어주세요.
4. PR을 만들어주세요.

# 기능 추가 시 참고사항

1. 가상환경에 'python manage.py startapp 기능이름(ex. login, assignments)' 명령어로 기능 추가
2. 'islyweb/settings.py'의 INSTALLED_APPS에 기능 이름 추가
3. 디렉토리 '기능이름/'에 url.py 파일 추가 및 내용 작성
4. 경로 templates/기능이름/index.html 작성
5. 기능이름/views.py 내용 작성
6. islyweb/urls.py에 기능이름 경로 추가하여 url 연결
7. 서버 돌려서 잘 작동하는지 확인해보기

# 주의 사항

- 작업 브랜치 규칙:'issueid'-브랜치 이름 (e.x, '3-added-buubb', 비고.buubb는 제 githubID입니다.)
- 순번과 Github ID는 입력이 필수입니다.
- PR 제출 후 리뷰가 진행이 돼요. merge 되기 전에 수정과 rebase가 필요하실 수 있어요.

# Who Am I

| 순번 | Github ID | 
| ---- | --------- |
| - | - |

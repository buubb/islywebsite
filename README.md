# Install 필수
- pip install djangorestframework
- pip install summernote
- pip install mysqlclient
- User 테이블 사용은 https://han-py.tistory.com/353 참고
- pip install django-extensions
- pip install django-admin-thumbnails //일반
- pip install ‘django-admin-thumbnails<0.3’ //파이참 이용자
- python -m pip install Pillow //일반
- python -m pip install ‘Pillow<10’ //파이참 이용자# git 사용 방법
- pip install bandit // 보안 취약점 점검 툴
- pip install cmarkgfm
# commit 할 때
- 작업 브랜치 규칙:[이름] 수정 사항 (e.x, '[yubin] main 툴바 수정')

# push하고 싶을 때
- git add .
- git status
- git pull origin master > 솔직히 pull은 push 하기 전에만 하면 상관없음.
- git commit -m "수정사항"
- git push origin master

# I.Sly() URL 
- 메인 페이지: /
- 공지사항: /notice
- 과제 목록
    심화: /assignments/advanced
    기초: /assignments/basic
- 과제 제출: /assignments/submit
- 자료실: /library
- 팀 활동 게시물: /team-activities
- 재능 기부: /volunteer
- CTF 문제 모음: /CTF-Challenge
- 동아리 지원: /recruit
- 로그인: /login
- 아이슬리 소개: /introduction

# 기능 추가 시 참고사항
1. 가상환경에 'python manage.py startapp 기능이름(ex. login, assignments)' 명령어로 기능 추가
2. 'islyweb/settings.py'의 INSTALLED_APPS에 기능 이름 추가
3. 디렉토리 '기능이름/'에 url.py 파일 추가 및 내용 작성
4. 경로 templates/기능이름/index.html 작성
5. 기능이름/views.py 내용 작성
6. islyweb/urls.py에 기능이름 경로 추가하여 url 연결
7. 서버 돌려서 잘 작동하는지 확인해보기
<<<<<<< HEAD

# 주의 사항

- 작업 브랜치 규칙:'issueid'-브랜치 이름 (e.x, '3-added-buubb', 비고.buubb는 제 githubID입니다.)
- 순번과 Github ID는 입력이 필수입니다.
- PR 제출 후 리뷰가 진행이 돼요. merge 되기 전에 수정과 rebase가 필요하실 수 있어요.  

# Who Am I

| 순번 | Github ID | 
| ---- | --------- |
| - | - |

# Requirement
- pip install djangorestframework
- pip install summernote
- pip install mysqlclient
- User 테이블 사용은 https://han-py.tistory.com/353 참고
- pip install django-extensions
- pip install django-admin-thumbnails //일반
- pip install ‘django-admin-thumbnails<0.3’ //파이참 이용자
- python -m pip install Pillow //일반
- python -m pip install ‘Pillow<10’ //파이참 이용자
- pip install django-session-timeout // 세션 설정에 필요한 패키지
- pip install django-brutebuster // 관리자가 차단된 계정을 수동으로 해제할 수 있음
=======
>>>>>>> 463fbe33090c39f1a6da22e6a8f4a963ccd39b86

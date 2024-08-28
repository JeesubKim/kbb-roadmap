# kbb-roadmap
kbb-roadmap website

## Objective?
심심풀이 땅콩 오징어 프로젝트

장고를 쓸 일이 있어서 `심심풀이 프로젝트`도 하나 파서 해보는 중

심심풀이지만 체계적인 `KBB` 로드맵 관리가 절실함

그래서 시작함

솔까 ORM 쿼리가 엉망임, 그래도 뭐 `이 정도` 후로젝또에서는 노상관

`플렉스박스`는 반의반의반의반의반x100 장인이라.. 레이아웃은 `전부 다 Grid로` 조져 볼려고 했으나, 배운게 도둑질이라고 `flex` 없이 하기 힘든걸 깨닫고 섞어 씀

## Requirement

# FE
모든 Layout은 Mobile-first


# BE

# Roadmap

사용자는 신규 로드맵을 작성 하고 사용자를 할당 할 수 있다

## 로드맵 조회
1. 모든 사용자는 로드맵 페이지에 들어가면 모든 로드맵 상태를 조회 할 수 있다. [Done]
2. 모든 로드맵은 날짜순, open > 종료 로 정렬 되어야 한다 [Done]
3. Header에 신규 생성페이지로 가는 메뉴가 나타나야 한다 [Done]
4. 로드맵은 클릭시 댓글 작성 가능, 별도 페이지로 표시해야한다 [Done]
5. 로드맵 승인은 로드맵 Detail 페이지에서 나타나야 하고 여기서 액션을 취할 수 있어야 한다 (승인, 승인 철회, 승인한사람의 리스트가 나타난다) [Done]

## 로드맵 신규 생성
1. header에 뒤로가기 메뉴가 나타나야 한다 [Done]
2. 로드맵 제목을 적을 수 있는 input 이 나타나야 한다 [Done]
3. Assignee 칸에서는 가입자를 조회 할 수 있어야 한다 [Done]
4. 저장 버튼을 누르면 저장이 되어야 한다 [Done]


## 로드맵 생성 규칙
* 로드맵 Status 흐름: # Pending > In Progress > In Review > Done

1. 로드맵 제목 중복 체크 [Done]
2. 그리고 유사도를 검사해서 60% 이상 일치할 경우 비슷한 로드맵이 존재하는데 혹시 이미 등록된것과 같은지 나타내주어야 한다 (모달) [Backlog]

2. 로드맵이 생성 요청 > Status는 Pending > 가입자 모두에게 Notification 생성 (동의 페이지 링크) [Done] 
3. 과반 승인 시 In Progress 변경 [Done]

## 로드맵 종료
1. 로드맵 페이지에 완료 버튼을 클릭 시 증빙서류(사진)을 제시해야 함. [Backlog]
2. Status 는 In Review 으로 변경 [Done]
3. 가입자 모두에게 Notification 생성 (동의 페이지 링크 또는 Modal이 나타나야 함)  [Done]
4. 과반 승인시 Done 로 변경 [Done]



# Report

## Report 조회
1. 제보 페이지에서는 모든 제보항목이 Grid layout로 나타나야 함
2. Header에는 "신규" 항목이 나타나야함 [Done]
3. Report는 클릭시 댓글 작성 가능 [Done]

## Report 신규 생성
1. 제목, 내용, 이미지를 입력해야 함 [Done]
2. 제보 생성 시 제보 조회 화면으로 돌아가야 함 [Done]


# Notification

## Notification 조회

1. 해당 User의 모든 Notification 이 조회가 되어야함 [Done]
2. Notification 클릭시 해당 화면으로 이동 [Done]
3. Notification status 의 is_read가 True로 변경 되어야 함 [Done]
4. Notification status 의 is_read에 따라서 별도 분류되어야 함 [Done]
5. Grey 처리되어야 함 



# User

## Account 정보
1. User는 Google account로 무조건 접속해야 하며 사진을 가져온다. [Done]
2. 계정 정보 및 로그인 시점을 보여준다 [Done]
3. 로그아웃 버튼을 제공한다 [Done]

## Account 생성
1. 무조건 Google OAuth2.0 을 사용해서만 접속 가능 [Done]




# How to get to the google oauth page directly
```
# settings.py
SOCIALACCOUNT_LOGIN_ON_GET = True
```

# How to allow others to access test server

```
python manage.py runserver 0.0.0.0:8000
```


# How to make it work when `/user/` is not accessible from mobile
```
#settings.py
SITE_ID = 1 # <-- Make sure SITE ID is set
INSTALLED_APPS = [
    'django.contrib.sites',
    ...
]
```

# How to reset DB

1. Clear all files except for `__init__.py` in migrations folders
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. Setup below
5. Make sure SITE_ID is properly set (This is going to be stored in `db.sqlite3`)

# Add Google in Social app in django admin

## Admin
Social applications > Add > 
Add `localhost:8000` in Chosen sites


## Google Cloud
https://console.cloud.google.com/apis/credentials
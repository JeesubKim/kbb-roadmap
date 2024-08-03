# kbb-roadmap
kbb-roadmap website

## Requirement

# Roadmap

사용자는 신규 로드맵을 작성 하고 사용자를 할당 할 수 있다

## 로드맵 조회
1. 모든 사용자는 로드맵 페이지에 들어가면 모든 로드맵 상태를 조회 할 수 있다.
2. 모든 로드맵은 날짜순, open > 종료 로 정렬 되어야 한다
3. Header에 신규 생성페이지로 가는 메뉴가 나타나야 한다
4. 로드맵은 클릭시 댓글과 1차 대댓글 까지 작성 가능

## 로드맵 신규 생성
1. header에 뒤로가기 메뉴가 나타나야 한다
2. 로드맵 제목을 적을 수 있는 input 이 나타나야 한다
3. Assignee 칸에서는 가입자를 조회 할 수 있어야 한다
4. 저장 버튼을 누르면 저장이 되어야 한다


## 로드맵 생성 규칙
1. 로드맵 제목이 중복되는지, 그리고 유사도를 검사해서 60% 이상 일치할 경우 비슷한 로드맵이 존재하는데 혹시 이미 등록된것과 같은지 나타내주어야 한다 (모달)

2. 로드맵이 생성 요청 > Status는 Pending > 가입자 모두에게 Notification 생성 (동의 페이지 링크 또는 Modal이 나타나야 함) > 과반 승인 시 Pending > Opened 변경

## 로드맵 종료
1. 로드맵 페이지에 완료 버튼을 클릭 시 증빙서류(사진)을 제시해야 함. Status 는 Reviewing 으로 변경
2. 가입자 모두에게 Notification 생성 (동의 페이지 링크 또는 Modal이 나타나야 함) > 과반 승인시 Completed 로 변경



# Report

## Report 조회
1. 제보 페이지에서는 모든 제보항목이 Grid layout로 나타나야 함
2. Header에는 "신규" 항목이 나타나야함
3. Report는 클릭시 댓글과 1차 대댓글 까지 작성 가능

## Report 신규 생성
1. 제목, 내용, 이미지를 입력해야 함
2. 제보 생성 시 제보 조회 화면으로 돌아가야 함



# Notification

## Notification 조회

1. 해당 User의 모든 Notification 이 조회가 되어야함
2. Notification status 의 is_read에 따라서 별도 분류되어야 하고 Grey 처리되어야 함
3. Notification 클릭시 해당 화면으로 이동 또는 Actionable step window 제공 (Modal)



# User

## Account 정보
1. User는 Google account로 무조건 접속해야 하며, 관리자에 의해 사진이 강제 할당 될 수 있다.
2. 계정 정보 및 로그인 시점을 보여준다
3. 로그아웃 버튼을 제공한다

## Account 생성
1. 무조건 Google OAuth2.0 을 사용해서만 접속 가능

# 프로젝트 소개

<img width="300" alt="스크린샷 2021-08-15 오후 10 03 39" src="https://user-images.githubusercontent.com/77820288/129480838-a4d81c48-eda9-4e13-be70-4235f5cae023.png">

<img width="300" alt="스크린샷 2021-08-15 오후 10 03 57" src="https://user-images.githubusercontent.com/77820288/129480865-1f673d1f-94dd-4e7c-a898-e3fcf2e6feb9.png">

<img width="300" alt="스크린샷 2021-08-15 오후 10 04 35" src="https://user-images.githubusercontent.com/77820288/129480870-7f4580de-1b32-456a-8aa8-903874c1d51e.png">

<img width="300" alt="스크린샷 2021-08-15 오후 10 13 34" src="https://user-images.githubusercontent.com/77820288/129480876-176a214f-1af5-4f44-9b8c-beca8c242824.png">


---

프로젝트 개요 : 스터디카페 예약 웹 사이트

프로젝트 기간 : 2021.07 ~ 2021.08

프로젝트 목표 : 

- Django를 이용해 CRUD 기능 구현하기
- 라이브러리를 사용하지 않고 최대한 구현해보기
- 모델링부터 로직 구현까지 철저한 계획과 검증으로 진행하기

# 적용 기술 및 구현 기능

---

### 적용 기술

- Front-End : JavaScript
- Back-End : Python, Django
- Comuunication Tool : Git, GitHub, Slack

### 구현 기능

- Member : 회원가입, 로그인 & 로그아웃, 회원관리(내역, 수정)
- Product : 카페 등록, 내역, 조회, 삭제, 수정
- Booking : 카페 예약, 내역, 정보
- Review : 리뷰 작성, 내역

### 구현 기능 상세

**메인페이지**

**로그인 & 회원가입**

1. 비즈니스 유저와 일반 유저 각각의 회원가입 & 로그인 기능 구현
2. 카카오, 구글 소셜 로그인 기능 구현 

**마이페이지**

1. 일반 유저 : 예약 내역 확인 가능, 북마크 카페 확인 가능, 유저 정보 수정 및 비밀번호 변경 가능
2. 비즈니스 유저 : 카페 업로드 및 수정 / 삭제 가능, 유저 정보 수정 가능, 내 카페에 리뷰 확인 가능

**카페 상세 페이지**

1. 일반 유저가 해당 카페 예약 가능(날짜, 이용시간, 좌석 중복 처리 구현)
2. 해당 카페를 이용했던 유저만 리뷰 작성 가능
3. 해당 카페 북마크 가능
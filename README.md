# 프로젝트 소개
프로젝트 웹 사이트 : http://15.164.117.28
<img width="1395" alt="스크린샷 2021-08-17 오후 2 04 31" src="https://user-images.githubusercontent.com/77820288/129667335-44416785-d910-4d24-86e1-9c77e5507f24.png">


<img width="1008" alt="스크린샷 2021-08-15 오후 10 03 57" src="https://user-images.githubusercontent.com/77820288/129480865-1f673d1f-94dd-4e7c-a898-e3fcf2e6feb9.png">

<img width="1006" alt="스크린샷 2021-08-15 오후 10 04 35" src="https://user-images.githubusercontent.com/77820288/129480870-7f4580de-1b32-456a-8aa8-903874c1d51e.png">

<img width="510" alt="스크린샷 2021-08-17 오후 2 14 28" src="https://user-images.githubusercontent.com/77820288/129667449-18bbd8a4-7bad-41e7-98c9-d4f6b7a6cfd1.png">

<img width="739" alt="스크린샷 2021-08-17 오후 2 05 34" src="https://user-images.githubusercontent.com/77820288/129667475-461c3c70-378a-41b8-8c7e-331ceaddc254.png">

<img width="711" alt="스크린샷 2021-08-17 오후 2 05 41" src="https://user-images.githubusercontent.com/77820288/129667501-918e524f-143b-4ca1-a4b5-f45025eb9c43.png">

<img width="713" alt="스크린샷 2021-08-17 오후 2 05 48" src="https://user-images.githubusercontent.com/77820288/129667526-556037c8-3871-436d-b4e6-3505c6bcb0a4.png">

<img width="714" alt="스크린샷 2021-08-17 오후 2 05 55" src="https://user-images.githubusercontent.com/77820288/129667541-cc6a5caa-49ae-4342-8d42-e0221c0ce99b.png">

<img width="465" alt="스크린샷 2021-08-17 오후 2 06 38" src="https://user-images.githubusercontent.com/77820288/129667574-1bd6ef21-9c2d-49e0-a6c6-a93341c30fe6.png">

<img width="762" alt="스크린샷 2021-08-17 오후 2 11 22" src="https://user-images.githubusercontent.com/77820288/129667662-24d443b9-31e6-438a-b885-4f776e20cec8.png">

<img width="503" alt="스크린샷 2021-08-17 오후 2 12 14" src="https://user-images.githubusercontent.com/77820288/129667697-3e4e0956-41c6-4d42-81f3-ce6653386c5e.png">

<img width="756" alt="스크린샷 2021-08-17 오후 2 11 36" src="https://user-images.githubusercontent.com/77820288/129667745-0f426a06-8943-4fc6-818c-11d45125d1b6.png">

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

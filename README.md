# backend

## Profile bar

### 로그인 후

#### Response

1. 프로필 썸네일 사진
1. 이름
1. my list

#### Request

1. 읽고 있는 책 list api
1. 읽고 싶은 책 list api
1. 읽은 책 list api

## Main Page

#### Profile bar

#### Response

1. 인기있는 책
1. 최근 사람들이 읽은 책

#### Request

1. search api
   - 장르나 평점 등으로 구분
   - 조건에 맞는 책 list 반환
   - 각 책에 대한 정보
     - 썸네일
     - 제목
     - 작가
     - 평점

## Rate or Review

#### Profile bar

#### Request

1. 책 서평을 등록 및 편집
   - 제목
   - 작가
   - 평점
   - 서평

## Login Page

#### Response

1. ID/PW가 있는지 확인

## SignUp Page

#### Response

1. 회원가입
   - ID 중복 확인
   - PW 유효성 검사

## Detail Page

#### Profile bar

#### Response

1. 책 세부사항
   - 책 썸네일 사진
   - 제목
   - 저자
   - 평점
   - 책 소개
   - (책 소개 밑에 있는 칸에 글자가 뭔지 잘 모르겠습니다 ㅜ)
   - 서평
   - Q&A

#### Request

1. my list의 어느 곳에 추가할지 결정(?)

## Add New

#### Profile bar

#### Request

1. 책 등록
   - 책 사진
   - 제목
   - 작가
   - 평점
   - 책 소개
   - (책 소개 밑에 있는 칸에 글자가 뭔지 잘 모르겠습니다 ㅜ)

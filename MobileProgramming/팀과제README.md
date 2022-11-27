## Screen Saver

Nav activity에서 데이터를 불러오는 동안 보이는 Fragment
버튼 클릭 시 Main Fragment로 이동

## Main Fragment

1. 회원 정보(예: 떡볶이)
2. 챌린지 현황(예: 진행 0, 완료 3, 개설 0)
3. 캘린더뷰 - MaterialCalendarView 라이브러리 사용
    1. 챌린지 인증한 날짜에 점 표시 - MainFragment.kt

## Certification Fragment - 인증 센터

패키지 certicenter

### List View - 현재 내가 참여중인 챌린지 목록

현재 사용자가 참여중인 챌린지 클래스(Challenge.kt) 및 adapter

## Record Fragment - 기록 센터

패키지 recordcenter

### Grid View - 내가 참여중인 챌린지 인증 사진 모음

현재 사용자가 참여중인 챌린지 인증 사진 클래스(Record.kt) 및 adapter

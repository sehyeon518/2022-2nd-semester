## Screen Saver

Nav activity에서 데이터를 불러오는 동안 보이는 Fragment\
화면 클릭 시 Main Fragment로 이동

<img src="https://user-images.githubusercontent.com/84698896/205427299-8506577b-ea67-4f45-9124-51542d80e701.png" width="200"/>

## Main Fragment

ScrollView를 사용한 Layout

Navgation bar의 MainPage 메뉴 또는 상단 TTC 로고 클릭 시 보이는 Fragment

<img src="https://user-images.githubusercontent.com/84698896/205427501-244e8017-3806-4081-ab21-7b8889f7e187.png" width="200">
<img src="https://user-images.githubusercontent.com/84698896/205428115-f9bf7b13-f1d2-487a-afce-08c62c81f25b.png" width="200">

### 1. 회원 정보 (예: 떡볶이)

사용자 프로필: 기본 이미지로 설정\
사용자 이름: UserProfile 객체의 name

    showMyName()


### 2. 챌린지 현황 (예: 진행 2, 완료 3, 개설 2)

    showCount()

`userChallenge/getRef?idUser=" + 사용자 번호`를 통한 json object

각 text view 클릭 시 진행 중인 챌린지, 완료한 챌린지, 개설한 챌린지 목록을 보여주는 fragment로 이동

### 3. 챌린지 인증센터 이동

`챌린지 인증하러 가기` 또는 Navigation bar의 Certification 메뉴 클릭 시 Certification Fragment로 이동

### 4. 캘린더뷰 - MaterialCalendarView 라이브러리 사용

    showDate()
    
`https://github.com/prolificinteractive/material-calendarview`

챌린지 인증한 날짜에 점 표시\
MainFragment.kt 내 `var calendarView:MaterialCalendarView 객체`
MaterialCalendar 라이브러리 커스텀 함수 overriding\
챌린지 인증 날짜를 CalendarDay 타입으로 받아 지정된 색의 점을 표시함 (예: 11월 22일, 23일, 27일 인증)

<img src="https://user-images.githubusercontent.com/84698896/205427917-87a81865-12cf-421e-b8c0-01884a193506.png" width="200">

```kotlin
calendarView?.addDecorator(EventDecorator(Color.parseColor("#645EFF"), 
                        Collections.singleton(CalendarDay.from(yyyy, mm-1, dd))))
```

```kotlin
class EventDecorator(private val color: Int, dates: Collection<CalendarDay>?) : DayViewDecorator { 
    private val dates: HashSet<CalendarDay> 

      override fun shouldDecorate(day: CalendarDay): Boolean { 
        return dates.contains(day) 
      } 
    override fun decorate(view: DayViewFacade) { 
        view.addSpan(DotSpan(9F, color)) 
    } 
    init{ 
        this.dates = HashSet(dates) 
    } 
}
```

### 5. 사용자 관리

각 뷰 클릭 시 해당 유저 관리 페이지로 이동


## Certification Fragment - 인증 센터

현재 참여중인 챌린지 목록을 List View로 불러오는 Fragment

<img src="https://user-images.githubusercontent.com/84698896/205429002-9a25258b-e2a9-4a84-b2be-71c22059472c.png" width="200">

각 챌린지마다 챌린지 대표 사진, 챌린지 이름, 챌린지 만든이, 인증하기 버튼, 갤러리 버튼으로 구성되어 있음

### 1. 인증하기

### 2. 갤러리

갤러리 버튼 클릭 시 해당 챌린지 기록센터로 이동

뷰 모델(MyViewModel.kt)을 통해 해당하는 챌린지의 challenge name이 기록센터로 전달\
뷰 모델은 MutableLiveData를 이용하여 sendMessage와 getMessage 메소드를 통해챌린지의 이름을 주고 받을 수 있음

```kotlin
val message = MutableLiveData<String>()
fun sendMessage(text: String) {
    message.value = text
}
fun getMessage(): String? {
    return message.value
}
```

## Record Fragment - 기록 센터

해당하는 챌린지를 인증한 사진을 Grid View로 불러오는 Fragment

뷰 모델의 getMessage 메소드를 통해 챌린지의 이름을 받아 해당하는 챌린지를 인증한 기록을 불러옴

### Grid View - 내가 참여중인 챌린지 인증 사진 모음

현재 사용자가 참여중인 챌린지 인증 사진 클래스(Record.kt) 및 adapter

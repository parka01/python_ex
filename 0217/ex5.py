"""1페이지를 읽는 데 평균 3분의 시간이 걸린다면
총 120페이지의 책을 완독하는데 걸리는 시간은 얼마인지를 구하는
프로그램을 작성 하시오."""
TimePerPage=3
PagesOfBook=120
ReadingTimeForOneBook=TimePerPage*PagesOfBook
print(ReadingTimeForOneBook)
#----------------모범답안---------------------
avg_time=3 #1페이지 읽는 시간
total_page=120 #읽어야 하는 페이지
time=(avg_time*total_page)/60 #완독시간
print("완독하는데 걸리는 시간 %.f 시간"%time)
"""3분에 2100자를 입력할 수 있는 사람이 45분 동안 몇 자를 입력할 수 있는지를
 구하는 프로그램을 작성 하시오."""
typePerMinute=int(2100/3)
print('45분동안 입력 가능한 자수: ', typePerMinute*45)
#----------------모범답안---------------------
min3_per_word=2100 #3분동안 입력 가능한 글자수
min_per_word=min3_per_word/3 #1분동안 입력 가능한 글자수
min45_per_word=45*min_per_word
print("45분동안 %.0f자 입력 가능 "%min45_per_word)
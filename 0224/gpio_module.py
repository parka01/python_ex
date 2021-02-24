from gpiozero import LED #gpio모듈에서 LED불러오기
from time import sleep #time모듈에서 sleep함수를 불러오기

led=LED(4) #4는 LED의 핀 번호이다. 객체생성.LED수가 많으면 그 수만큼 객체생성을 해야한다.
while True:
    led.on()    #LED켜기 함수
    sleep(1)    #불을 켜고 1초 기다린다.
    led.off()   #LED끄기 함수
    sleep(1)    #불을 끄고 1초 기다린다.

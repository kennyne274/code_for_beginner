# 터틀로 원 그리기
# 먼저 터틀 모듈을 임포트 합니다
import turtle

# 터틀 객체를 형성하여 t 변수에 넣어줍니다. 이제부터 모든 터틀 명령어 앞에 t.가 붙을 거에요.
t = turtle.Turtle()
t.speed(5)  # 터틀의 속도
t.pensize(3) # 펜의 굵기
t.pencolor("green") # 펜의 색상

t.circle(100) # 반지름 100 픽셀의 원을 그립니다.

turtle.done() # 작업 완료

import turtle

# c = ["red", "green", "blue", "yellow"]
# print(len(c))
# m = 0
# r = 30


t = turtle.Turtle()


def myTurtleMake (tur, color, move, radius) :
    global m
    tur.color(color)
    tur.circle(int(radius))
    m = int(m) + 50
    t.goto(m, 0)
    return tur

c = input("색깔 : ")
m = input("이동거리 : ")
r = input("원의 반지름 : ")
t = turtle.Turtle()


myTurtleMake(t, c, m, r)  # 함수 호출
turtle.mainloop()  # turtle 객체 생성
turtle.bye()
# t.color("red")
# t.circle(50)
# t.goto(50, 0)
#
# t.color("green")
# t.circle(50)
# t.goto(100, 0)
# t.color("blue")
# t.circle(50)
# t.goto(150, 0)
# t.color("yellow")
# t.circle(50)
# t.goto(150, 0)



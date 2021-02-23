# 单选题 8

# 导入turtle（海龟）工具箱，为了在屏幕上绘图
from turtle import Turtle


def ZhengDuoBianXing(bianshu, t):
    for i in range(bianshu):
        t.forward(50)
        t.setheading(60)


t = Turtle()
# t.setx(0)
# t.sety(0)

ZhengDuoBianXing(7, t)

# t.setx(0)
# t.sety(-100)

done()

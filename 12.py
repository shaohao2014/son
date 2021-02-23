"""
第15题答案的python演示代码：
导入turtle模块
你只要知道turtle是python的一个图形界面库（工具箱），
方便你在电脑屏幕上生成一个图形化的程序界面。
"""

from turtle import Screen, Turtle

screen = Screen()
# screen.addshape("./t.gif")

t = Turtle()
# t.shape("./t.gif")


x, y = 0, 0
for i in range(4):
    for j in range(3):
        t = t.clone()
        y -= 100
        t.sety(y)
    x += 100
    y = 0
    t.setx(x)
    t.sety(y)

t.hideturtle()

screen.mainloop()

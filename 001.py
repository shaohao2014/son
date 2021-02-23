import threading
import turtle
import time


now = time.localtime()  # 返回服务器时间

print(now)
print(time.strftime("%Y-%m-%d %H:%M:%S", now))

# 绘制单根数码管


def drawLine(draw):
    turtle.pensize(3)
    turtle.pu
    turtle.fd(3)
    if draw:
        turtle.pd()
    else:
        turtle.pu()

    turtle.fd(24)
    turtle.pu()
    turtle.fd(3)
    turtle.right(90)


# 根据数字绘制数码管
def drawNum(num, color):
    turtle.colormode(255)
    turtle.color(eval(color))
    # 第一条线
    if num in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 3, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.left(90)

    if num in [0, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.pu()
    turtle.left(180)
    turtle.fd(30)  # 绘制后面数字间隔位置
    turtle.update()


def Tick():
    now = time.localtime()
    now_time.n_sec = now.tm_sec
    turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    turtle.fd(-300)

    darwDate(str(now.tm_year), '(255, 69, 0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('年', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    darwDate(str(now.tm_mon), '(0,139,0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('月', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    darwDate(str(now.tm_mday), '(0,0,139)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('日', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(-90)
    turtle.right(90)
    turtle.fd(-510)

    darwDate(str(now.tm_hour))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('时', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    darwDate(str(now.tm_min))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('分', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    darwDate(str(now.tm_sec))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('秒', align="center", font=("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(0.1, Tick)  # 利用多线程库定时刷新
    timer.start()


def main():
    turtle.hideturtle()  # 隐藏画笔
    turtle.speed(0)  # 最快
    turtle.tracer(0)
    turtle.pu()
    turtle.fd(-300)
    Tick()
    turtle.done()
# Python turtle模块的海龟作图，由于需要展示海龟运动的过程，缺省状态下，对作图进行了延迟处理，
# 致使复杂图形的绘制速度过慢，可以用如下方法取消延迟，加速绘图：
# 在绘图之前调用tracer
# turtle.tracer(0)
# 在绘图结束时调用update
# turtle.update()


main()

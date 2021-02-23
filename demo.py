
# import turtle

# screen = turtle.Screen()
# screen.addshape("./t.gif")
# turtle.shape("./t.gif")

# turtle.fd(190)
# turtle.right(90)
# turtle.fd(190)
# turtle.right(90)
# turtle.fd(190)
# turtle.mainloop()

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(260)
    left(169)
    if abs(pos()) < 1:
        break
end_fill()
done()

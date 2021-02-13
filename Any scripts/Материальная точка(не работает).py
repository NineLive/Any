"""
Моделирование материальной точки из соответствующего задания
http://cs.mipt.ru/python/lessons/lab3.html#id16
"""
import turtle as trt
from math import sin, cos, ceil as c
window = trt.Screen()
window.setup(1000,600)

tur = trt.Turtle()
tur.width(2)
tur.up()
tur.setposition(0,0)
tur.pd()
tur.shape('circle')
tur.speed(3)



def move():
    """
    x = tur.xcor() + v0 *0.1* cos(alpha) * t
    y = tur.ycor() + v0 * sin(alpha) * t - (g * t ** 2) / 2
    :return:
    """
    g = 9.8
    v0 = 25
    alpha = 67 * 3.14/180
    t = 0
    i = 0
    while i != 2:
        h_max = (v0**2 * sin(alpha)**2) / (2*g)
        print('h_max = ', h_max)

        while t != 22.5:
            t += 0.1
            x = tur.xcor() + v0*0.2 * cos(alpha) * t
            y = tur.ycor() + v0*0.8 * sin(alpha) * t - (g * t ** 2) / 2
            print('UP', x, y)
            tur.goto(x, y)
            tur.stamp()
            if tur.ycor() <= 0:
                break
        break

        print('x = ', c(tur.xcor()),'y = ',c(tur.ycor()))
        tur.goto(x, y)
        t += 0.5
        i += 1






move()

trt.mainloop()


"""
Второй вариант(не работает)

import turtle as trt

window = trt.Screen()
window.setup(1000,600)

tur = trt.Turtle()
tur.width(2)
tur.up()
tur.setposition(0,0)
tur.pd()
tur.shape('circle')
tur.speed(3)

Vx = 5
Vy = 5
ay = 2
dt = 0.1
x = tur.xcor()
def move():
    Vx = 10
    Vy = 2
    ay = 0.1
    dt = 0.1
    x = tur.xcor()
    y = tur.ycor()
    for dt in range(0,20,1):
        Vy +=ay*dt
        x += Vx*dt
        y += Vy*dt - ay*dt**2/2
        tur.goto(x,y)
        tur.stamp()

move()
trt.mainloop()
"""
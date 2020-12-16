from vpython import *
g=9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
C_drag = 0.9
scene = canvas(center = vec(0,5,0), width=600,align = 'left', background=vec(0,0.5,0.5))
floor = box(length=30, height=0.01, width=4, color=color.blue)
ball = sphere(radius = size, color=color.red, make_trail=True, trail_radius = size/3)
ball.pos = vec(-15, size, 0)
theta = pi/4
ball.v = vec(20*cos(theta), 20*sin(theta), 0)
drop = 0
a1 = arrow(color = color.yellow, shaftwidth = 0.05)
oscillation = graph(width = 450, align = 'right')
funct1 = gcurve(graph = oscillation, color=color.blue, width=4)

dis=0

hei = 0

t=0
dt = 0.001
while  drop < 3:
    rate(1000)
    ball.v += vec(0, -g, 0) * dt - C_drag*ball.v*dt
    ball.pos += ball.v*dt
    a1.pos = ball.pos
    a1.axis = ball.v
    t += dt
    
    funct1.plot( pos=(t, ball.v.mag) )
    dis += ball.v.mag * dt
    

    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y = - ball.v.y
        drop += 1

    if ball.pos.y > hei:
        hei = ball.pos.y
    
displacement = ball.pos.y + 15
msg1 = text(text = 'displacement = ' + str(displacement), pos = vec(-10, 15, 0))
msg2 = text(text = 'total distant = ' + str(dis), pos = vec(-10, 13, 0))
msg3 = text(text = 'largest height = ' + str(hei), pos = vec(-10, 11, 0))
print (displacement)
print (dis)
print (hei)

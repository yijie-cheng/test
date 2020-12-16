from vpython import *
import random
import math
g = 9.8 
size, m = 0.2, 1      
k = 150000
L = 2-m*g/k
N = random.randint(1,4)
scene = canvas(title='N='+str(N), width=500, height=500, center=vec(0, -1, 0), align = 'left', background=vec(0.4,0.6,0.7))
g1 = graph(title='Instant Energy', width = 450, align = 'left', xtitle='t(s)', ytitle='E(J)')
funct1 = gcurve(graph = g1, color=color.blue, width=4)
funct2 = gcurve(graph = g1, color=color.red, width=4)
g2 = graph(title='Average Energy', width = 450, align = 'right', xtitle='t(s)', ytitle='E(J)')
funct3 = gcurve(graph = g2, color=color.blue, width=4)
funct4 = gcurve(graph = g2, color=color.red, width=4)

totk = 0 #total kinetic energy
totu = 0 #total gravitational potential energy
    
balls =[]
for i in range(5):
    ball = sphere(pos = vec(-0.8+0.4*i, -L - m*g/k, 0), radius = size, color=color.white)
    ball.v = vec(0, 0, 0)
    balls.append(ball)
for i in range(N):
    balls[i].v = vec(-sqrt(0.98), 0, 0)
        
springs =[]
for i in range(5):
    spring = cylinder(pos = vec(-0.8+0.4*i, 0, 0), radius =0.03)
    springs.append(spring)

# raise balls
T = 0
dT=0.0001
while(balls[0].pos.y <= -L - m*g/k +0.05):
    rate(5000)
    T += dT
    for i in range(5):
        springs[i].axis = balls[i].pos-springs[i].pos
        spring_force = - k * (mag(springs[i].axis) - L) * springs[i].axis.norm()
        balls[i].a = vector(0, - g, 0) + spring_force / m 
        balls[i].v += balls[i].a*dT
        balls[i].pos += balls[i].v*dT
        
# start
dt = 0.0001
t = 0
while True:
    rate(5000)
    t += dt
    insk = 0
    insu = 0

    def af_col_v(m1, m2, v1, v2, x1, x2): # function after collision velocity
        v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
        v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
        return (v1_prime, v2_prime)
        
    for i in range(5):
        springs[i].axis = balls[i].pos-springs[i].pos
        spring_force = - k * (mag(springs[i].axis) - L) * springs[i].axis.norm()
        balls[i].a = vector(0, - g, 0) + spring_force / m 
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        if (i<4 and mag(balls[i].pos - balls[i+1].pos) <= 0.4 and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = af_col_v (1, 1, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
            
        insk += 0.5*m*pow(mag(balls[i].v),2) #instant kinetic energy
        insu += m*g*(balls[i].pos.y+L+m*g/k) #instant gravitational potential energy
        
    funct1.plot( pos=(t, insk) )
    funct2.plot( pos=(t, insu) )

    totk += insk*dt
    totu += insu*dt
    funct3.plot( pos=(t, totk/t) )
    funct4.plot( pos=(t, totu/t) )

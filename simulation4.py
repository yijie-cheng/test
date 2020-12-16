import numpy as np 
from vpython import * 
A, N, omega = 0.10, 50, 2*pi/1.0              
size, m, k, d = 0.06, 0.1, 10.0, 0.4               
#scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0,0.5,0.5), align = 'left', center = vec((N-1)*d/2, 0, 0))
oscillation = graph(width = 800)
#funct1 = gdots(graph = oscillation, color=color.orange, size=3)
funct2 = gcurve(graph = oscillation, color=color.red, size=3)
#balls = [sphere(radius=size, color=color.yellow, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)] 
#springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)]
n=1
for n in range(1,25):
    #c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
    t, dt = 0, 0.001
    Unit_K= 2 * pi/(N*d)
    Wavevector = n * Unit_K 
    phase = Wavevector * arange(N) * d 
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    cnt=0
    ptpos=0
    cupos=0
    while True: 
        rate(10000) 
        t += dt 
        #ball_pos[0] = A * sin(omega * t )
        for i in range(N):
            if i == N-1:
                spring_len[-1] = ball_pos[0]+20-ball_pos[-1]
            else:
                spring_len[i] = (ball_pos[i+1]-ball_pos[i])
                
        for i in range(N):
            if i == 0:
                ball_v[0] += k* (spring_len[0]-d)/m*dt - k* (spring_len[-1]-d)/m*dt
            elif i == N-1:
                ball_v[-1] += - k * (spring_len[-2]-d)/m*dt + k * (spring_len[-1]-d)/m*dt
            else:
                ball_v[i] += k* (spring_len[i]-d)/m*dt - k* (spring_len[i-1]-d)/m*dt 
        ball_pos +=  ball_v*dt
        '''
        for i in range(N): balls[i].pos.x = ball_pos[i]      
        for i in range(N-1):                                 
            springs[i].pos = balls[i].pos                    
            springs[i].axis = balls[i+1].pos - balls[i].pos 
        
        ball_disp = ball_pos - ball_orig 
        for i in range(N): 
            c.modify(i, y = ball_disp[i]*4+1)
        '''
        ptpos = cupos
        cupos = ball_pos[-1]
        if ptpos>=19.6 and cupos <=19.6 and cnt==0:
            t1=t
            cnt+=1
        elif ptpos>=19.6 and cupos <=19.6 and cnt==1:
            t2=t
            break
    w=2*pi/(t2-t1)
    #print("n = ",n , " ,w = : " , w)
    K = (2*pi*n)/(N*d)
    print("K = ",K , " ,w = : " , w)
    #funct1.plot( pos=(n, w))
    funct2.plot( pos=(K, w))

from updating import *
from paddle import *
from time import sleep
from colorama import Fore, Back, Style
import os 
from input import *
import time
from ball import *
from bricks import *
from powerups import *

ball = gameball()
timetrack = time.time()
var = 0 
flag = 0
paddle = paddl()
prnt=printboard()
flag1=0
flag2=0
getch = Get()

xvel=0
yvel=0
mballs = multiballs()
brick = brickarray()
lent = 2
cntr=var+2
xorg=0
yorg=0
# pwrup = managepowerup()
tdarr=[]
while(1):
    
    if time.time()-timetrack >= 0.09:
        timetrack = time.time()
        if flag == 0:
            flag=1
            prnt.getinitalscreen() 
            tdarr = prnt.copygrid()
            tdarr = brick.createarr(tdarr)
            # pwrup.reset()
            tdarr[34] = ball.initializeball()
            tdarr[35] = paddle.initializepaddle()
            
            mballs.reset()
            prnt.setupdategrid(tdarr)
            paddletime = time.time()
            prnt.initializetime() 
            
        else:
            tdarr = prnt.copygrid()
            tdarr=paddle.returnpaddle(tdarr)
            flag2 = 0
            c = input_to(getch)
            if c=='d':
                flag3 = 0
                if paddle.padlrightpos()==1:
                    tdarr,flag2 = paddle.callmoveright(tdarr)
                    if flag1==0:
                        flag3 = 1
                        tdarr[34]=ball.shiftballright()
                    prnt.setupdategrid(tdarr)
            elif c=='e':
                break

            
            elif c=='a':
                if paddle.padlleftpos()==1:
                    tdarr,flag2 = paddle.callmoveleft(tdarr)
                    flag3 = 0
                    if flag1==0:
                        #print(flag3)
                        flag3 = 1   
                        tdarr[34]=ball.shiftballleft()
                    prnt.setupdategrid(tdarr)
                    #print(flag3)
            elif c=='p':
                flag3 = 0
                if flag1==0:
                    #print(flag3)
                    flag1=1
                    cntr = paddle.getpadlcentr()
                    ball.fireball(cntr)
                    flag3 = 1
                    mballs.initializeinitalball(ball.xpos,ball.ypos,ball.xvel,ball.yvel)
                else:
                    flag3 = 0
                    paddle.paddledegrab()
                    mballs.setballarr(paddle.getactivatepaddlearr())
            elif c=='m':
                tdarr = brick.movebrickdown(tdarr,5,1)
            cntr = paddle.getpadlcentr()
            if flag1 !=0:
                scr = prnt.getscore()
                flag3 = 0
                brick,tdarr,scr = mballs.checkbrickcollision(brick,tdarr,scr)
                
                prnt.updatescore(scr)
                prnt.printball()

                tdarr,paddle,collidflag = mballs.updateallballpos(tdarr,cntr,paddle.getpadlresid(),paddle)
                xvel = ball.setvel()
                tdarr = brick.movebrickdown(tdarr,int(time.time()-paddletime),collidflag)
                flag2 = paddle.getactivategrabpaddle()
                
            xvel = ball.setvel()
            prnt.setupdategrid(tdarr)

            
            if mballs.removeballs()==0 and flag1!=0 and flag2==0:
                ball.restoreflag()
                flag3 = 0
                tdarr = []
                prnt.getlives()
                paddle.resetpadlpos()
                flag = 0
                flag1=0
                prnt.printball()

        os.system('clear')
        brick.changerainbowcolor()
        prnt.callprintscreen(brick.returnvis(),brick.retrunidval(),brick.getarray())
        
     






from bricks import *
from powerups import *
import random
class gameball:
    def __init__(self):
        self.xvel = 0
        self.yvel = 0
        self.xpos = random.randint(1,5)
        self.ypos = 34        
        self.resetflag = 0 
        self.flagpaddlegrab = 0
        self.__prevchar = ''
        self.flagandgrab = 0
        self.isthruball = 0
        self.__strin=""
        self.pushedflag = 0
        self.paddlecollidflag = 0
    def setpaddlecollidflag(self,val):
        self.paddlecollidflag = val
    def setvel(self):
        self.vel = 2
    def getpaddlecollidflag(self):
        return self.paddlecollidflag
    
    def __initialball(self):
        self.xpos = random.randint(1,5)
        self.ypos = 34
        self.__strin=""
        ball = "O"
        for i in range(150):
            if i==0 or i==149:
                self.__strin=self.__strin+"#"
            elif i==self.xpos:
                self.__strin=self.__strin+ ball
            else:
                self.__strin=self.__strin+" "
        return self.__strin
    
    def setxvel(self,x):
        self.xvel = x
    def fireball(self,cntr):
        return self.__releaseball(cntr)  
    def setyvel(self,y):
        self.yvel = y
        
    def __moveballright(self):
        self.__strin=""
        self.xpos=self.xpos+2  
        ball = "O"
        for i in range(150):
            if i==0 or i==149:
                self.__strin=self.__strin+"#"
            elif i==self.xpos:
                self.__strin=self.__strin+ball
            else:
                self.__strin=self.__strin+" "
        return self.__strin
    def __moveballleft(self):
        self.__strin=""
        self.xpos=self.xpos-2
        
        ball = "O"
        for i in range(150):
            if i==0 or i==149:
                self.__strin=self.__strin+"#"
            elif i==self.xpos:
                self.__strin=self.__strin+ball
            else:
                self.__strin=self.__strin+" "
        return self.__strin
    
    
    def initializeball(self):
        return self.__initialball()
    def __releaseball(self,cntr):
        self.yvel = -1
        if self.xpos > cntr:
            self.xvel=self.xvel+abs(self.xpos-cntr)
        else:
            self.xvel=self.xvel-abs(self.xpos-cntr)
    def updateveloc(self,x,y):
        self.xvel = x
        self.yvel = y
    def shiftballleft(self):
        return self.__moveballleft()
    
    
    def __checkreflection(self,xposnew,yposnew,cntr,resid):
        if xposnew <= 0:
            self.xvel *= -1
            xposnew = self.xpos + self.xvel
        elif xposnew >=148:
            self.xvel *= -1
            xposnew = self.xpos + self.xvel
        if yposnew <=0:
            self.yvel *= -1
            yposnew = self.ypos + self.yvel
        elif yposnew >34:
            varx = self.xpos+((35-self.ypos)/abs(self.yvel)*self.xvel)

            if varx<=cntr+resid and varx>=cntr-resid:
                if xposnew>cntr:
                    self.xvel=self.xvel+int(abs(varx-cntr))      
                    if self.xpos+self.xvel>=148:
                        self.xvel *= -1
                        xposnew = self.xpos + self.xvel
                elif xposnew<=cntr:
                    self.xvel=self.xvel-int(abs(cntr-varx))

                    if self.xpos+self.xvel <=0:
                        self.xvel *= -1
                        xposnew = self.xpos + self.xvel
                
                if self.getpaddlegrabflag()==1:
                        self.yvel = -1
                        self.setflagandgrab(1)   
                        return self.xpos,self.ypos
                self.yvel *= -1
                yposnew = self.ypos+self.yvel           
            elif varx>cntr+resid or varx<cntr-resid:
                self.xvel = 0
                self.resetflag=1   
                self.yvel = 0
        return xposnew,yposnew
    def restoreflag(self):
        self.resetflag = 0
    def shiftballright(self):
        return self.__moveballright()
    
    def __updateballpos(self,tdarr,cntr,resid):

        xposnew = self.xpos + self.xvel
        yposnew = self.ypos + self.yvel
        tempstr=""
        xposnew,yposnew = self.__checkreflection(xposnew,yposnew,cntr,resid)
        
        tempr=""
        ball = "O"
        for i in range(35):
            for j in range(150):
                if i == self.ypos: 
                    if j== self.xpos:
                        for k in range(150):
                            if tdarr[i][k]!=ball:
                                tempstr=tempstr+tdarr[i][k]
                            else:
                                tempstr=tempstr+" "
                        tdarr[i]=tempstr
        self.xpos = xposnew
        self.ypos = yposnew
        for i in range(150):
            if i<xposnew:
                tempr=tempr+tdarr[yposnew][i]
            elif i==xposnew:
                tempr=tempr+ball
            else:
                tempr=tempr+tdarr[yposnew][i]
        tdarr[yposnew]=tempr
        
        return tdarr
    def setxypos(self,x,y):
        self.xpos = x
        self.ypos = y
    def getxvel(self):
        return self.xvel
    def setballupdate(self,tdarr,cntr,resid):
        return self.__updateballpos(tdarr,cntr,resid)
    
    
    def setflagandgrab(self,val):
        self.flagandgrab=val
    
    def update(self,xpos,ypos,xvel,yvel):
        self.xvel = xvel
        self.yvel = yvel
        self.xpos = xpos
        self.ypos = ypos
    
    
    def increasespeed(self):
        if self.xvel<0:
            self.setxvel(self.xvel-1)
            
        elif self.getxvel>=0:
            self.setxvel(self.xvel+1)
    def checkflag(self):
        return self.resetflag
    def resetdefaultspeed(self):
        if self.xvel<0:
            self.setxvel(self.xvel+1)
            
        elif self.getxvel>=0:
            self.setxvel(self.xvel-1)
    def getpaddlegrabflag(self):
        return self.flagpaddlegrab

    
    def getyvel(self):
        return self.yvel
    
    def getflagandgrab(self):
        return self.flagandgrab
    
    
class multiballs:
    def __init__(self):
        self.flg = 0
        self.ballarr = []
        
    def reset(self):
        self.flg = 0
        self.ballarr = []
        
    def setballarr(self,ball):
        length = len(ball)
        for i in range(length):
            self.ballarr.append(ball[i])
    
    def initializeinitalball(self,x,y,xvel,yvel):
        if self.flg ==0:
            self.flg = 1
            temp = gameball()
            temp.setxypos(x,y)
            self.ballarr.append(temp)
            temp.updateveloc(xvel,yvel)
            
            
    def getballarr(self):
        return self.ballarr
    
    def updateallballpos(self,tdarr,cntr,resid,paddl):
        cnt = 1
        variab = 0
        tempro = []  
        while cnt!=0:
            cnt = 0
            length = len(self.ballarr)
            for i in range(length):
                if self.ballarr[i].getflagandgrab()==1:
                    cnt=cnt+1
                    tempro.append(self.ballarr[i])
                    self.ballarr.pop(i)
                    break
        length = len(self.ballarr)
        for i in range(length):
            vrb = self.ballarr[i].getpaddlecollidflag()
            tdarr = self.ballarr[i].setballupdate(tdarr,cntr,resid)
            self.ballarr[i].setpaddlecollidflag(0) 
            if vrb == 1:
                variab = 1
            
        if len(tempro)!=0:
            paddl.setactivatepaddlearr(tempro)
        return tdarr,paddl,variab
    def addball(self):
        tempo = []
        length = len(self.ballarr)
        for i in range(length):  
            gameball().setxypos(self.ballarr[i].xpos,self.ballarr[i].ypos)
            gameball().setyvel(self.ballarr[i].yvel)
            tempo.append(gameball())
        for i in range(length):
            gameball().setxvel(self.ballarr[i].xvel)
            if self.ballarr[i].xvel!=0:
                neg = -1*(tempo[i].xvel)
                tempo[i].setxvel(neg)
            else:
                tempo[i].setxvel(1)
        length = len(tempo)
        for i in range(length):
            self.ballarr.append(tempo[i])
    def removeballs(self):
        cnt = 1
        while cnt!=0:
            length = len(self.ballarr)
            cnt = 0
            for i in range(length):
                if self.ballarr[i].checkflag()==1:
                    self.ballarr.pop(i)
                    cnt=cnt+1
                    break
        return length
    
    def checkbrickcollision(self,brick,tdarr,scr):
        length = len(self.ballarr)
        for i in range(0,length,1):
            ball = self.ballarr[i]
            val = brick.checkcollisionbrick(ball.xvel,ball.yvel,ball.xpos,ball.ypos,ball.isthruball)
            ball.updateveloc(val[0],val[1])
            if val[2] != -1:
                scr=scr+1
                tdarr = brick.removebrick(tdarr,val[2])
                
            
        return brick,tdarr,scr
        
    def setthruball(self,val):
        self.isthruball=val
    def setpaddlegrabflag(self,val):
        self.flagpaddlegrab=val


    



        


            

    
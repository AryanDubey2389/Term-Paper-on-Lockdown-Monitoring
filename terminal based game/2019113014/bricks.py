from colorama import Fore, Back, Style
import random
class brick:
    def __init__(self):
        self.mat = []
        self.color = ""
        self.__bricklength = 0
        self.__level = 0
        self.__char = ''
        self.arr = []
        self.vis = []
        self.fin = []
        
        
    
class strongbrick(brick):
    def setvalues(self,prsnt,xstart,xend,ystart,yend,val):
        self.repr = 'S'
        self.isglass=0
        self.__strength = 3
        self.xstart = xstart
        self.xend = xend
        self.israin = 0
        self.__itr = 0
        self.ystart = ystart
        self.yend = yend
        self.__bid = val
        
        self.color = Back.MAGENTA
        
        
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        
        

    def getcomps(self):
        return self.xstart,self.xend,self.ystart,self.yend
    def getid(self):
        return self.__bid
    
    def setcolofvalue(self,thru):
        self.color=self.__arraycolor[(self.__itr + 1)%3]
        self.__itr = (self.__itr + 1)%3
        if thru == 1:
            self.__strength = 0
        else:
            self.__strength -= 1
        if self.__strength > 0:
            return 0
        elif self.__strength <= 0:
            return 1
    def increaseyecord(self):
        self.ystart +=1
        self.yend +=1
    

class rainbowbrick(brick):
    def setvalues(self,prsnt,xstart,xend,ystart,yend,val):
        self.repr = 'R'
        self.israin  = 1
        self.__stoprainbow = 0
        self.xstart = xstart
        self.xend = xend
        self.__itr = 0
        self.__rainbowitr = 0
        self.ystart = ystart
        self.yend = yend
        self.color = Back.GREEN
        self.__strength = 3
        
        self.__bid = val
        self.isglass=0
        
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        
        
    def getcomps(self):
        return self.xstart,self.xend,self.ystart,self.yend
    def getid(self):
        return self.__bid
    
    def setcolofvalue(self,thru):        
        self.color=self.__arraycolor[(self.__itr + 1)%3]
        self.__itr = (self.__itr + 1)%3
        self.__stoprainbow = 1
        
        if thru==1:
            self.__strength = 0
        else:
            self.__strength -= 1
        if self.__strength!=0:
            return 0
        elif self.__strength!=0:
            return 1
    def rainbowchangecolor(self):
        if self.__stoprainbow == 0:
            self.color = self.__arraycolor[(self.__rainbowitr + 1)%3]
            self.__rainbowitr = self.__rainbowitr + 1
            

    def increaseyecord(self):
        self.ystart += 1
        self.yend += 1
class unbreakablebrick(brick):
    def setvalues(self,prsnt,xstart,xend,ystart,yend,val):
        self.repr = 'U' 
        self.isglass=0
        self.__itr = 0
        self.xstart = xstart
        self.xend = xend
        self.__strength = -1
        
        self.ystart = ystart
        self.yend = yend
        self.israin = 0
        self.color = Back.RED
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        
        

    def getcomps(self):
        return self.xstart,self.xend,self.ystart,self.yend
    def getid(self):
        return self.__bid

    
    def setcolofvalue(self,thru):
        self.color=self.__arraycolor[(self.__itr + 1)%3]
        self.__itr = (self.__itr + 1)%3
        if thru==1:
            self.__strength = 0
        else:
            self.__strength = self.__strength-1
        if self.__strength < 0:
            return 0
        elif self.__strength >= 0:
            return 1
    
    def increaseyecord(self):
        self.ystart +=1
        self.yend +=1
class glassbrick(brick):
    def setvalues(self,prsnt,xstart,xend,ystart,yend,val):
        self.repr = 'G'
        self.__itr=0
        self.israin=0
        self.xstart = xstart
        self.xend = xend
        self.__strength = 1
        self.ystart = ystart
        self.yend = yend
        self.isglass = 1
        self.color = Back.BLUE  
        self.__bid = val
        self.__arraycolor = [Back.MAGENTA,Back.YELLOW,Back.BLUE]
        
    def getcomps(self):
        return self.xstart,self.xend,self.ystart,self.yend
    def getid(self):
        return self.__bid

    
    def setcolofvalue(self,thru):
        self.color=self.__arraycolor[(self.__itr + 1)%3]
        self.__itr = (self.__itr + 1)%3
        if thru == 1:
            self.__strength = 0
        else:
            self.__strength -= 1
        if self.__strength > 0:
            return 0
        elif self.__strength <= 0:
            return 1

    def increaseyecord(self):
        self.ystart +=1
        self.yend +=1
        
class brickarray(brick):
    def __init__(self):
        self.__itr = 0
        self.__movebrickflag = 0
        self.copy = []
        self.__level = 0
        self.currentbricknumber = 16
        self.movebricktime = 4
        self.idarr = []
        self.minimum1 = 0
        
    def movebrickdown(self,tdarr,timeer,flg):
        self.minimum1 = 0
        if timeer > 3:
            if flg==1:
                for i in range(0,37):
                    # self.mat.append(idarr[i][j])
                    for j in range(0,150):
                        print(self.idarr[i][j],end="")
                    print()

                for i in range(35):
                    strin1 = ''
                    flag = 0
                    flagstart = 0 
                    startindx = 0
                    strin2 = ''
                    endindx = 0
                    flagend = 0


                    for j in range(150):
                        if self.idarr[i][j] != 0:
                            flag = 1
                            endindx = j
                            if flagstart == 0:
                                startindx = j
                                flagstart = 1
                            
                    if flag == 1:
                        for j in range(150):
                            if j>=startindx and j<=endindx:
                                strin1=strin1+" "
                                strin2=strin2+tdarr[i][j]
                            else:
                                strin1=strin1+tdarr[i][j]
                                strin2=strin2+tdarr[i+1][j]
                        tdarr[i]=strin1
                        tdarr[i+1] = strin2
                        
                for i in range(17):
                    self.arr[i].increaseyecord()

                for i in range(35,1,-1):
                    k = i - 1
                    for j in range(150):
                        self.idarr[i][j]=self.idarr[k][j]

                


                returnarray = []
                minimumz = 0
                for i in range(37):
                    strin=''
                    char = ' '
                    flag = 0  
                    for j in range(150):
                        flag = 0
                        for k in range(1,18):
                            if j>=self.arr[k-1].xstart and j<=self.arr[k-1].xend:
                                if i>=self.arr[k-1].ystart and i<=self.arr[k-1].yend:
                                    if self.idarr[i][j] != 0:
                                        char = self.arr[k-1].repr
                                    flag = 1
                                    break
                        if flag==1:
                            strin=strin+char
                        else:
                            strin=strin+tdarr[i][j]
                    returnarray.append(strin)
                
                for i in range(37):
                    for j in range(150):
                        if self.idarr[i][j]==0:
                            flag = 1
                            continue
                        else:
                                minimumz = i
                if minimumz >= 34:
                    self.minimum1 = 1
                return returnarray
        return tdarr
    
    def initializebricks(self):  
        if self.__level == 0:
            print("movebrick flag = ",self.__movebrickflag)
            self.arr=[]
            br1 = unbreakablebrick()
            br1.setvalues(1,42,43,10,11,1)
            self.arr.append(br1)
            br2 = strongbrick()
            br2.setvalues(1,44,45,10,11,2)
            self.arr.append(br2)
            br3 = unbreakablebrick()
            self.arr.append(br3)
            br3.setvalues(1,40,41,12,13,3)
            br4 = glassbrick()
            br4.setvalues(1,42,47,12,13,4)
            self.arr.append(br4)
            br5 = unbreakablebrick()
            br5.setvalues(1,48,49,12,13,5)
            self.arr.append(br5)
            br6 = glassbrick()
            br6.setvalues(1,42,43,14,15,6)
            self.arr.append(br6)
            br7 = strongbrick()
            br7.setvalues(1,44,45,14,15,7)
            self.arr.append(br7)
            br8 = glassbrick()
            br8.setvalues(1,46,48,14,15,8)
            self.arr.append(br8)
            br9 = glassbrick()
            br9.setvalues(1,42,43,16,17,9)
            self.arr.append(br9)
            br10 = unbreakablebrick()
            br10.setvalues(1,44,46,16,17,10)
            self.arr.append(br10)
            br11 = strongbrick()
            br11.setvalues(1,47,48,16,17,11)
            self.arr.append(br11)
            br12 = glassbrick()
            br12.setvalues(1,49,50,16,17,12)
            self.arr.append(br12)
            br13 = rainbowbrick()
            br13.setvalues(1,50,55,12,13,13)
            self.arr.append(br13)
            br14 = glassbrick()
            br14.setvalues(1,38,39,12,13,14)
            self.arr.append(br14)
            br15 = glassbrick()
            br15.setvalues(1,36,37,12,13,15)
            self.arr.append(br15)
            br16 = glassbrick()
            self.arr.append(br16)
            br16.setvalues(1,40,41,14,15,16)
            br17 = strongbrick()
            
            br17.setvalues(1,46,49,10,11,17)
            self.arr.append(br17)


    
    def createarr(self,tdarr):
        if self.__level == 0:  
            ans = []
            self.idarr = []
            self.copy = []
            self.vis = []
            self.initializebricks()
            
            
            for i in range(0,37):
                temp = []
                for j in range(0,150):
                    temp.append(0)
                self.vis.append(temp)
                self.idarr.append(temp)
            
            for i in range(37):
                strin=''
                char = ' '
                flag = 0
                for j in range(150):
                    flag = 0
                    for k in range(1,18):
                        if i>=self.arr[k-1].ystart and i<=self.arr[k-1].yend:
                            if j>=self.arr[k-1].xstart and j<=self.arr[k-1].xend:
                                flag = 1
                                char = self.arr[k-1].repr
                                self.idarr[i][j] = self.arr[k-1].getid()
                                # print("index at this point = ",self.idarr[i][j])
                                break
                    if flag==1:
                        strin=strin+char
                    else:
                        strin=strin+tdarr[i][j]
                self.copy.append(strin)
            return self.copy
    def increaselevel(self):
        self.__level = self.__level + 1
    def changerainbowcolor(self):
        length = len(self.arr)
        for j in range(length):
            if self.arr[j].israin==1:
                self.arr[j].rainbowchangecolor()
    
    
    
    def getarray(self):
        return self.arr
    def setnewbricknumber(self,val):
        self.currentbricknumber = self.currentbricknumber - val
    def getcopy(self):
        return self.copy
    
    def getcurrentbrick(self):
        return self.currentbricknumber
    def checkcollisionbrick(self,xvel,yvel,xpos,ypos,thruball):
        flag = 0
        xexp = xpos + xvel
        iden = -1
        yexp = ypos + yvel  
        targetx = (xpos + xpos + xvel)/2
        if xexp >=124 or xexp<1 or yexp >=34 or yexp<0:
           return xvel,yvel,-1
        
        if xvel >= 0 and yvel < 0:
            for i in range(xpos,int(min(149,targetx+1)),1):
                if self.idarr[ypos-1][i] == flag:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-1][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs:
                                if i<=xcompre:
                                    if flag==0 and thruball == 0:
                                        yvel = -1*yvel
                                        if self.arr[j].setcolofvalue(thruball) ==1:
                                            iden = self.idarr[ypos-1][i]
                                        flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos][i+1] ==0:
                    continue
                else: 
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos][i+1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag==0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos][i+1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
            for i in range(int(min(149,targetx+1)),int(min(149,xpos+xvel+1)),1):
                if self.idarr[ypos-2][i]==flag:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-2][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs:
                                if i<=xcompre:
                                    if flag==0 and thruball == 0:
                                        yvel = -1*yvel
                                        if self.arr[j].setcolofvalue(thruball) ==1:
                                            iden = self.idarr[ypos-2][i]
                                        flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos-1][i+1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-1][i+1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag==0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos-1][i+1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 1:
                        break
                    else:
                        continue
        
        elif xvel < 0 and yvel < 0:
            for i in range(xpos,int(max(0,targetx-1)),-1):
                vel2 = 0
                if self.idarr[ypos-1][i]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-1][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs: 
                                if i<=xcompre:
                                    if flag==0 and thruball == 0:
                                        yvel = -1*yvel
                                        if self.arr[j].setcolofvalue(thruball) ==1:
                                            iden = self.idarr[ypos-1][i]
                                        flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos][i-1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos][i-1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if (xpos-xcompre)==1 and flag == 0 and thruball == 0:
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos][i-1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
            for i in range(int(max(0,targetx+1)),int(max(0,xpos+xvel-1)),-1):
                vel1 = 0
                if self.idarr[ypos-2][i]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-2][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs:
                                if i<=xcompre:
                                    vel1+=1
                                    if flag == 0 and thruball == 0:
                                        vel2+=1
                                        yvel = -1*yvel
                                        chk = self.arr[j].setcolofvalue(thruball)
                                        if chk ==1:
                                            iden = self.idarr[ypos-2][i]
                                        flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos-1][i-1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos-1][i-1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag == 0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel 
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos-1][i-1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
        
        elif xvel >= 0 and yvel > 0:
            for i in range(xpos,int(min(149,targetx+1))):
                vel5 = 0
                if self.idarr[ypos+1][i]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+1][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre and flag==0 and thruball == 0: 
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos+1][i]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos][i+1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos][i+1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag == 0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel 
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos][i+1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 1:
                        break
                    else:
                        continue
            for i in range(int(min(149,targetx+1)),int(min(xpos+xvel+1,149)),1):
                if self.idarr[ypos+2][i]==flag:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+2][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre and flag==0 and thruball == 0: 
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos+2][i]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos+1][i+1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+1][i+1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag == 0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel 
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos+1][i+1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break

        elif xvel < 0 and yvel > 0:
            flag = 0
            for i in range(xpos,int(max(0,targetx-1)),-1):
                temp =  self.idarr[ypos+1][i]
                if temp==flag:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+1][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre and flag == 0 and thruball == 0: 
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos+1][i]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos][i-1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos][i-1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if (xpos-xcompre)==1 and flag == 1 and thruball == 0:
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos][i-1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
            for i in range(int(max(0,targetx+1)),int(max(0,xpos+xvel-1)),-1):
                vel3 = 0
                if self.idarr[ypos+2][i]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+2][i]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if i>=xcomprs and i<=xcompre and flag==0 and thruball == 0: 
                                yvel = -1*yvel
                                if self.arr[j].setcolofvalue(thruball) ==1:
                                    iden = self.idarr[ypos+2][i]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break
                if self.idarr[ypos+1][i-1]==0:
                    continue
                else:
                    for j in range(len(self.arr)):
                        if self.arr[j].getid()==self.idarr[ypos+1][i-1]:
                            xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                            if xcomprs-xpos==1 and flag == 0 and xvel!=0 and thruball == 0:
                                xvel = -1*xvel 
                                if self.arr[j].setcolofvalue(thruball)==1:
                                    iden = self.idarr[ypos+1][i-1]
                                flag = 1
                        if flag == 0:
                            continue
                        else:
                            break
                    if flag == 0:
                        continue
                    else:
                        break   
        val = -1
        return xvel,yvel,iden
    
    
    def checkerglass(self,iden):
        length = len(self.arr)
        for j in range(length):
            if self.arr[j].getid()==iden:
                return self.arr[j]

    def retrunidval(self):
        return self.idarr
    def getarray(self):
        return self.arr
    
    def updateglassarr(self,arr,elem,vis):
        que = []
        que.push(arr)
        idx = 0
        while 1:
            if len(que) == 0:
                break
            else:
                length = len(que)
                for i in range(length):
                    coordinatess = que[i].getcomps()
                    xcomprs,xcompre,ycomprs,ycompre = coordinatess
                    for l in range(xcomprs,xcompre+1,1):
                        temp = self.idarr[ycomprs-1][l]
                        if temp!=0:
                            if checkglass(temp)==1:
                                if vis[temp]!=1:
                                    que.push()

                        temp = self.idarr[ycompre+1][l]
                        if temp!=0:
                            visit[temp]=1
                    for l in range(ycomprs,ycompre+1):
                        temp = self.idarr[l][xcompre+1]
                        if temp!=0:
                            visit[temp]=1
                        temp = self.idarr[l][xcomprs-1]
                        if temp!=0:
                            visit[temp]=1
    
    def returnvis(self):
        return self.vis
    
    def getcopy(self):
        return self.copy
    
    def removebrick(self,tdarr,iden):
        visit = []
        v1 = 0
        flag = 0
        for i in range(20):
            visit.append(0)
        velarray = []
        a = " "
        for j in range(len(self.arr)):
            if self.arr[j].getid()==iden:
                xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                velarray.append(v1)
                for i in range(ycomprs,ycompre+1):
                    strin =""
                    for k in range(xcomprs):
                        var = tdarr[i][k]
                        strin+=var
                    for k in range(xcomprs,xcompre+1):
                        strin+=a
                    for k in range(xcompre+1,150):
                        var = tdarr[i][k]
                        strin+=var
                    tdarr[i]=strin
                for l in range(ycomprs,ycompre+1):
                    v1+=1
                    for m in range(xcomprs,xcompre+1,1):
                        self.idarr[l][m]=0
                if self.arr[j].isglass==1: 
                    flag = 1 
                    que = [] 
                    
                    
                    que.append(self.arr[j])
                    while 1:
                        if len(que) == 0:
                            break
                        else:
                            for t in range(len(que)):
                                xcomprs,xcompre,ycomprs,ycompre = que[t].getcomps()
                                flag = 0
                                #print(flag)
                                for l in range(xcomprs,xcompre+1):
                                    if self.idarr[ycomprs-1][l]!=0:
                                        if self.checkerglass(self.idarr[ycomprs-1][l]).isglass==1:
                                            if visit[self.idarr[ycomprs-1][l]]!=1:
                                                temp = 1
                                                visit[self.idarr[ycomprs-1][l]]=temp
                                                que.append(self.checkerglass(self.idarr[ycomprs-1][l]))
                                        else:
                                            temp = 1
                                            visit[self.idarr[ycomprs-1][l]]=temp
                                    if self.idarr[ycompre+1][l]!=0:
                                        if self.checkerglass(self.idarr[ycompre+1][l]).isglass==1:
                                            if visit[self.idarr[ycompre+1][l]]!=1:
                                                temp = 1
                                                visit[self.idarr[ycompre+1][l]]=temp
                                                que.append(self.checkerglass(self.idarr[ycompre+1][l]))
                                        else:
                                            temp = 1
                                            visit[self.idarr[ycompre+1][l]]=temp
                                for l in range(ycomprs,ycompre+1):
                                    if self.idarr[l][xcompre+1]!=0:
                                         
                                        if self.checkerglass(self.idarr[l][xcompre+1]).isglass==1:
                                            if visit[self.idarr[l][xcompre+1]]!=1:
                                                temp = 1
                                                visit[self.idarr[l][xcompre+1]]=temp
                                                que.append(self.checkerglass(self.idarr[l][xcompre+1]))
                                        else:
                                            temp = 1
                                            visit[self.idarr[l][xcompre+1]]=temp

                                    if self.idarr[l][xcomprs-1]!=0:
                                         
                                        if self.checkerglass(self.idarr[l][xcomprs-1]).isglass==1:
                                            if visit[self.idarr[l][xcomprs-1]]!=1:
                                                temp = 1
                                                visit[self.idarr[l][xcomprs-1]]=temp
                                                que.append(self.checkerglass(self.idarr[l][xcomprs-1]))
                                        else:
                                            temp = 1
                                            visit[self.idarr[l][xcomprs-1]]=temp
                            que.pop(0)
     
        for i in range(20):
            if visit[i]!= 0:
                a = " "
                for j in range(len(self.arr)):
                    temp = self.arr[j].getid()
                    if temp == i:
                        v1 +=1
                        xcomprs,xcompre,ycomprs,ycompre = self.arr[j].getcomps()
                        velarray.append(v1)
                        for t in range(ycomprs,ycompre+1):
                            strin =""
                            for k in range(xcomprs):
                                var = tdarr[t][k]
                                strin+=tdarr[t][k]
                            for k in range(xcomprs,xcompre+1):
                                strin+=a
                            for k in range(xcompre+1,150):
                                var = tdarr[t][k]
                                strin+=tdarr[t][k]
                            tdarr[t]=strin
                            flag = 0
                            for l in range(ycomprs,ycompre+1):
                                for m in range(xcomprs,xcompre+1,1):
                                    self.idarr[l][m]=flag





        return tdarr
    def getminimum1(self):
        return self.minimum1
    def returnvis(self):
        return self.vis




    
        
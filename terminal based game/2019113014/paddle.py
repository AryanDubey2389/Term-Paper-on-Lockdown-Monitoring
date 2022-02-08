from colorama import Fore, Back, Style
from ball import*
class paddl:
    def __init__(self):
        self.__var = 1
        self.__len = 5
        self.__strin=""  
        self.__txt = '='
        self.__cntr =3  
        self.__resid = 2
        self.__activategrabpaddle = 0
        self.__activatepaddlarr = []
        for i in range(150):
            if i>=1 and i<=5:
                self.__strin+=("=")
            if i==0 or i==149:
                self.__strin+="#"
    def getactivategrabpaddle(self):
        return self.__activategrabpaddle
    
    def __movright(self,arr):
        if(self.__var>142):
            return arr,self.__activategrabpaddle
        else:
            length = len(self.__activatepaddlarr)
            for i in range(length):
                self.__activatepaddlarr[i].setxypos(self.__activatepaddlarr[i].getxpos()+2,34)
            self.__var+=2
            self.__strin=("")
            self.__cntr+=2
            for i in range(0,self.__var):
                if i!=0:
                    self.__strin+=" "
                elif i == 0:
                    self.__strin+="#"
                    
            for i in range(self.__var,self.__var+self.__len):
                self.__strin = self.__strin+("=")
            for i in range(self.__var+self.__len,150):
                if i==149:
                    self.__strin=self.__strin+"#"
                else:
                    self.__strin=self.__strin+" "
            arr[35]=self.__strin
            self.__strin=""
            length = len(self.__activatepaddlarr)
            for i in range(150):
                #print(flag)
                chk = 0
                ball = "O"
                for j in range(length):
                    x = self.__activatepaddlarr[j]
                    if x.getxpos()==i:
                        chk = 1
                if chk == 0:
                    if i==0 or i==149:
                        self.__strin+='#'
                    else:
                        self.__strin+=" "       
                else:
                    self.__strin+=ball
                    
                    
            arr[34]=self.__strin
        return arr,self.__activategrabpaddle
    def padlrightpos(self):
        x = self.__var+self.__len+1
        if self.__var+self.__len+1<=148:
            return 1
        else:
            return 0

    def __movleft(self,arr):
        if(self.__var>=3):
            self.__strin=""
            self.__cntr-=2
            length = len(self.__activatepaddlarr)
            for i in range(length):
                self.__activatepaddlarr[i].setxypos(self.__activatepaddlarr[i].getxpos()-2,34)
            self.__var-=2 
            
            for i in range(0,self.__var):
                if i!=0:
                    self.__strin+=" "
                elif i==0:
                    self.__strin+="#"
            for i in range(self.__var,self.__var+self.__len):
                self.__strin=self.__strin+("=")
            for i in range(self.__var+self.__len,150):
                if i!=149:
                    self.__strin+=" "
                elif i==149:
                    self.__strin+="#"
            arr[35]=self.__strin
            self.__strin=""
            length = len(self.__activatepaddlarr)
            for i in range(150):
                chk = 0
                ball = "O"
                for j in range(length):
                    x = self.__activatepaddlarr[j]
                    if x.getxpos()==i:
                        flag = 1
                        chk = 1
                if chk == 0:
                    if i==0 or i==149:
                        self.__strin+='#'
                    else:
                        self.__strin+=' '
                elif chk == 1:
                    self.__strin+=ball
                
                    
                    
            arr[34]=self.__strin
        return arr,self.__activategrabpaddle
    def initializepaddle(self):
        self.__len = 5
        strin = ""
        self.__var = 1
        self.__resid = 2
        for i in range(150):
            if i==0 and i>5:
                strin = strin + self.__txt
            else:
                strin=strin+" "
        return strin
    def padlleftpos(self):
        x = self.__var-2
        if x < 0:
            return 0
        elif x >= 0:
            return 1
    def returnpaddle(self,tdarr):
        strint=''
        for i in range(0,self.__var):
            if i!=0:
                strint+=" "
            elif i==0:
                strint+="#"
        for i in range(self.__var,self.__var+self.__len):
            strint=strint+("=")
        for i in range(self.__var+self.__len,150):
            if i!=149:
                strint+=" "
            elif i==149:
                strint+="#"
        tdarr[35] = strint
        length = len(self.__activatepaddlarr)
        if self.__activategrabpaddle != 0:
            self.__strin=""
            for i in range(150):
                ball ="O"
                chk = 0
                for j in range(length):
                    x = self.__activatepaddlarr[j]
                    if x.getxpos()==i:
                        chk = 1
                if chk == 0:
                    if i==0 or i==149:
                        self.__strin+='#'
                    else:
                        self.__strin+=' '
                    
                elif chk == 1:
                    self.__strin+=ball
                        
            tdarr[34]=self.__strin
        return tdarr
    def resetpadlpos(self):
        self.__var = 1
        self.__cntr = 3
        self.__resid = 2
    def getpadlcentr(self):
        return self.__cntr
    def getpadlresid(self):
        return self.__resid
    def callmoveleft(self,arr):
        return self.__movleft(arr)
    
    def increasepadllength(self):
        self.__len=self.__len+2
        self.__cntr=self.__cntr+1
        self.__resid=self.__resid+1
    def decreasepadllength(self):
        if self.__len >=5:
            self.__len=self.__len-2
            self.__cntr=self.__cntr-1
            self.__resid=self.__resid-1
    def callmoveright(self,arr):
        return self.__movright(arr)
    def setactivagegrabpaddle(self,val):
        temp = val
        self.__activategrabpaddle = temp
        
    def getactivatepaddlearr(self):
        var = self.__activatepaddlarr
        self.setactivagegrabpaddle(0)
        self.__activatepaddlarr = []
        
        return var
    def setactivatepaddlearr(self,val):
        length = len(val)
        for i in range(length):
            self.__activatepaddlarr.append(val[i])
        self.setactivagegrabpaddle(1)


    def paddledegrab(self):
        length = len(self.__activatepaddlarr)
        if self.__activategrabpaddle==1:
            for i in range(length):

                self.__activatepaddlarr[i].setflagandgrab(0)
        
        


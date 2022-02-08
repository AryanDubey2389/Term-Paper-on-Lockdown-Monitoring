#import colorama

import time
import os
from colorama import Fore, Back, Style
import sys
#colorama.init(autoreset=True)
class printboard:
    #tdarr = []
    def __init__(self):
        self.__ballvel = 0
        self.__isupdated = 0
        self.__scr = 0
        self.__tdarr = []
        self.__timeplayed = 0
        self.__liferemain = 4
        
    def getscore(self):
        return self.__scr

    def copygrid(self):
        return self.__tdarr

    def __updategrid(self,arr):
        self.__tdarr = arr
    
    def __printscreeninit(self):
        print('\n')
        self.__tdarr = []
        print("YOUR SCORE:",0)
        for i in range(37):
            strin=""
            txt = "'"
            for j in range(150):
                if i==0 or i==36:
                    strin+="#"
                else:
                    if j==0 or j==149:
                        strin+=("#")
                    elif i==35:
                        if j==0 or j==149:
                            strin+=("#")
                        elif j >= 1 and j<=5:
                            txt = Back.RED+txt+Style.RESET_ALL
                            strin+=txt     
                        else:
                            strin+=" "   
                    else:
                        strin+=" "
            self.__tdarr.append(strin)
    def printball(self):
        self.set = 0
        self.vel = 0

    def updatescore(self,val):
        self.__scr = val

    
        
    def __printscreen(self,vis,idarr,getarr):

        print("YOUR SCORE - ", self.__scr,"  TIME ACTIVE - ",int(time.time()-self.__timeplayed),"s"," Lives Remaining - ",self.__liferemain)
        tempo = "" 

        for i in range(37):
            for j in range(150): 
                if vis[i][j] == 0:
                    print(self.__tdarr[i][j],end='')
                elif vis[i][j] != 0:
                    ident = idarr[i][j]
                    color = ""
                    for k in range(len(getarr)):
                        if getarr[k].getid() == idarr[i][j]:
                            color = getarr[k].color
                    print(tempo + color+self.__tdarr[i][j]+Back.RESET,end='')
            print()
    def callprintscreen(self,vis,idarr,getarr):
        self.__printscreen(vis,idarr,getarr)
    def setupdategrid(self,arr):
        return self.__updategrid(arr)
    
    def getlives(self):
        if self.__liferemain==0:
            print("Game Over")
            sys.exit()
        self.__liferemain-=1
    def initializetime(self):
        self.__timeplayed = time.time()
    def getinitalscreen(self):
        return self.__printscreeninit()
    
    
    




            
    

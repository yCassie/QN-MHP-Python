# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:37:17 2024

@author: wyuanc
"""

"""General animation helpers for visualizing QN-MHP entities and server states."""

import time

from qn_mhp_layout import Structure
from utility import color_changer

space = Structure().background()[0]
Cache = Structure().background()[1]
loc_dic=Structure().loc_dic
occupy_dic=Structure().occupy_dic
save_dic=Structure().save_dic
save_dic_copy=Structure().save_dic_copy

    #3.3 entity animation
class entity_animation:
                

   
    entity_loc={}
   

    
    def __init__(self):
        self.frame = Structure().frame
        self.w=Structure().w
        self.h=Structure().h
        self.circle_r = Structure().circle_r
        self.Capacity = Structure().Capacity
        self.dx = Structure().dx
        self.space = space
        self.Cache = Cache
        self.loc_dic = loc_dic
        self.occupy_dic = occupy_dic
        self.save_dic=save_dic
        self.save_dic_copy=save_dic_copy
        
    def show (self,i,j,k,server,generation):
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'

        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])

        self.save_dic[(i[0],k,generation,'0')]=self.frame.canvas.create_oval(30,self.h/2,50,self.h/2+20,fill=color,tags=(i[0],k,generation))
        self.save_dic[(i[0],k,generation,'0' ,'text')]=self.frame.canvas.create_text(40, self.h/2+10,anchor='center',text=i[0],font=("Times New Roman",10,"bold"),tags=(i[0],k,generation,'text'))
        self.save_dic_copy[(i[0],k,generation,'0')]=self.frame.canvas.create_oval(30,self.h/2,50,self.h/2+20,fill=color,tags=(i[0],k))
        self.save_dic_copy[(i[0],k,generation,'0' ,'text')]=self.frame.canvas.create_text(40, self.h/2+10,anchor='center',text=i[0],font=("Times New Roman",10,"bold"),tags=(i[0],k,generation,'text'))
        self.frame.canvas.update()
        time.sleep(0.05)
        self.frame.canvas.delete((i[0],k,generation))
        self.frame.canvas.delete((i[0],k,'text'))

    def enter (self,resource,server,connection,i,j,k,generation):
        
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'
        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])
     
        circle_r = self.circle_r
        
        #if the server is full, move the entitiy to wating room
        if resource.count>=self.Capacity[server]:     
            self.loc_dic[(server,i[0],k,generation)]=-1  #loc_dic[full/not full,space] full=-1, not full=0
            for cache in self.Cache:
                if cache['name']==connection:
                    v0 = cache['location'][0]
                    v1 = cache['location'][1]
            x=v0
            y=v1+self.dx/2-circle_r
            self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r,fill=color)
            self.save_dic[(i[0],k,server ,generation,'text')]=self.frame.canvas.create_text(x+circle_r, y+circle_r,anchor='center',text=i[0],font=("Times New Roman",10,"bold"))
            time.sleep(0.05)
            self.frame.canvas.update()        
        elif resource.count<self.Capacity[server]:   
            if self.Capacity[server] !=10e5:
                #if server is not full before the entity enters

                for item in range(self.Capacity[server]):
                    if (server,item) not in self.occupy_dic:
                        v0 = self.space[(server,item)][0]
                        v1 = self.space[(server,item)][1]        
                        x=v0
                        y=v1+self.dx/2-circle_r
                        
                        self.entity_loc[(i[0],k,server,generation)]=[x,y,color]
                        self.loc_dic[(server,i[0],k,generation)]=item
                        break 
            elif self.Capacity[server] ==10e5:
                
                self.loc_dic[(server,i[0],k,generation)]=0
                v0 = self.space[(server,0)][0]
                v1 = self.space[(server,0)][1]
            
                x=v0
                y=v1+self.dx/2-circle_r
                
                self.entity_loc[(i[0],k,server,generation)]=[x,y,color]
    
    def leave(self,i,j,k,server):
        
        if self.Capacity[server]!=10e5:
            self.occupy_dic.pop((server,self.loc_dic[(server,i[0])]))
        self.frame.canvas.coords( self.save_dic[(i[0],k,'0')],[self.w+1, self.w+1, self.w+1, self.w+1])
        self.frame.canvas.coords( self.save_dic[(i[0],k,'0','text')],[self.w+1, self.w+1])
        
    
    def add (self,server,i,j,k,generation):
        
        if i[1]['stimuli']==0:
            color='gray'
        elif i[1]['color']==-999:
            color='white'
        else:
            color=color_changer(i[1]['color'][0],i[1]['color'][1],i[1]['color'][2])
        circle_r=self.circle_r
        if  self.loc_dic[(server,i[0],k,generation)]!=-1:
            x=self.entity_loc[(i[0],k,server,generation)][0]
            y=self.entity_loc[(i[0],k,server,generation)][1]
            
            self.frame.canvas.update()
            self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r, fill=color)
            self.save_dic[(i[0],k,server,generation,'text')]=self.frame.canvas.create_text(x+circle_r,y+circle_r,anchor="center",text=i[0],font=("Times New Roman",10,"bold"))
            self.occupy_dic[(server,self.loc_dic[(server,i[0],k,generation)])]=(i[0],k,generation)
            time.sleep(0.05)
            self.frame.canvas.update()
        else:
            
            for item in range(self.Capacity[server]):
                if (server,item) not in self.occupy_dic:
                    v0 = self.space[(server,item)][0]
                    v1 = self.space[(server,item)][1]
                    self.loc_dic[server,i[0],k,generation]=item       
                    x=v0
                    y=v1+self.dx/2-circle_r
                    self.frame.canvas.coords( self.save_dic[(i[0],k,server,generation)],[self.w+1, self.w+1, self.w+1, self.w+1])
                    self.frame.canvas.coords( self.save_dic[(i[0],k,server,generation,'text')],[self.w+1, self.w+1])
                    self.frame.canvas.update()
                    self.save_dic[(i[0],k,server,generation)]=self.frame.canvas.create_oval(x, y, x + 2*circle_r, y + 2*circle_r, fill=color)
                    self.save_dic[(i[0],k,server,generation,'text')]=self.frame.canvas.create_text(x+circle_r,y+circle_r,anchor="center",text=i[0],font=("Times New Roman",10,"bold"))
                    time.sleep(0.05)
                    self.frame.canvas.update()
                    break
            self.occupy_dic[(server,item)]=(i[0],k,generation)
    
    def delete (self,i,j,k,server,generation):
        if self.Capacity[server]!=10e5:
            if (server,self.loc_dic[(server,i[0],k,generation)]) in self.occupy_dic:
                self.occupy_dic.pop((server,self.loc_dic[(server,i[0],k,generation)]))
        entity_del =  self.save_dic[(i[0],k,server,generation)]
        entity_num_del = self.save_dic[(i[0],k,server,generation,'text')]
        self.frame.canvas.delete(entity_del)
        self.frame.canvas.delete(entity_num_del)
        time.sleep(0.05)
        self.frame.canvas.update()
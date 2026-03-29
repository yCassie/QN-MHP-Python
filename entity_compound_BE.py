# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:55:01 2024

@author: wyuanc
"""

"""Entity-generation functions for compound behavior elements, including concurrent task streams."""

from random import randint
from utility import look_for_ls,color_dic,track1D_amp_dic,track1D_freq_dic,direction_track1D,track2D_freq_dic,track2D_amp_dic,static2D_freq_dic,dynamic1D_freq_dic,dynamic2D_freq_dic
from utility import save_user_input as save
from utility import random_cpt,random_mpt,random_ppt
from animation_general import entity_animation
from gui_general import Tasklist_dic,task_info_dic,anim,saved,path
from compound_BE import Look_for
from main_process import process as process
import time
import random
import math


j=None
#4.8 entity generation
class entity_generation:
    
    def Look_for_en(self,env,qn_mhp,k_):
        
        
        generation='look_for_en'
    
        # initialization
        i = [0]
        index=0
        count=0
        k=k_
        yield env.timeout(0)  
        #generate entities
    
    
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        attribute = {'stimuli':1,'type':2,'info':6}
      
        if len(look_for_ls)>1:
            item=randint(1,len(look_for_ls)-1)
        elif len(look_for_ls)==1:
            item=0
        attribute['eye_loc']=look_for_ls[item][0]
        attribute['color']=look_for_ls[item][2]
        attribute['text']=look_for_ls[item][1]  
    
        
        if len(look_for_ls)==0:
            attribute['eye_loc']=-999
            attribute['color']=-999
            attribute['text']=-999  
                
    
        i.append(attribute)
        if attribute['stimuli']==1 and len(look_for_ls)!=0:
            del look_for_ls[item]
            count+=1
        i[1]['color'] = color_dic[i[1]['color']]
        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
            
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()   
        env.process(Look_for(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, count, generation,ppt,cpt,mpt))
        
    
    
    def track1D_en(self,env,qn_mhp,k_):
        
        #from gui_compound_BE import track1D_curse_loc
        
        generation='track1D_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        #target=0
        #user=track1D_curse_loc
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))            
        

                
    def track2D_en(self,env,qn_mhp,k_):
        
        #from gui_compound_BE import track2D_cursor_loc_x,track2D_cursor_loc_y,track2D_target_loc_x,track2D_target_loc_y
        
        generation='track2D_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified

        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999,-999,-999]#[target_x,user_x,target_y,user_y]
        attribute['color']=-999
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))   


    
    def static2D_en(self,env,qn_mhp,k_):
        
        from display_compound_BE import Reaction_static_2DTracing
        from gui_compound_BE import static2D_cursor_loc_x
        
        generation='static2D_en'
    
        # initialization
        i = [0]
        index=0              
        k=k_
        yield env.timeout(0)  
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target_x=-Reaction_static_2DTracing().xmax
        target_y=math.sin(target_x)
        user_x=-Reaction_static_2DTracing().xmax+(2*Reaction_static_2DTracing().xmax*static2D_cursor_loc_x/100)
        user_y=math.sin(user_x)
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target_x,target_y,user_x,user_y]#[target,user]
        attribute['color']=-999
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)      

        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))   

    
    def dynamic1D_en(self, env,qn_mhp,k_):
        
        from gui_compound_BE import dynamic1D_cursor_loc
        
        generation='dynamic1D_en'
    
        # initialization
        i = [0]
        index=0
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified
        
        target=0
        user=dynamic1D_cursor_loc
        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[target,user]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))   
     
    
    def tracing1D_b_en(self,env,qn_mhp,k_):
        
        generation='trace1D_b_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified

        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))  
    
    
    def tracing1D_1w_en(self,env,qn_mhp,k_):
        
        generation='trace1D_1w_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified

        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt)) 
    
    
    
    def tracing2D_b_en(self,env,qn_mhp,k_):
        
        generation='trace2D_b_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified

        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999,-999,-999]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt))        
        
    def tracing2D_1w_en(self,env,qn_mhp,k_):
        
        generation='trace2D_1w_en'
    
        # initialization
        i = [0]
        index=0
        
        k=k_
        yield env.timeout(0)  
                
                
        #update entity index i
        index+=1
        i=[index]        
        #update outserver_dic. outserver_dic indicates whether entity can be sent from item server to the next server
        #e.g. if outserver_dic[1] = 1, it means entity can be sent from server1 to server2&3
        #server index in this case: server name 1-8: index1-8 A:101 B:102 C:103 F:104 W:201 Y:202 Z:203
        #server index will be consistent with Hanning's code
        outserver_dic = {}
        for item in range(1,300):
            outserver_dic[item] = 0
        #update arival time
        arrival_time = env.now
        #update attibute 
        #0: noise 1: stimuli; 2:visual 3:auditory; 4:spatial 5:verbal 6:both spatial and verbal  7: unknown or unspecified

        
        attribute = {'stimuli':1,'type':2,'info':6}
        attribute['eye_loc']=[-999,-999,-999,-999]#[target,user]
        attribute['color']=(255,0,0)
        i.append(attribute)

        if anim==1:
            entity_animation().show(i, j, k, '0',generation)
        
        # Call the functions to get a new random process time each entity
        ppt = random_ppt()
        cpt = random_cpt()
        mpt = random_mpt()
        
        env.process(process(qn_mhp, env, i, j, k, attribute, outserver_dic, arrival_time, generation,ppt,cpt,mpt)) 
        


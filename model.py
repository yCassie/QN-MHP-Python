# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:18:28 2024

@author: wyuanc
"""

"""SimPy server definitions and service logic for the QN-MHP architecture."""

import simpy
from animation_general import entity_animation

from gui_general import anim
import random
import math

#define ppt, cpt, mpt
#change ppt, cpt, mpt thourgh module utility.py

#ppt = round((-1) * 16 * math.log(1-random.uniform(0,1)) + 17,2)
#cpt = round((-1) * 22 * math.log(1-random.uniform(0,1)) + 13,2)
#mpt = round((-1) * 14 * math.log(1-random.uniform(0,1)) + 10,2)

#ppt=33
#cpt=35
#mpt=24

#data record for specific BE 
forced_exit_dic={}


#4.5 Servers

class QN_MHP (object):
    
    def __init__(self, env):
        self.env = env
        self.resource()
    def resource(self):
        env=self.env
        self.server1 = simpy.Resource(env,10e5)
        self.server2= simpy.Resource(env, 4)
        self.server3 = simpy.Resource(env, 4)
        self.server4 = simpy.Resource(env,5)
        self.server5 = simpy.Resource(env,10e5)
        self.server6= simpy.Resource(env, 4)
        self.server7 = simpy.Resource(env, 4)
        self.server8 = simpy.Resource(env,5)
        self.serverA = simpy.PreemptiveResource(env,4)
        self.serverB = simpy.PreemptiveResource(env,4)
        self.serverC = simpy.Resource(env,5)
        self.serverD = simpy.Resource(env,10e5)
        self.serverE = simpy.Resource(env,1)
        self.serverF = simpy.Resource(env,1)
        self.serverG = simpy.Resource(env,10e5)
        self.serverW = simpy.Resource(env,1)
        self.serverY = simpy.Resource(env,2)
        self.serverZ = simpy.Resource(env,5)
        self.righthand = simpy.Resource(env,1)
        self.lefthand = simpy.Resource(env,1)
        self.eyes = simpy.Resource(env,1)

        
class server_def:
    #perception
    def server1(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.server1.request() as request:
            yield request
            yield env.timeout(ppt)
    
    
    def server2(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,background,ppt,cpt,mpt):
        if anim==1:       
            background.enter(qn_mhp.server2, '2', '1_2', i, j, k,generation)
            with qn_mhp.server2.request() as request:
                yield request
                background.add('2', i, j, k,generation)
                yield env.timeout(ppt)
            outserver_dic[2]=1
            background.delete(i, j, k, '2',generation)

            background.enter(qn_mhp.server4, '4', '2_4', i, j, k,generation)
    
        else:       
            with qn_mhp.server2.request() as request:
                yield request
                yield env.timeout(ppt)
            outserver_dic[2]=1
                
    def server3(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,background,ppt,cpt,mpt):  
        if anim==1:
            background.enter(qn_mhp.server3, '3', '1_3', i, j, k,generation)
            with qn_mhp.server3.request() as request:        
                yield request
                background.add('3', i, j, k,generation)
                yield env.timeout(ppt) 
            outserver_dic[3]=1
            background.delete(i, j, k, '3',generation)
            background.enter(qn_mhp.server4, '4', '3_4', i, j, k,generation)
        else:
            with qn_mhp.server3.request() as request:        
                yield request
                yield env.timeout(ppt) 
            outserver_dic[3]=1
    
    def server4(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.server4.request() as request:
            yield request
            yield env.timeout(ppt)
    
    def server5(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.server5.request() as request:
            yield request
            yield env.timeout(ppt)
    
    def server6(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        if anim==1:       
            entity_animation().enter(qn_mhp.server6, '6', '5_6', i, j, k,generation)
            with qn_mhp.server6.request() as request:
                yield request
                entity_animation().add('6', i, j, k,generation)
                yield env.timeout(ppt)
            outserver_dic[6]=1
            entity_animation().delete(i, j, k, '6',generation)
            entity_animation().enter(qn_mhp.server8, '8', '6_8', i, j, k,generation)
        else:       
            with qn_mhp.server6.request() as request:
                yield request
                yield env.timeout(ppt)
            outserver_dic[6]=1
    
    def server7(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):  
        if anim==1:
            entity_animation().enter(qn_mhp.server7, '7', '5_7', i, j, k,generation)
            with qn_mhp.server7.request() as request:        
                yield request
                entity_animation().add('7', i, j, k,generation)
                yield env.timeout(ppt) 
            outserver_dic[7]=1
            entity_animation().delete(i, j, k, '7',generation)
            entity_animation().enter(qn_mhp.server8, '8', '7_8', i, j, k,generation)
        else:
            with qn_mhp.server7.request() as request:        
                yield request
                yield env.timeout(ppt) 
            outserver_dic[7]=1
    
    def server8(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.server8.request() as request:
            yield request
            yield env.timeout(ppt)
    
    
    #cognition
    def serverA(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,prio,generation,ppt,cpt,mpt):
        if anim==1:
            if outserver_dic[4]==1:
                entity_animation().enter(qn_mhp.serverA,'A','4_A', i, j, k,generation)
            else:
                entity_animation().enter(qn_mhp.serverA,'A','8_A', i, j, k,generation)
            with qn_mhp.serverA.request(priority=prio) as request:                       
                yield request   
                entity_animation().add('A', i, j, k,generation)         
                try:
                    yield env.timeout(cpt)  #use cpt time
                                 
                except simpy.Interrupt:
                    forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                    print('%.2fmsec, entity %s is forced to exit serverA'%(env.now, (i[0],k)))
                  
                entity_animation().delete(i, j, k, 'A',generation)   
        else:
            with qn_mhp.serverA.request(priority=prio) as request:                       
                yield request                   
                try:
                    yield env.timeout(cpt)  #use cpt time               
                except simpy.Interrupt:
                    forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                    print('%.2fmsec, entity %s is forced to exit serverA'%(env.now, (i[0],k)))
            
    def serverB(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,prio,generation,ppt,cpt,mpt):
        if anim==1:
            if outserver_dic[4]==2:
                entity_animation().enter(qn_mhp.serverB,'B','4_B', i, j, k,generation)
            else:
                entity_animation().enter(qn_mhp.serverB,'B','8_B', i, j, k,generation)
            with qn_mhp.serverB.request(priority=prio) as request:                       
                yield request 
                entity_animation().add('B', i, j, k,generation)         
                try:
                    yield env.timeout(cpt)  #use cpt time
                                  
                except simpy.Interrupt:
                    forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                    print('%.2fmsec, entity %s is forced to exit serverB'%(env.now, (i[0],k)))
                entity_animation().delete(i, j, k, 'B',generation)  
        else:
            with qn_mhp.serverB.request(priority=prio) as request:                       
                yield request                   
                try:
                    yield env.timeout(cpt)  #use cpt time               
                except simpy.Interrupt:
                    forced_exit_dic[(i[0],k)]=['%.2fmsec'%(arrival_time), attribute]  
                    print('%.2fmsec, entity %s is forced to exit serverB'%(env.now, (i[0],k)))
    
    def serverC(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.serverC.request() as request:
            yield request
            yield env.timeout(cpt)    
            
    def serverF(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.serverF.request() as request:
            yield request
            yield env.timeout(cpt)  
    
    #To be decided:
        #serverD, serverG, serverH, 
    
    #Motor
    def serverW(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.serverW.request() as request:
            yield request
            yield env.timeout(mpt)  
            
    def serverY(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.serverY.request() as request:
            yield request
            yield env.timeout(mpt)  
            
    def serverZ(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.serverZ.request() as request:
            yield request
            yield env.timeout(mpt)  
            
    def server22(self,qn_mhp,env,i,j,k,attribute,outserver_dic,arrival_time,generation,ppt,cpt,mpt):
        with qn_mhp.server22.request() as request:
            yield request
            yield env.timeout(20)  
    
    #To be decided: 
        #serverV, server21, ser server23, server24


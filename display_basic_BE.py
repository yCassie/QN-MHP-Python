# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:55:02 2024

@author: wyuanc
"""
"""Display primitives and animation support for basic behavior-element tasks."""

import time
import tkinter as tk
from tkinter import messagebox
from gui_general import task_info_dic
from qn_mhp_layout import myCanvas
from utility import color_changer, look_for_ls,color_list,text_list

if 'Press_button' in task_info_dic.values():
    class reaction_press_button:
   
        def __init__(self,task_no):
            
            self.task_no = task_no
            from gui_basic_BE import choice_N
            self.N = choice_N[self.task_no]
        
        def background(self,sti_type):
            self.root = tk.Tk()
            self.w = self.root.winfo_screenwidth() / 2
            self.h = self.root.winfo_screenheight() / 5
            self.frame = myCanvas(self.root, self.w, self.h)  # Assuming myCanvas is defined elsewhere
            self.frame.canvas.pack(fill="both", expand=True)
            self.root.title('Reaction')
            self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, 0, self.root.winfo_screenheight() / 1.7))
            
            
            
            frame=self.frame
            w=self.w
            h=self.h
            N=self.N
            
            self.sti_type=sti_type
            
            if sti_type=='color':
               
                if N == 1:
                    frame.canvas.create_rectangle(w / 2 - 80, h / 2 - 18, w / 2 + 80, h / 2 + 18, fill='red', outline='red')
                else:
                    for c in range(N):
                        color = color_list[c]
                        frame.canvas.create_rectangle(w / (N + 1) * c + 30, h / 2 - 18, w / (N + 1) * c + 150, h / 2 + 18,
                                                      fill=color_changer(color[0], color[1], color[2]))
            elif sti_type=='text':
                if N==1:
                    frame.canvas.create_rectangle(w/2-80,h/2-18,w/2+80,h/2+18,fill='white',outline='white')
                    frame.canvas.create_text(w/2, h/2,anchor='center',text='A',font=("Times New Roman",15,"bold"))
                else:
                    for c in range(N):
                        text=text_list[c]
                        frame.canvas.create_rectangle(w/(N+1)*c+30,h/2-18,w/(N+1)*c+150,h/2+18,fill='white')
                        frame.canvas.create_text(w/(N+1)*c+90, h/2,anchor='center',text=text,font=("Times New Roman",15,"bold"))
        
        def add_button(self, i):
            
            if self.sti_type=='color':
            
                if self.N == 1:
                    self.frame.canvas.create_rectangle(self.w / 2 - 80, self.h / 2 - 18, self.w / 2 + 80, self.h / 2 + 18,
                                                       fill='gray', outline='gray', tag='button_rec')
                    self.frame.canvas.update()
                    time.sleep(0.4)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()
                else:
                    for item in range(self.N):
                        if i[1]['color'] == color_list[item]:
                            self.frame.canvas.create_rectangle(self.w / (self.N + 1) * item + 30, self.h / 2 - 18,
                                                               self.w / (self.N + 1) * item + 150, self.h / 2 + 18, fill='gray',
                                                               outline='gray', tag='button_rec')
                            self.frame.canvas.update()
                            break
        
                    time.sleep(0.4)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()
                    
            elif self.sti_type=='text':
                
                if self.N == 1:
                    self.frame.canvas.create_rectangle(self.w / 2 - 80, self.h / 2 - 18, self.w / 2 + 80, self.h / 2 + 18,
                                                       fill='gray', outline='gray', tag='button_rec')
                    self.frame.canvas.update()
                    time.sleep(0.4)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()
                
                
                else:
                    for item in range(self.N):
                        if i[1]['text']==text_list[item]:
                            self.frame.canvas.create_rectangle(self.w/(self.N+1)*item+30,self.h/2-18,self.w/(self.N+1)*item+150,self.h/2+18,fill='gray',outline='gray',tag='button_rec')
                            self.frame.canvas.update()
                            break
                    time.sleep(0.4)
                    self.frame.canvas.delete('button_rec')
                    self.frame.canvas.update()
                        
if'Count' in task_info_dic.values():
    class Reaction_count:
    
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))           
        
        frame.canvas.create_text(w/2,h/4,text='Current count: ',font=("Times New Roman",18))
    
        frame.canvas.create_text(w/6*5,20,text='trial #: ',font=("Times New Roman",15))
    
        def show(self,start_num,end_num):
            self.frame.canvas.create_text(100,20,text='Count from %s to %s'%(start_num,end_num),font=("Times New Roman",18,"bold"),tag='count')
    
        def count_num (self,current):
            
            self.frame.canvas.create_text(self.w/2,self.h/2,text=str(current),font=("Times New Roman",18),fill='red',tag='current_count')
            self.frame.canvas.update()
            time.sleep(0.1)
            self.frame.canvas.delete('current_count')
        
        def trial(self,trial):
            self.frame.canvas.create_text(self.w/8*7,20,text=trial,font=("Times New Roman",15),tag='trial')
            self.frame.canvas.update()
            #time.sleep(0.1)
            #self.frame.canvas.delete('trial')
            
        def delete(self):
            self.frame.canvas.delete('trial')
            self.frame.canvas.delete('count') 
            
if 'Cal_single_digit_num' in task_info_dic.values():
    class Reaction_calsingledig:
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/5
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))    
        
        from gui_basic_BE import operation

        if operation=='Add (+)':
            text='+'
        elif operation=='Subtract (-)':
            text='-'
        elif operation=='Multiplication (*)':
            text='*'
        else:
            text='/'
        frame.canvas.create_text(w/2,h/2,text=text,font=("Times New Roman",18,"bold"))
            #frame.canvas.create_text(w/2,h/4,text='Current count: ',font=("Times New Roman",18))  
        
        def first_num(self,first_num):
            self.frame.canvas.create_text(self.w/2-20,self.h/2,text=str(first_num),font=("Times New Roman",18),fill='red',tag='first_num')
            self.frame.canvas.update()
        
        def second_num(self,second_num):
            self.frame.canvas.create_text(self.w/2+20,self.h/2,text=str(second_num),font=("Times New Roman",18),fill='blue',tag='second_num')
            self.frame.canvas.update()
            
        def result(self,i):
            
            self.frame.canvas.create_text(self.w/2+60,self.h/2,text=' = '+str(i),font=("Times New Roman",18),tag='result')
            self.frame.canvas.update()
            time.sleep(0.2)
            
        def delete(self):

            self.frame.canvas.delete('first_num')

            self.frame.canvas.delete('second_num')

            self.frame.canvas.delete('result')

if 'Look_at' in task_info_dic.values() or 'Look_for' in task_info_dic.values():
    class Reaction_general:
        root = tk.Tk()
        w=root.winfo_screenwidth()/2
        h=root.winfo_screenheight()/3
        frame=myCanvas(root,w,h)
        frame.canvas.pack(fill="both",expand=True)
        root.title('Reaction')
        root.geometry('%dx%d+%d+%d'%(w,h,0,root.winfo_screenheight()/1.7))  
        max_value = max(max(t[0]) for t in look_for_ls if isinstance(t[0], tuple))
        rows, cols = max_value+1,max_value+1
        cell_width, cell_height = h // cols, h // rows
    
        
        
        def judge_result(self,judge,result):
            
            if result=='T':
                if judge=='color':
                    self.frame.canvas.create_text(self.cell_width*self.rows+80,self.h/2,anchor='center',text='identical color',font=("Times New Roman",15,"bold"),tag='ji_text')
                elif judge=='text' :
                    self.frame.canvas.create_text(self.cell_width*self.rows+80,self.h/2,anchor='center',text='identical text',font=("Times New Roman",15,"bold"),tag='ji_text')
            elif result=='F':
                if judge=='color':
                    self.frame.canvas.create_text(self.cell_width*self.rows+80,self.h/2,anchor='center',text='different color',font=("Times New Roman",15,"bold"),tag='ji_text')
                elif judge=='text':
                    self.frame.canvas.create_text(self.cell_width*self.rows+80,self.h/2,anchor='center',text='different text',font=("Times New Roman",15,"bold"),tag='ji_text')
            self.frame.canvas.update()
            time.sleep(1)
            self.frame.canvas.delete('ji_rec')
            self.frame.canvas.delete('ji_text')
            self.frame.canvas.update()
            
        def look_at(self):
            self.draw_table(self.rows, self.cols, self.cell_width, self.cell_height)  
            self.draw_circles(look_for_ls, self.cell_width, self.cell_height)
        
        def show_eye(self,row,column,radius=15):
            # Draw the circle
            x_center = (column + 0.5) * self.cell_width
            y_center = (row + 0.5) * self.cell_height
            self.frame.canvas.create_oval(x_center-radius, y_center-radius, x_center+radius, y_center+radius,outline='red',width=2,fil=None,tag='eye')
            self.frame.canvas.update()      
        
        def delete(self):
            self.canvas.delete('eye')
                
        def draw_table(self, rows, cols, cell_width, cell_height):
            # Draw table grid
            for i in range(rows + 1):
                self.frame.canvas.create_line(0, i * cell_height, cols * cell_width, i * cell_height)
            for i in range(cols + 1):
                self.frame.canvas.create_line(i * cell_width, 0, i * cell_width, rows * cell_height)
            
            # Draw row numbers in the first column
            for i in range(1, rows):
                self.frame.canvas.create_text(self.cell_width / 2, (i + 0.5) * cell_height, 
                                              text=str(i), font=('Arial', 10))
    
            # Draw column numbers in the first row
            for i in range(1, cols):
                self.frame.canvas.create_text((i + 0.5) * cell_width, self.cell_height / 2, 
                                              text=str(i), font=('Arial', 10))
    
            # Label for the first cell
            self.frame.canvas.create_text(self.cell_width / 2, self.cell_height / 2,
                                          text='Row/Column', font=('Arial', 10))

        def draw_circles(self, look_for_ls, cell_width, cell_height):
            radius = 10
            for (row, col), text, color in look_for_ls:
                # Calculate center of the cell
                x_center = (col + 0.5) * cell_width
                y_center = (row + 0.5) * cell_height
                
                # Draw circle
                self.frame.canvas.create_oval(x_center - radius, y_center - radius, 
                                              x_center + radius, y_center + radius, 
                                              fill=color)
                # Draw text
                self.frame.canvas.create_text(x_center, y_center, text=text, fill="black")
                self.frame.canvas.update()
                
                
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utility import max_val_click

class Reaction_click:
    
    def __init__(self, dimension):
        self.dimension = dimension
        
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand="yes")
        self.points = []  # List to store multiple points
        if self.dimension == 1:
            self.root.title("1D Visualization")
            self.fig, self.ax = plt.subplots(figsize=(12, 6))

            # Generate x values from 0 to max_click
            x_vals = list(range(0, max_val_click + 1))
            y_vals = [0 for _ in x_vals]

            self.ax.set_yticks([])  # Remove y-axis ticks for 1D
            self.ax.set_xticks(range(0, max_val_click + 1, 10))  # Set x ticks from 0 to max_click
            self.ax.set_xlim(0, max_val_click)  # Set x-axis limits from 0 to max_click
            
            # Add trial number as a label in the upper-right corner of the plot
            self.trial_label = self.ax.text(0.95, 0.95,'Trial: ', \
                                            transform=self.ax.transAxes, fontsize=12,\
                                                verticalalignment='top', horizontalalignment='right')
            #Add labels for the color of initial position and click position
            self.blue_label = self.ax.text(0.05, 0.05,'Blue: Initial Position', \
                                            transform=self.ax.transAxes, fontsize=12,color='blue',\
                                                verticalalignment='top', horizontalalignment='left')
            self.red_label = self.ax.text(0.05, 0.1,'Red: Click Position', \
                                            transform=self.ax.transAxes, fontsize=12,color='red',\
                                                verticalalignment='top', horizontalalignment='left')
        
        elif self.dimension == 2:
            self.root.title("2D Visualization")
            self.fig, self.ax = plt.subplots(figsize=(10, 10))
            # Update position for 2D scatter
            # Generate x values from 0 to max_click
            x_vals = list(range(0, max_val_click + 1))
            y_vals = list(range(0, max_val_click + 1))
            self.ax.set_xticks(range(0, max_val_click + 1, 10))  # Set x ticks from 0 to max_click
            self.ax.set_xlim(0, max_val_click)  # Set x-axis limits from 0 to max_click
            self.ax.set_yticks(range(0, max_val_click + 1, 10))  # Set x ticks from 0 to max_click
            self.ax.set_ylim(0, max_val_click)  # Set x-axis limits from 0 to max_click
        
            # Add trial number as a label in the upper-right corner of the plot
            self.trial_label = self.ax.text(0.95, 0.95,'Trial: ', \
                                            transform=self.ax.transAxes, fontsize=12,\
                                                verticalalignment='top', horizontalalignment='right')
            #Add labels for the color of initial position and click position
            self.blue_label = self.ax.text(0.05, 0.05,'Blue: Initial Position', \
                                            transform=self.ax.transAxes, fontsize=12,color='blue',\
                                                verticalalignment='top', horizontalalignment='left')
            self.red_label = self.ax.text(0.05, 0.1,'Red: Click Position', \
                                            transform=self.ax.transAxes, fontsize=12,color='red',\
                                                verticalalignment='top', horizontalalignment='left')
        
        elif self.dimension == 3:
            self.root.title("3D Visualization")
            self.fig = plt.figure(figsize=(10, 10))
            self.ax = self.fig.add_subplot(111, projection='3d')
            x_vals = list(range(0, max_val_click + 1))
            y_vals = list(range(0, max_val_click + 1))
            z_vals = list(range(0, max_val_click + 1))
            self.ax.set_xticks(range(0, max_val_click + 1, 10))  # Set x ticks from 0 to max_click
            self.ax.set_xlim(0, max_val_click)  # Set x-axis limits from 0 to max_click
            self.ax.set_yticks(range(0, max_val_click + 1, 10))  # Set y ticks from 0 to max_click
            self.ax.set_ylim(0, max_val_click)  # Set y-axis limits from 0 to max_click
            self.ax.set_zticks(range(0, max_val_click + 1, 10))  # Set z ticks from 0 to max_click
            self.ax.set_zlim(0, max_val_click)  # Set z-axis limits from 0 to max_click

            # Add trial number as a label in the upper-right corner of the plot
            self.trial_label = self.ax.text2D(0.95, 0.95, 'Trial: ', \
                                            transform=self.ax.transAxes, fontsize=12,\
                                                verticalalignment='top', horizontalalignment='right')
            
            #Add labels for the color of initial position and click position
            self.blue_label = self.ax.text2D(0.05, 0.05,'Blue: Initial Position', \
                                            transform=self.ax.transAxes, fontsize=12,color = 'blue',\
                                                verticalalignment='top', horizontalalignment='left')
            self.red_label = self.ax.text2D(0.05, 0.1,'Red: Click Position', \
                                            transform=self.ax.transAxes, fontsize=12,color = 'red',\
                                                verticalalignment='top', horizontalalignment='left')
        # Embed the matplotlib plot into the Tkinter frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
       

    def create_initial_point(self,coords,trial_number):
        
        self.target_x = coords[0]
        self.cursor_x = coords[1]
        self.target_y = coords[2]
        self.cursor_y = coords[3]
        self.target_z = coords[4]
        self.cursor_z = coords[5]
        #update trial label
        self.trial_label.set_text(f'Trial: {trial_number}')
        # Plot the cursor point in 1D
        # Create the initial point and store it in the points list
        if self.dimension == 1:
            point = self.ax.scatter(self.cursor_x, 0, c='blue', s=100)
        elif self.dimension == 2:
            point = self.ax.scatter(self.cursor_x, self.cursor_y, c='blue', s=100)
        elif self.dimension == 3:
            point = self.ax.scatter(self.cursor_x, self.cursor_y,self.cursor_z, c='blue', s=100)
        self.points.append(point)  # Store point in the list
        self.canvas.draw()  # Redraw the figure
        self.root.update()
        time.sleep(0.3)

  
    def move_point(self):
        """Move the point to a new position based on the given coordinates."""
       
        if self.dimension == 1:
            # Update cursor position for 1D
            # Re-plot the point at the new position
            # Create the initial point and store it in the points list
            target_point = self.ax.scatter(self.target_x, 0, c='red', s=100)
        elif self.dimension == 2:
            target_point = self.ax.scatter(self.target_x, self.target_y, c='red', s=100)
        elif self.dimension == 3:
            target_point = self.ax.scatter(self.target_x, self.target_y,self.target_z, c='red', s=100)
        
        self.points.append(target_point)  # Store point in the list
        #self.ax.set_xlim(0, max_val_click)  # Optional: adjust limits if needed
        self.canvas.draw()  # Redraw the figure
        self.root.update()
        time.sleep(0.3)
        
        
    def delete_point(self):
        for point in self.points:
            point.remove()  # Remove each point from the canvas
        self.points.clear()  # Clear the list of points
        self.canvas.draw()
        self.root.update()
        time.sleep(0.3)

"""
Created on Tue Aug  6 13:23:02 2024

@author: wyuanc
"""

"""Main entry point for running the QN-MHP simulation.

Usage:
    python run_code.py

The script launches the GUI, builds the SimPy model, runs the selected tasks
"""




import simpy
import gui_general
import utility
from utility import save_user_input as save
from utility import attribute_dic,tracktrace_name
import numpy as np



import sys
import os
from datetime import datetime
import atexit

# ----------------------------------------------------------------------
# Tee class:
# Redirects all standard output (print statements) to both:
# 1) Console (terminal)
# 2) Log file
# ----------------------------------------------------------------------
class Tee:
    def __init__(self, filename):
        # Open log file with UTF-8 encoding
        self.file = open(filename, "w", encoding="utf-8")
        self.stdout = sys.stdout  # Original console output

    def write(self, message):
        # Write to both file and console
        self.file.write(message)
        self.stdout.write(message)
        self.file.flush()  # Ensure real-time logging (important for simulation)

    def flush(self):
        # Required for compatibility with sys.stdout
        self.file.flush()
        self.stdout.flush()


# ----------------------------------------------------------------------
# Create log directory if it does not exist
# ----------------------------------------------------------------------
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# ----------------------------------------------------------------------
# Generate a timestamped log filename
# Example: log_20260328_154233.txt
# ----------------------------------------------------------------------
log_file = os.path.join(
    log_dir,
    f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
)

# ----------------------------------------------------------------------
# Redirect all print() output to both console and file
# ----------------------------------------------------------------------
sys.stdout = Tee(log_file)


# ----------------------------------------------------------------------
# Ensure log file is properly closed when the program exits
# ----------------------------------------------------------------------
def close_log():
    sys.stdout.file.close()

atexit.register(close_log)


# ----------------------------------------------------------------------
# Optional: Mark the start of simulation (useful for experiment tracking)
# ----------------------------------------------------------------------
print("===== Simulation Started =====")




env = simpy.Environment()
gui_general.run()

#Run GUI


from gui_general import task_info_dic,Tasklist_dic,SIMTIME,anim,entity_dic,entity_dic_hear,entity_dic_see


from entity_basic_BE import entity_generation as gen_basic
from entity_compound_BE import entity_generation as gen_comp

from model import QN_MHP
qnmhp = QN_MHP(env)


#run model
#ignition of entity generation accorcing to user input data

class ModelRun:
    
    def entity(self):
        """
        Process entities based on the Tasklist_dic and run the appropriate simulation.
        """
        for no in Tasklist_dic:
            self.process_task(no)
        if entity_dic_see!={} or entity_dic_hear!={}:
            self.process_entity_data(entity_dic_see)
            self.process_entity_data(entity_dic_hear)

    def process_task(self, no):
        """
        Process a compound BE based on its identifier.

        """
        task_types = {
            'Look_for': lambda: env.process(gen_comp().Look_for_en(env, qnmhp, no)),
            'Tracking_1D': lambda: self.track_1d(no),
            'Tracking_1D_1W': lambda: self.track_1d(no),
            'Tracking_1D_Random': lambda: self.track_1d(no),
            'Tracking_2D': lambda: self.track_2d(no),
            'Tracking_2D_Random': lambda: self.track_2d(no),
            'Tracking_2D_1W': lambda: self.track_2d(no),
            'Tracing_1D_Bounded': lambda: self.tracing_1d_bounded(no),
            'Tracing_1D_1W': lambda: self.tracing_1d_1w(no),
            'Tracing_2D_Bounded': lambda: self.tracing_2d_bounded(no),
            'Tracing_2D_1W': lambda: self.tracing_2d_1w(no)
        }

        for task_type, action in task_types.items():
            if [task_type] in Tasklist_dic[no]:
                action()
                break

    def track_1d(self, no):
        """
        Process 1D tracking.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().track1D_en(env, qnmhp, no))
        
    def track_2d(self, no):
        """
        Process 2D tracking.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().track2D_en(env, qnmhp, no))

    def tracing_1d_bounded(self, no):
        """
        Process 1D bounded tracing.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().tracing1D_b_en(env, qnmhp, no))

    def tracing_1d_1w(self, no):
        """
        Process 1D tracing with one way.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().tracing1D_1w_en(env, qnmhp, no))

    def tracing_2d_bounded(self, no):
        """
        Process 2D bounded tracing.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().tracing2D_b_en(env, qnmhp, no))

    def tracing_2d_1w(self, no):
        """
        Process 2D tracing with one way.

        Args:
        - no: Identifier for the task to process.
        """
        start_time = env.now
        env.process(gen_comp().tracing2D_1w_en(env, qnmhp, no))

    def process_entity_data(self, entity_dict):
        """
        Process entities (see or hear) based on their characteristics.

        Args:
        - entity_dict: Dictionary of entities to process.
        """
        if entity_dict==entity_dic_see:
            entity_source='see'
        else:
            entity_source='hear'
        if entity_dict:
            for (r, c, no) in entity_dict:
                if entity_dict[(r, c, no)]!='':
                    entity_value = entity_dict[(r, c, no)] 
                    fa = eval(entity_dict[(r, 2, no)])
                    iat = eval(entity_dict[(r, 3, no)])
                    occur = eval(entity_dict[(r, 4, no)])
                    k_ = no
                    if entity_value == 'Color':
                        env.process(gen_basic().color_en(env, qnmhp, k_, fa=fa, iat=iat, occur=occur,seeorhear=entity_source))
                    elif entity_value == 'Text':
                        env.process(gen_basic().text_en(env, qnmhp, k_, fa=fa, iat=iat, occur=occur,seeorhear=entity_source))

    def print_departure_summary(self):
        """Print departure logs before any final GUI window is closed."""
        print("\nBehavior element departure summary")
        print(utility.format_departure_be_table(utility.departure_BE_N))
        print("\nServer departure summary")
        print(utility.format_departure_server_table(utility.departure_server_N))

    def run(self):
        """
        Run the simulation and handle animations and plotting.
        """
        self.entity()
        env.run(until=SIMTIME)  # Running time

        if anim == 1:
            import qn_mhp_layout
            layout = qn_mhp_layout.Structure()
            layout.background()
        
        from plot import Plot
        
        """
        Check for tracking or tracing tasks and plot the corresponding graphs.
        """
        track_trace_task = any(any(task in Tasklist_dic[task_no] for task in [[item]]) for task_no in Tasklist_dic for item in tracktrace_name)

        if track_trace_task:
            a = Plot()
            a.RMSE()
            if len(Tasklist_dic) != 1:
                b = Plot()
                b.tick()
        else:
            Plot().tick()

        self.print_departure_summary()

        if anim == 1:
            layout.root.mainloop()



# Initialize reaction if certain tasks are present
if 'Look_at' in task_info_dic.values() or 'Look_for' in task_info_dic.values():
    from display_basic_BE import Reaction_general
    Reaction_general().look_at()
    


# Run the model
ModelRun().run()
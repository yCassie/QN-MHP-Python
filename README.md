# QN-MHP Software README

## More detailed information can be found in “QN-MHP Python Work Instruction.pdf.”


## 1. Overview
Queueing Network Model Human Processor (QN-MHP) represents human information processing as a queueing network in which entities are processed by different servers, similar to how signals travel through the brain and are handled by different functional units. QN-MHP can be used to evaluate human performance, such as reaction time, and accuracy, during single-task and multitasking situations.

This repository implements a GUI-driven QN-MHP simulation environment built with Python, Tkinter, SimPy, and Matplotlib. The software lets a user define tasks, configure behavior elements (BEs), generate visual or auditory entities, run a simulation in SimPy time, and inspect outputs such as sojourn-time plots and optional animation windows.

The codebase supports two broad classes of behaviors:
- **Basic Behavioral Elements (Basic BEs)** such as `See`, `Hear`, `Store_to_WM`, `Choice`, `Judge_identity`, `Judge_relative_location`, `Count`, `Cal_single_digit_num`, `Press_button`, `Mouse_click`, and `Look_at`. They are the fundamental elements required to complete a task.

- **Compound Behavioral Elements (Compound BEs)** such as `Look_for`, several tracking tasks, and several tracing tasks. Compound BEs coordinate multiple lower-level Basic BEs.

## 2. Core runtime idea
The software follows this high-level flow:
1. Launch the main GUI from `run_code.py`.
2. Define task numbers and BE order in the task-definition window.
3. Define entity streams and BE-specific parameters.
4. Define simulation time and whether animation is enabled.
5. Build the SimPy environment and QN-MHP resources.
6. Generate entities and dispatch them through the selected BE sequence.
7. Record sojourn time, RMSE, and departure logs.
8. Show plots and, when enabled, the animation/layout windows.

## 3. Quick start
1. Install the Python dependencies used by the codebase: `simpy`, `numpy`, `matplotlib`, `pyautogui`, and the standard-library modules already imported by the project.
2. Place all project files in the same working directory.
3. Run:
   ```bash
   python run_code.py
   ```
4. In the main menu:
   - Click **1. Define Task** to choose task count, BE names, and order.
   - Click **2. Define Entity and BE Parameters** to define entities and BE-specific settings.
   - Click **3. Define Simulation Parameters** to set total simulation time and animation on or off.
   - Click **Start** to begin the run.

## 4. Main user workflow
### Step 1 - Define tasks
The task-definition GUI in `gui_general.py` provides up to five tasks (current version supports up to 2 tasks running at the same time). For each task you select:
- the task number in row 1,
- the BE name in odd-numbered columns,
- the execution order in even-numbered columns.

The available BE list includes both basic and compound BEs.

### Step 2 - Define entities and BE parameters
The entity/parameter GUI shows one vertical column per task. What appears depends on the chosen BEs:
- If a task contains `See` and/or `Hear`, the top button opens the entity-definition window.
- BEs that require extra parameters become clickable buttons.
- BEs without user parameters appear as labels.

Entity definition lets you enter up to four rows of entities per task. Each row contains:
- entity type (`Color` or `Text`),
- first arrival time,
- IAT (interval arrival time),
- occurrences.

### Step 3 - Define simulation parameters
Set:
- **Simulation Time (msec)**
- **Animation** on/off

## 5. Parameter conventions
### Time
- All time in the simulation is **SimPy time in milliseconds**.
- Service times are sampled through `random_ppt()`, `random_cpt()`, and `random_mpt()` in `utility.py`.
- Plot labels such as sojourn time and RMSE are therefore based on the simulation clock, not wall-clock time.

### Coordinates
- Many task-specific windows use coordinates in a normalized range such as **0-100**.
- `Look_at` uses discrete table coordinates from **1-9** on x and y.
- `Mouse_click` supports 1D, 2D, and 3D display modes.
- Tracking/tracing windows convert plotted pixel positions to millimeters for internal calculations through `pixels_to_mm()`.

## 6. Basic BE summary
### `See`
Processes visual entities. In animation mode it routes a visual signal through perceptual servers 1, 2, 3, and 4, then to memory-related servers depending on the information type.

### `Hear`
Processes auditory entities through the auditory pathway and records departures similarly to `See`, but using auditory assumptions.

### `Store_to_WM`
Stores selected entity information into working-memory structures.

### `Choice`
Makes a selection among alternatives. It is reused directly by some compound tasks to choose a corrective action or response.

### `Judge_identity`
Compares the perceived entity with the user-defined target identity (text or color).

### `Judge_relative_location`
Compares target and cursor or point locations. Used heavily inside tracking/tracing tasks.

### `Count`
Counts over a configured length and visualizes the count progression in the reaction window.

### `Cal_single_digit_num`
Performs one of four arithmetic operations selected in the GUI: add, subtract, multiply, or divide.

### `Press_button`
Shows button-like stimuli and highlights the chosen option.

### `Mouse_click`
Displays a 1D, 2D, or 3D click-space visualization and records click positions.

### `Look_at`
Moves eye fixation to a discrete table location in the `Reaction_general` window.

## 7. Compound BE summary
### `Look_for`
Recursively performs a visual search. It repeatedly runs `Look_at -> See -> Judge_identity -> Store_to_WM` until the target is found or the configured search list is exhausted.

### Tracking tasks
- `Tracking_1D`
- `Tracking_1D_1W`
- `Tracking_1D_Random`
- `Tracking_2D`
- `Tracking_2D_Random`
- `Tracking_2D_1W`

These tasks display moving targets and a cursor, repeatedly perceive both target and cursor locations, judge their relative location, then respond through mouse click or keyboard press. RMSE is accumulated across responses.

### Tracing tasks
- `Tracing_1D_Bounded`
- `Tracing_1D_1W`
- `Tracing_2D_Bounded`
- `Tracing_2D_1W`

These tasks operate on point-tracing displays rather than target-cursor tracking displays. They use movement amplitude, direction, shape, and response settings.

## 8. File map
- `run_code.py` - entry point; starts GUI, builds model, runs simulation, and shows plots.
- `gui_general.py` - main menu, task-definition UI, entity-definition UI, simulation-parameter UI.
- `gui_basic_BE.py` - parameter windows for basic BEs.
- `gui_compound_BE.py` - parameter windows for compound BEs.
- `entity_basic_BE.py` - generators for color and text entities.
- `entity_compound_BE.py` - generators for compound tasks.
- `main_process.py` - dispatches each entity through the ordered BE list.
- `basic_BE.py` - implementations of all basic BEs.
- `compound_BE.py` - implementations of all compound BEs.
- `model.py` - SimPy resources and server service definitions.
- `animation_general.py` - canvas-based entity animation on the QN-MHP layout.
- `qn_mhp_layout.py` - background layout and canvas classes.
- `display_basic_BE.py` - reaction windows for button, counting, arithmetic, look-at, and click tasks.
- `display_compound_BE.py` - reaction windows for tracking and tracing tasks.
- `plot.py` - mean/SD sojourn plot and RMSE plot.
- `utility.py` - shared dictionaries, constants, persistence helpers, and utility functions.

## 9. Persistence and backup
The software writes configuration values into the `backup/` folder using pickle files. Important behavior:
- a fresh run resets the session folder through `reset_session_folder('backup/')`,
- **save as** copies the current `backup/` contents to a user-selected folder,
- **open** switches the active path to a selected folder and loads saved settings from there.

## 10. Outputs
Typical outputs include:
- `task_info_dic.txt`, `simtime.txt`, `anim.txt`, and many task-specific parameter files in the active save folder,
- run-time print output in the console,
- sojourn-time mean and standard-deviation plots,
- RMSE plot for tracking/tracing tasks,
- departure summaries for behavior elements and servers.

## 11. Important implementation notes
- The software mixes GUI state, global variables, and file-backed dictionaries. Saving parameters is therefore part of the normal workflow.
- Several windows create conditional classes only when the relevant task exists in `task_info_dic`.
- `Look_for` uses the predefined `look_for_ls` item list in `utility.py`.
- Tracking and tracing shapes are generated by helper functions in `utility.py` and the display classes in `display_compound_BE.py`.

## 12. Recommended usage notes
- Define tasks first. The entity and parameter windows assume task structure already exists.
- Save task and entity settings before closing windows.
- When debugging, keep animation enabled only when needed; it opens multiple windows and slows execution.
- For repeatable studies, keep a dedicated save folder for each experiment condition.

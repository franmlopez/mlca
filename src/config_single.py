from math import pi, sin, cos

# Parameters for single configuration to be simulated
num_simulations = 100   # number of simulations 
S_cue_1, S_cue_2 = 1, 0                         # cue components
S_motion_1, S_motion_2 = cos(pi/6), sin(pi/6) # motion components
S_color_1, S_color_2 = cos(pi/6), sin(pi/6)     # color components

# General parameters
dt = .1                 # integration step
total_time = 100        # total time of integration
tau = 1                 # time normalization
th = 10                 # threshold boundary
std = .5                # gaussian noise
alpha = .1              # leakage
beta = .1               # lateral inhibition
eta, eta2    = 1, .25   # learning rates
S_cue_motion_1, S_cue_motion_2 = 1, 0               # motion cues components
S_cue_color_1, S_cue_color_2 = 0, 1                 # color cues components
S_motion_L_1, S_motion_L_2 = cos(pi/6), sin(pi/6)   # motion left components
S_motion_R_1, S_motion_R_2 = sin(pi/6), cos(pi/6)   # motion right components
S_color_g_1, S_color_g_2 = cos(pi/6), sin(pi/6)     # color green components
S_color_r_1, S_color_r_2 = sin(pi/6), cos(pi/6)     # color red components
from math import pi, sin, cos

# Parameters for different configurations to be simulated
num_simulations = 1000       # number of simulations
num_cues = 2                # number of cues
num_motion_coherences = 6   # number of motion coherences
num_color_coherences = 6    # number of color coherences
S_cue_1_min, S_cue_2_min = 1, 0     # cue components
S_cue_1_max, S_cue_2_max = 0, 1     # cue components
S_motion_1_min, S_motion_2_min = 0.9428, 0.3333    # motion components
S_motion_1_max, S_motion_2_max = 0.3333, 0.9428    # motion components
S_color_1_min, S_color_2_min = 0.9129, 0.4082      # color components
S_color_1_max, S_color_2_max = 0.4082, 0.9129      # color components

# General parameters
dt = .1                 # integration step
total_time = 100        # total time of integration
tau = 1                 # time normalization
th = 10                 # threshold boundary
std = .5                # gaussian noise
alpha = .1              # leakage
beta = .1               # lateral inhibition
eta, eta2    = 1, .8   # learning rates
S_cue_motion_1, S_cue_motion_2 = 1, 0         # motion cues components
S_cue_color_1, S_cue_color_2 = 0, 1           # color cues components
S_motion_L_1, S_motion_L_2 = 0.9428, 0.3333   # motion left components
S_motion_R_1, S_motion_R_2 = 0.3333, 0.9428   # motion right components
S_color_g_1, S_color_g_2 = 0.9129, 0.4082     # color green components
S_color_r_1, S_color_r_2 = 0.4082, 0.9129     # color red components
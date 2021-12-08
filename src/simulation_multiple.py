import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import gmtime, strftime
import os

from model import mlca
from plots import plot_psychometric_curves, plot_response_histograms, plot_response_time_distributions
from config_multiple import *


def main():

    results_dir = '../results/simulation_multiple_' + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + '/'
    os.mkdir(results_dir)

    S_cue_motion = np.array([[S_cue_motion_1, S_cue_motion_2]])
    S_cue_color  = np.array([[S_cue_color_1, S_cue_color_2]])
    S_motion_L   = np.array([[S_motion_L_1, S_motion_L_2]])
    S_motion_R   = np.array([[S_motion_R_1, S_motion_R_2]])
    S_color_g    = np.array([[S_color_g_1, S_color_g_2]])
    S_color_r    = np.array([[S_color_r_1, S_color_r_2]])

    M = np.kron(S_cue_motion, np.array([eta*np.kron(S_motion_L,S_color_g) + eta2*np.kron(S_motion_L,S_color_r), 
                                    eta*np.kron(S_motion_R,S_color_r) + eta2*np.kron(S_motion_R,S_color_g)])) \
        + np.kron(S_cue_color,  np.array([eta*np.kron(S_motion_L,S_color_g) + eta2*np.kron(S_motion_R,S_color_g),
                                   eta*np.kron(S_motion_R,S_color_r) + eta2*np.kron(S_motion_L,S_color_r)]))  

    A = np.array([[-alpha, -beta], [-beta, -alpha]])
    
    df_results = pd.DataFrame([], columns=['cue','motion','color','choice','rt'])

    for cue_idx in range(num_cues):
        print("Simulating cue number {}".format(cue_idx+1))
        S_cue = np.array([[
            np.linspace(S_cue_1_min, S_cue_1_max, num_cues)[cue_idx],
            np.linspace(S_cue_2_min, S_cue_2_max, num_cues)[cue_idx],
        ]])
        
        for motion_coherence_idx in range(num_motion_coherences):
            print("\t Simulating motion coherence number {}".format(motion_coherence_idx+1))
            S_motion = np.array([[
                np.linspace(S_motion_1_min, S_motion_1_max, num_motion_coherences)[motion_coherence_idx],
                np.linspace(S_motion_2_min, S_motion_2_max, num_motion_coherences)[motion_coherence_idx],
            ]])

            for color_coherence_idx in range(num_color_coherences):
                print("\t\t Simulating color coherence number {}".format(color_coherence_idx+1))
                S_color = np.array([[
                    np.linspace(S_color_1_min, S_color_1_max, num_color_coherences)[color_coherence_idx],
                    np.linspace(S_color_2_min, S_color_2_max, num_color_coherences)[color_coherence_idx],
                ]])

                for _ in range(num_simulations):
                    time, X = mlca(M, S_cue, S_motion, S_color, A, dt=dt, total_time=total_time, tau=tau, th=th, std=std)
                    choice = ('right' if X[-1,1] > X[-1,0] else 'left')
                    df_results.loc[len(df_results)] = [str(S_cue[0]), str(S_motion[0]), str(S_color[0]), choice, time[-1]]

        print("Plotting...")
        plot_response_histograms(df_results, str(S_cue[0]), results_dir+'simulation_multiple')
        plot_response_time_distributions(df_results, str(S_cue[0]), results_dir+'simulation_multiple')
        plot_psychometric_curves(df_results, str(S_cue[0]), num_simulations, results_dir+'simulation_multiple')
                        
    df_results.to_csv(results_dir + 'simulation_multiple.csv')


if __name__ == '__main__' :
    main()


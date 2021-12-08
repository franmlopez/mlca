import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import gmtime, strftime
import os

from model import mlca
from config_single import *

def main():

    results_dir = '../results/simulation_single_' + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + '/'
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

    S_cue = np.array([[S_cue_1, S_cue_2]])
    S_motion = np.array([[S_motion_1, S_motion_2]])
    S_color = np.array([[S_color_1, S_color_2]])
    
    df_results = pd.DataFrame([], columns=['cue','motion','color','choice','rt'])
    fig,ax = plt.subplots(figsize=(10,6))

    for _ in range(num_simulations):

            time, X = mlca(M, S_cue, S_motion, S_color, A, dt=dt, total_time=total_time, tau=tau, th=th, std=std)
            choice = ('right' if X[-1,1] > X[-1,0] else 'left')
            df_results.loc[len(df_results)] = [S_cue[0], S_motion[0], S_color[0], choice, time[-1]]
            ax.plot(time,X[:,0],'red', alpha=.2)
            ax.plot(time,X[:,1],'blue', alpha=.2)
            
    df_results.to_csv(results_dir + 'simulation_single.csv')
    ax.set_xlim(0,total_time)
    ax.set_ylim(0,th)
    ax.set_xlabel('Time')
    ax.set_ylabel('Accumulated evidence')
    ax.legend(['Response to left/green','Response to right/red'])
    fig.savefig(results_dir + 'simulation_single.png', dpi=fig.dpi)

    print('')
    print('Results for simulation with cue vector {}, motion vector {}, and color vector {}:'.format(S_cue[0], S_motion[0], S_color[0]))
    print('\t number of choices to left: {}/{}'.format(df_results[df_results.choice=='left'].choice.count(),num_simulations))
    print('\t response time mean: {}'.format(df_results.rt.mean()))
    print('\t response time std:  {}'.format(df_results.rt.std()))
    print('')

if __name__ == '__main__' :
    main()


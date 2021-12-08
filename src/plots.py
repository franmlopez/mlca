import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_response_histograms(df, cue, file_name_prefix):
    df = df[df.cue==cue]
    g = sns.catplot(data=df, x="choice", col="motion", row='color', 
                kind='count', height=2, margin_titles=True)
    fig = g.fig
    fig.savefig(file_name_prefix+'_'+cue+'_histograms.png', dpi=fig.dpi)


def plot_response_time_distributions(df, cue, file_name_prefix):
    df = df[df.cue==cue]
    g = sns.displot(data=df, x="rt", col="motion", row="color",
                kind='kde', height=2, facet_kws=dict(margin_titles=True, xlim=(0,80),),)
    fig = g.fig
    fig.savefig(file_name_prefix+'_'+cue+'_time_distributions.png', dpi=fig.dpi)


def plot_psychometric_curves(df, cue, num_simulations, file_name_prefix):

    df = df[df.cue==cue]

    # motion coherence
    fig,ax = plt.subplots(figsize=(6,6))
    num_x = df.motion.unique().size
    x = np.arange(num_x)
    y = df.groupby('motion').choice.apply(lambda x: (x=='left').sum()).tolist()
    ax.plot(x, y, 'ok', markersize=8)
    ax.set_ylim(-1, num_simulations*num_x+1)
    ax.set_xlabel('Motion coherence')
    ax.set_ylabel('Number of responses to left')
    ax.set_title(str(cue))
    fig.savefig(file_name_prefix+'_'+cue+'_motion_psychometric.png', dpi=fig.dpi)

    # color coherence
    fig,ax = plt.subplots(figsize=(6,6))
    num_x = df.color.unique().size
    x = np.arange(num_x)
    y = df.groupby('color').choice.apply(lambda x: (x=='left').sum()).tolist()
    ax.plot(x, y, 'ok', markersize=8)
    ax.set_ylim(-1, num_simulations*num_x+1)
    ax.set_xlabel('Color coherence')
    ax.set_ylabel('Number of responses to green')
    ax.set_title(cue)
    fig.savefig(file_name_prefix+'_'+cue+'_color_psychometric.png', dpi=fig.dpi)
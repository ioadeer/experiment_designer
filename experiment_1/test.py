import sys
import numpy as np
import os 
import datetime
import pandas as pd

def main():
    subject_n = 50
    audio_stimulus_n = 3
    audio_stimulus_repetitions = 5
    visual_stimulus_n = 5
    
    # Create audio stimulus counting from
    audio_stimulus = np.tile(np.arange(audio_stimulus_n), audio_stimulus_repetitions)
    visual_stimulus = np.arange(visual_stimulus_n)
    combination = np.array(np.meshgrid(audio_stimulus, visual_stimulus)).T.reshape(-1,2)
    np.random.shuffle(combination)
    df = pd.DataFrame(combination, columns= ['AudioStimulus','VisualStimulus'])
    #for subject in range(subject_n):
    #    df['subject'] = np.zeros(len(df)) + subject
    df['Subject'] = np.zeros(len(df)) + 1
    df['Subject'] = df['Subject'].astype(int)
    cols = df.columns.to_list()
    cols = cols[-1:] + cols[:-1] 
    df = df[cols]
    df['Response'] = '' 
    df['DateTimeOfResponse'] = ''
    df['ResponseTime'] = np.zeros(len(df))
    print(df)
    

if __name__ == '__main__':
    main() 
    sys.exit(0)

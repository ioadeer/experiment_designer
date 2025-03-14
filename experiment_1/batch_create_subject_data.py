# First 360 experiment

import sys
import numpy as np
import os 
import datetime
import pandas as pd
import yaml

def main():
    subject_n = 50
    audio_stimulus_n = 3
    audio_stimulus_repetitions = 5
    visual_stimulus_n = 5

    #config create folder to place DataFrame
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = 'output'
    if os.path.isdir(output_dir):
        print("output folder already exist...")
    else:
        os.mkdir(output_dir)
        print("Creating output dir...")

    try:
        os.chdir(output_dir)
    except Exception as err:
        print(err)

    folder_name  = date+'-'+str(subject_n)+'-participants'
    os.mkdir(folder_name)

    try:
        os.chdir(folder_name)
    except Exception as err:
        print(err)
        
    description_str = "In this experment subjects where exposed to 5 visual " \
                      " stimuli, consisting on 360 photos, and 3 audio stimuli. " \
                      " Each audio stimulus was repeated 5 times. " \
                      " 3 test trials added " \
                      " Total number of trials 5x3x5 + 3 = 78." \
                      " First all combination of stimuli where created using " \
                      " np.tile and np.meshgrid methods. " \
                      " Stimulus were randomized using np.random.shuffle method. " 
                        
    experiment_metadata= dict({
            "Experiment description": description_str,
            "Subjects N": str(subject_n),
            "Trail n": str(audio_stimulus_n*audio_stimulus_repetitions*visual_stimulus_n),
            "Date of creation": date,
            })

    with open('Experiment_Metadata.yaml','w') as output_file:
        yaml.dump(experiment_metadata,output_file,default_flow_style=False)


    # Create audio stimulus counting from
    audio_stimulus = np.tile(np.arange(audio_stimulus_n), audio_stimulus_repetitions)
    visual_stimulus = np.arange(visual_stimulus_n)
    combination = np.array(np.meshgrid(audio_stimulus, visual_stimulus)).T.reshape(-1,2)

    for subject in range(subject_n):
        # Random order
        np.random.shuffle(combination)
        # add
        # agregando 3 test trials
        # audio y visual no congruente
        # audio sala 3 2 1
        a = np.arange(2,-1,-1)
        # sala 1 3 5
        b = np.arange(0,6,2)
        t_trial = np.column_stack((a,b))
        df_test_trial = pd.DataFrame(t_trial, columns= ['AudioStimulus','VisualStimulus'])
        df_stimuli = pd.DataFrame(combination, columns= ['AudioStimulus','VisualStimulus'])
        df_stimuli = pd.concat([df_test_trial, df_stimuli], axis = 0, ignore_index= True)
        # subject number
        df = pd.DataFrame()
        df['Subject'] = np.zeros(len(df_stimuli)) + subject + 1
        df['Subject'] = df['Subject'].astype(int)
        df['TrialNumber'] = np.arange(1,len(df_stimuli)+1)
        df = pd.concat([df,df_stimuli], axis=1)
        # put first subject col
        df['Response'] = 'AddResponse' 
        df['DateTimeOfResponse'] = 'AddDate'
        df['ResponseTime'] = np.zeros(len(df))
        file_name = "Subject_"+f"{subject+1:03}" + ".csv"
        df.to_csv(file_name)

    

if __name__ == '__main__':
    main() 
    sys.exit(0)

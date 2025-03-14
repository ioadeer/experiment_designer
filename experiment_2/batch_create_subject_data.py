# Second 360 experiment

import sys
import itertools
from itertools import chain
import numpy as np
import os 
import datetime
import pandas as pd
import yaml

def main():
    subject_n = 50
    visual_stimulus_n = 20
    number_of_repetitions = 3

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
        
    description_str = "Second experiment. In this experiment we will compare" \
                      "different visual rooms for different percieved reverberantion." \
                      "we will use 5 360 images encompasing combinations" \
                      "AB AC AD AE BC BD BE CD CE DE" \
                      "BA BC BD BE AC AD AE CD CE DE" \
                      "Each series is repeated 3 times and randomized using" \
                      "np.random.shuffle from numpy"

    experiment_metadata= dict({
            "Experiment description": description_str,
            "Subjects N": str(subject_n),
            "Trail n": str(number_of_repetitions*visual_stimulus_n),
            "Date of creation": date,
            })

    with open('Experiment_Metadata.yaml','w') as output_file:
        yaml.dump(experiment_metadata,output_file,default_flow_style=False)

    # Create visual stimuli 
    list_a = list(chain.from_iterable(itertools.combinations('ABCDE', 2)))
    
    list_b = []
    for x in range(0,len(list_a)-1,2):
        list_b.append(list_a[x] + list_a[x+1])

    list_a_perm = list(chain.from_iterable(itertools.combinations('BACDE', 2)))

    list_b_perm = []
    for x in range(0,len(list_a_perm)-1,2):
        list_b_perm.append(list_a_perm[x] + list_a_perm[x+1])
    
    list_b = np.tile(list_b,3)
    list_b_perm = np.tile(list_b_perm,3)
    final = np.concatenate((list_b, list_b_perm), axis = 0 )

    for subject in range(subject_n):
        # agregando 3 test trials
        # sala AC, BD, CA
        t_trial = ['AC', 'BD', 'BA']
        df_test_trial = pd.DataFrame(t_trial, columns= ['Rooms'])
        # Randomize
        np.random.shuffle(final)
        df_stimuli = pd.DataFrame(final, columns= ['Rooms'])
        df_stimuli = pd.concat([df_test_trial, df_stimuli], axis = 0, ignore_index= True)
        ## subject number
        df = pd.DataFrame()
        df['Subject'] = np.zeros(len(df_stimuli)) + subject + 1
        df['Subject'] = df['Subject'].astype(int)
        df['TrialNumber'] = np.arange(1,len(df_stimuli)+1)
        df = pd.concat([df,df_stimuli], axis=1)
        ## put first subject col
        df['Response'] = 'AddResponse' 
        df['Confidence'] = 'AddConfidence'
        df['DateTimeOfResponse'] = 'AddDate'
        file_name = "Subject_"+f"{subject+1:03}" + ".csv"
        df.to_csv(file_name)

    

if __name__ == '__main__':
    main() 
    sys.exit(0)

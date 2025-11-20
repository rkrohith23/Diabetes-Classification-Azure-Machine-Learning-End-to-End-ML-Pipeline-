import pandas as pd

def azureml_main(dataframe1=None, dataframe2=None):
    if dataframe1 is None:
        return None  # Handle missing data gracefully
    
    # Selecting required columns
    scored_results = dataframe1[['PatientID', 'Scored Labels', 'Scored Probabilities']].copy()
    
    # Renaming columns for better readability
    scored_results.rename(columns={'Scored Labels': 'DiabetesPrediction',
                                   'Scored Probabilities': 'Probability'},
                          inplace=True)
    
    return scored_results

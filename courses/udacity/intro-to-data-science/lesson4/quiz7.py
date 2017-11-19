import pandas as pd

def filter_by_regular(filename):
    
    df = pd.read_csv(filename)
    turnstile_data = df.loc[df['DESCn'] == 'REGULAR']
    return turnstile_data
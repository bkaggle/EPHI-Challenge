import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)


if __name__=='__main__':
    path='C:/Users/user/Desktop/EPHI-Challenge/data/CHAMPS.csv'
    load_data(path)
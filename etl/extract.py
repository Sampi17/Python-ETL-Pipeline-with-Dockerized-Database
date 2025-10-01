import os
import pandas as pd

download_path = "raw"

# dateset information
default_dataset = 'saadharoon27/hr-analytics-dataset'
csv_filename = "HR_Analytics.csv"


def extract_data(dataset : str = default_dataset, download_path :str = download_path ) -> str:
    #downloading data-set form kaggle
    csv_path = os.path.join(download_path, csv_filename)
    csv = pd.read_csv(csv_path,sep=",")
    df = pd.DataFrame(csv)
    return df


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    data_file = pd.read_csv(path)
    return data_file

def data_visualization(data):

    plt.figure(figsize=(12, 6))

    sns.countplot(x='platform', hue='genre', data=data)

    plt.show()


if __name__ == "__main__":

    file_path = '../../dataset.csv'
    dataset = load_data(file_path)

    if dataset is not None:
        data_visualization(dataset)
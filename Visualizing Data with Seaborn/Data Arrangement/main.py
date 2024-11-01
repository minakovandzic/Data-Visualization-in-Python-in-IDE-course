import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    data_file = pd.read_csv(path)
    return data_file

def data_visualization(data):

    plt.figure(figsize=(12, 6))

    ordered_platforms = ['PS4', 'XOne', 'PC', 'WiiU']

    sorted_genres = sorted(data['genre'].unique())

    sns.countplot(x='platform', hue='genre', data=data, order=ordered_platforms, hue_order=sorted_genres)

    plt.show()

    return ordered_platforms, sorted_genres

if __name__ == "__main__":

    file_path = '../../dataset.csv'
    dataset = load_data(file_path)

    if dataset is not None:
        data_visualization(dataset)
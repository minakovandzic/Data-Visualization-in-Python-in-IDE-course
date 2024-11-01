import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    data_file = pd.read_csv(path)
    return data_file

def data_visualization(data):

    plt.figure(figsize=(12, 6))

    sns.set_style(style="darkgrid")

    ordered_platforms = ['PS4', 'XOne', 'PC', 'WiiU']

    sorted_genres = sorted(data['genre'].unique())

    sns.countplot(x='platform', hue='genre', data=data, order=ordered_platforms, hue_order=sorted_genres)

    legend = plt.legend(title='genre', loc='center left', bbox_to_anchor=(1, 0.5))

    legend.get_frame().set_facecolor('white')

    legend.get_frame().set_edgecolor('none')

    plt.tight_layout()

    plt.show()

if __name__ == "__main__":

    file_path = '../../dataset.csv'
    dataset = load_data(file_path)

    if dataset is not None:
        data_visualization(dataset)

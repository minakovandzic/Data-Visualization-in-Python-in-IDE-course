import pandas as pd

def load_data(path):

    data_file = pd.read_csv(path)

    print("Data loaded successfully.")
    return data_file

def explore_data(dataset):
    """
    Explore the dataset by printing the first 5 rows and info.
    Args:
        dataset (pd.DataFrame): The loaded dataset.
    """

    print(dataset.head())

    print(dataset.info())


if __name__ == "__main__":
    file_path = '../../dataset.csv'
    data = load_data(file_path)

    # If the data is successfully loaded, explore it
    if data is not None:
        explore_data(data)
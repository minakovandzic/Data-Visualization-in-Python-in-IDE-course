# Task 1 - Loading and Exploring Data

Before engaging in the process of plotting, 
it is *essential to load and explore the data thoroughly*. 

This foundational step helps to uncover underlying patterns and characteristics within the dataset,
ensuring that the visualizations created subsequently are accurate, relevant, and informative.

In this task, the focus is on loading data from a CSV file and performing basic exploration to understand the dataset. Using **Pandas**, we will load the data into a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), a powerful structure for organizing and analyzing tabular data.

**Load the CSV File**  
   Begin by loading the provided CSV file into a Pandas DataFrame. 
   Use the `read_csv()` function from the Pandas library to easily import data from the CSV file into a structured DataFrame, making it ready for exploration and analysis.

   ```
   import pandas as pd

   data_frame = pd.read_csv('dataset.csv')
   ```
   
**Explore the Dataset**

   Once the data is loaded, it is crucial to explore its contents to better understand the structure and quality of the dataset. You can use the following Pandas methods to get a quick overview:

- **[head()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head)**: Displays the first few rows of the dataset. This is useful to get a glimpse of the data and verify that it has been loaded correctly.

- **[info()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info)**: Provides a concise summary of the dataset, including the number of non-null values and data types of each column.

- **[describe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe)**: Generates summary statistics (like mean, median, standard deviation) for numerical columns in the dataset. This is helpful for quickly identifying trends or anomalies.


## Task

For this task, demonstrate your ability to load and explore a dataset.

1. Load the provided `dataset.csv` file using **Pandas**.
2. Display the first 5 rows of the dataset.
3. Display a summary of the dataset.

**Instructions:**
- To load a custom dataset, please ensure that the file is located in the same directory as your script, or provide the appropriate file path.
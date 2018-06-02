# Overwatch Ranked Data

## Background
I have been recording data from my ranked [Overwatch](http://playoverwatch.com/) matches for a number of seasons and the dataset can be found in this repo.

This originally started because I wanted to run some statistical models to understand my own gameplay better, which then turned into a series of [blog posts](https://www.simonho.ca/tag/overwatch/) on data visualization and statistics.

Feel free to use this dataset to create your own data visualizations, or conduct your own statistical analysis of the data.

I'll be updating this repo over time as I collect more data and/or run more analysis of the data.

## Data

The actual data files can be found in `/data`. Data for each season can be found in separate `.csv` files.

I have also aggregated all seasons into a single data file (`/data/all_seasons.csv`). The aggregation was done using a Python script (`combine_seasons.py`).

The dataset contains data from each of my ranked matches, with variables like my skill rating, enemy team skill rating, the role I played, individual performance metrics etc. A full explanation of all the variables can be found [here](https://www.simonho.ca/gaming/overwatch-ranked-data/).

![Overwatch data preview](https://www.simonho.ca/wp-content/uploads/2018/04/overwatch_data.png "Overwatch data preview")

## Data analysis

In `/analysis` you'll find the Jupyter notebooks I created for my analysis of the data.

I also uploaded this dataset to [Kaggle](https://www.kaggle.com/nem2k87/datasets), where you can find additional analyses by other users.

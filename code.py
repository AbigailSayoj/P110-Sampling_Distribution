import plotly.figure_factory as ff
import plotly.express as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")

data = df["responses"].tolist()

population_mean = statistics.mean(data)
print("Populaton mean:- ", population_mean)

#Function to get the mean of 30 samples
def ramndom_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

#Function to plot the mean on the graph.
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution:- ", mean)
    fig = ff.create_distplot([data], ["responses"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "MEAN"))
    fig.show()

#Function to repeat the process 100 times
def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean.list.append(set_of_means)

    std_deviation = statistics.stdev(data)
    print("Std_deviation:- ", std_deviation)

    show_fig(mean_list)
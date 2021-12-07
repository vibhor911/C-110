import csv
import plotly.express as px
import statistics
import math 
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

population_mean = statistics.mean(data)
print("Mean is-->",population_mean)
population_std = statistics.stdev(data)
print("Standard Deviation-->",population_std)

dataset=[]
for i in range (0,100):
    random_index=random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std = statistics.stdev(dataset)
print("Mean of 100 values-->", mean)
print("Standard Deviation of 100 values-->", std)

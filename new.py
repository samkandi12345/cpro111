import csv
import plotly.figure_factory as pff
import pandas as pd
import statistics 
import random
import plotly.graph_objects as pgo

df = pd.read_csv("marks.csv")
data = df["maths"].to_list()
mean = statistics.mean(data)
print(mean)
stdev = statistics.stdev(data)
print(stdev)

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,1000):
    setofmean = randomsetofmean(100)
    meanlist.append(setofmean)
mean2 = statistics.mean(meanlist)
print("sampling distribution: " , mean2)
std = statistics.stdev(meanlist)
print(std)


fstdstart , fstdend = mean2-std , mean2+std
sstdstart , sstdend = mean2-(2*std) , mean2+(2*std)
tstdstart , tstdend = mean2-(3*std) , mean2+(3*std)

df = pd.read_csv("data1.csv")
data = df["marks"].to_list()
mean = statistics.mean(data)
print("with tablets: " , mean)
stdev = statistics.stdev(data)
print("with tablets: " , stdev)
figure = pff.create_distplot([meanlist],["marks"],show_hist=False)

df = pd.read_csv("data2.csv")
data = df["marks"].to_list()
mean = statistics.mean(data)
print("with extra class: " , mean)
stdev = statistics.stdev(data)
print("with extra class: " , stdev)
figure = pff.create_distplot([meanlist],["marks"],show_hist=False)

df = pd.read_csv("data3.csv")
data = df["marks"].to_list()
mean = statistics.mean(data)
print("with fun worksheets: " , mean)
stdev = statistics.stdev(data)
print("with fun worksheets: " , stdev)
figure = pff.create_distplot([meanlist],["marks"],show_hist=False)


figure = pff.create_distplot([meanlist],["maths score"],show_hist=False)
figure.add_trace(pgo.Scatter(x=[mean2,mean2],y=[0,0.20],mode="lines",name="mean"))
figure.add_trace(pgo.Scatter(x=[fstdstart,fstdstart],y=[0,0.20],mode="lines",name="first"))
figure.add_trace(pgo.Scatter(x=[fstdend,fstdend],y=[0,0.20],mode="lines",name="first"))

figure.add_trace(pgo.Scatter(x=[sstdstart,sstdstart],y=[0,0.20],mode="lines",name="second"))
figure.add_trace(pgo.Scatter(x=[sstdend,sstdend],y=[0,0.20],mode="lines",name="second"))

figure.add_trace(pgo.Scatter(x=[tstdstart,tstdstart],y=[0,0.20],mode="lines",name="third"))
figure.add_trace(pgo.Scatter(x=[tstdend,tstdend],y=[0,0.20],mode="lines",name="third"))
figure.show()












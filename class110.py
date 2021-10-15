import plotly.figure_factory  as ff
import statistics
import random
import pandas as pd
import  csv
import plotly.graph_objects as go

df=pd.read_csv('class110/medium_data.csv')
data=df['temp'].tolist()
#population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data) 
#print("Population Mean: ",population_mean)


# fig=ff.create_distplot([data],['temp'],show_hist=False)
# fig.show()

def random_set_of_mean(counter):
    dataset=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['temp'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name='Mean'))
    fig.show()
    
    z_score=(mean_of_sample1-mean)/std_deviation

def setup():
    mean_list=[]

    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("Mean Of Sampling Distributions:-",mean)

setup()

population_mean=statistics.mean(data)
print("Population Mean:-",population_mean)


import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
math_score=df["math score"].to_list()

mean=sum(math_score)/len(math_score)
print("Mean:",str(mean))

median=statistics.median(math_score)
print("Median:",str(median))

mode=statistics.mode(math_score)
print("Mode:",str(mode))

std_deviation=statistics.stdev(math_score)
print("Standard Deviation:",str(std_deviation))

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation 
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)

list_of_data_within_1_std_deviation = [result for result in math_score if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in math_score if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in math_score if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation",format(len(list_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data lies within 2 standard deviations",format(len(list_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data lies within 3 standard deviations",format(len(list_of_data_within_3_std_deviation)*100.0/len(math_score)))
fig = ff.create_distplot([math_score],["Height"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.05], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()
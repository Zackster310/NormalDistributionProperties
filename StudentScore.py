import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

readingScore = df['reading score'].tolist()
mean = statistics.mean(readingScore)
median = statistics.median(readingScore)
mode = statistics.mode(readingScore)
stdDev = statistics.stdev(readingScore)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ", stdDev)

zone1S, zone1E = mean - stdDev, mean + stdDev
zone2S, zone2E = mean - (2 * stdDev), mean + (2 * stdDev)
zone3S, zone3E = mean - (3 * stdDev), mean + (3 * stdDev)

zone1List = [result for result in readingScore if result > zone1S and result < zone1E]
zone2List = [result for result in readingScore if result > zone2S and result < zone2E]
zone3List = [result for result in readingScore if result > zone3S and result < zone3E]

print("{}% of data for zone 1".format(len(zone1List)/len(readingScore) * 100))
print("{}% of data for zone 2".format(len(zone2List)/len(readingScore) * 100))
print("{}% of data for zone 3".format(len(zone3List)/len(readingScore) * 100))

fig = ff.create_distplot([readingScore], ["readingScore"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.05], mode = "lines", name = 'readingScoreMean'))

fig.add_trace(go.Scatter(x = [zone1S, zone1S], y = [0,0.05], mode = "lines", name = 'Zone 1 Start'))
fig.add_trace(go.Scatter(x = [zone1E, zone1E], y = [0,0.05], mode = "lines", name = 'Zone 1 End'))

fig.add_trace(go.Scatter(x = [zone2S, zone2S], y = [0,0.05], mode = "lines", name = 'Zone 2 Start'))
fig.add_trace(go.Scatter(x = [zone2E, zone2E], y = [0,0.05], mode = "lines", name = 'Zone 2 End'))

fig.add_trace(go.Scatter(x = [zone3S, zone3S], y = [0,0.05], mode = "lines", name = 'Zone 3 Start'))
fig.add_trace(go.Scatter(x = [zone3E, zone3E], y = [0,0.05], mode = "lines", name = 'Zone 3 End'))

fig.show()
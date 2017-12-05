
# multiple line-plots of evolution of paralell concepts in time 
# Line plots with time in X-axis and % of gorwth in Y-axis

import matplotlib.pyplot as plt 
import pandas as pd

# Read the data into a pandas DataFrame
data = pd.read_csv("/data")

# Define Tableau colors as RGB and scale to [0, 1] range for matplotlib format to be accepted
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
             
for i in range(len(tableau20)):
  r, g, b = tableau20[i]
  tableau20[i] = (r / 255., g / 255., b / 255.)

# Set the size of the plot as you wish it to be 
# Normally is ~1.33x wider than tall. Common sizes are (10, 7.5) and (12, 9) 
plt.figure(figsize=(12,14))


# Remove the plot frame lines. 
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)


# Ensure that the axis ticks only show up on the bottom and left of the plot
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

#Limit the range of the plot to only where the data is
# Avoid unnecessary whitespace
plt.ylim(0, 90) #-----> %
plt.xlim(1968, 2014) #------> dates

# Make sure your axis ticks are large enough to be asily read
plt.yticks(range(0,91,10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)
plt.xticks(fontsize=14)

# Provide tick lines across the plot to help your viewers 


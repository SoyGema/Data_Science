
# multiple line-plots of evolution of paralell concepts in time 
# Line plots with time in X-axis and % of gorwth in Y-axis

import matplotlib.pyplot as plt 
import pandas as pd

# Read the data into a pandas DataFrame
data = pd.read_csv("/data")

## -------- Probably this part could be ignored --------------------  ##
# Define Tableau colors as RGB and scale to [0, 1] range for matplotlib format to be accepted
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
             
for i in range(len(tableau20)):
  r, g, b = tableau20[i]
  tableau20[i] = (r / 255., g / 255., b / 255.)

## ----------------------------------------------------------------  ##
  
  
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
# trace along the axis. Configurate lines light and small so they don't obscure the primary data lines
for y in range(10, 91, 10):
  plt.plot(range(1968, 2012), [y] * len(range(1968, 2012)), "--
           ", lw=0.5, color="black", alpha=0.3)
           
# Remove the tick marks
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="off", right="off", labelleft="off")

# Now let's plot the data 
# Make a list ordering of the highest % in the final year . 
list = [ 'data_column_1' , 'data_column_2', 'data_column_3', 'data_column_4', 'data_column_5' ]


           
for rank, column in enumerate(list):
# Plot each line separately with its own color, using the Tableau20 color set order
           plt.plot(data.Year.values,
                    data[column.replace("/n", " ")].values,
                    lw=2.5, color=tableau20[rank])
           
# Add a text lable to the right end of every line.          
           y_pos = data[column.replace("/n", " ")].values[-1] - 0.5
           if column == "Data_column_1_name":
                y_pos += 0.5
           elif column == "Data_column_2_name":
                y_pos += 0.5
           elif column == "Data_column_3_name":
                y_pos += 0.25
           elif column == "Data_column_4_name":
                y_pos += 0.75
           elif column == "Data_column_5_name":
                y_pos += 1.25 

           # Again, make sure that all labels are large enough to be easily read 
           plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])
 
# Plot the text title
plt.text(1995, 93, " This is the title. Will appear in the top of the graph", fontsize=17, ha="center")
           
# Plot the references 
plt.text(1966, -8, "Here you can put the data source"
         "Authors : "
         "and notes : " , fontsize=10)

# Save the figure as PNG.
# You can also save it as PDF, JPEG.
plt.savefig("the_name_of_the_data.png", bbox_inches="tight")
           
## make it an interactive object with plotly (see again) 
import plotly.plotly as py
mpl_fig_obj = plt.figure()
py.plot_mpl(mpl_fig_obj)
           

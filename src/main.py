import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date, timedelta
import mplcursors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

data_dict = {}
year = 2021
start_date = date(year, 1, 1)
end_date = date(year + 1, 1, 1)
delta = timedelta(days=1)
SUNDAY = 6

# create nans for days in the previous year between the first day of the year and the first Sunday
prev_year = start_date
while prev_year.weekday() != SUNDAY:
    prev_year -= delta
    data_dict[prev_year.strftime('%y%m%d')] = np.nan
    
# fill data for the year
while start_date < end_date:
    data_dict[start_date.strftime('%y%m%d')] = random.randint(0, 3)
    start_date += delta

# create nans for days in the next year between the last day of the year and the last Sunday
next_year = end_date
while next_year.weekday() != SUNDAY:
    data_dict[next_year.strftime('%y%m%d')] = np.nan
    next_year += delta

# Convert the dictionary to a 2D list
data = [list(data_dict.values())[i:i+7] for i in range(0, len(data_dict), 7)]

# Transpose the data to switch the axes
data = np.array(list(map(list, zip(*data))), dtype=float)

# Get the shape of the data
num_rows, num_cols = data.shape


# Create the figure with a larger size
plt.figure(figsize=(num_cols/4, num_rows/3))

# Create the heatmap with padding between each square
ax = sns.heatmap(data, cmap='Blues', cbar=False, square=True, linewidths=0.1, linecolor='white')


# Set the y-axis labels to the days of the week and rotate them
plt.yticks(np.arange(data.shape[0]), ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], rotation=0)

# Add title to the graph
plt.title('Habit Tracker 2023')

# Add month labels to the x-axis
month_positions = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49, 52]
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(month_positions, month_labels, rotation=45, ha='right')

# Add padding
plt.tight_layout(pad=2.0)

plt.show()

# # Create the figure with size proportional to the data
# fig, ax = plt.subplots(figsize=(num_cols/2, num_rows/2))

# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)

# # Set aspect='auto' to adjust the aspect ratio based on the dimensions of the data
# im = ax.imshow(data, cmap='Blues', aspect='equal')

# # Add padding between squares
# for spine in ax.spines.values():
#     spine.set_visible(False)
# ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
# ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
# ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
# ax.tick_params(which="minor", bottom=False, left=False)

# # Hide the axes
# plt.axis('off')

# # Add hover functionality
# cursor = mplcursors.cursor(im, hover=True)
# cursor.connect("add", lambda sel: sel.annotation.set_text('Value: {}'.format(data[sel.index])))

# # Set the y-axis labels to the days of the week
# ax.set_yticks(np.arange(data.shape[0]))
# ax.set_yticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])

# # Add title to the graph
# ax.set_title('Habit Tracker 2023')

# # Add month labels to the x-axis
# month_positions = np.arange(0, 48, 4)  # Adjust the step size as needed
# month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ax.set_xticks(month_positions)
# ax.set_xticklabels(month_labels, rotation=45, ha='right')

# # Keep the number of weeks on the bottom of the graph
# ax.set_xticks(np.arange(data.shape[1]))

# plt.tight_layout()
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date, timedelta
import mplcursors
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Create a dictionary for the year 2023 with random values between 0 and 3
start_date = date(2023, 1, 1)
# Adjust the start date to the first Monday of the year
while start_date.weekday() != 0:
    start_date += timedelta(days=1)

end_date = date(2024, 1, 1)
delta = timedelta(days=1)

data_dict = {}
while start_date < end_date:
    data_dict[start_date.strftime('%y%m%d')] = random.randint(0, 3)
    start_date += delta

# Convert the dictionary to a 2D list
data = [list(data_dict.values())[i:i+7] for i in range(0, len(data_dict), 7)]

# Transpose the data to switch the axes
data = np.array(list(map(list, zip(*data))), dtype=float)


# TODO: remove later, testing making an element invisible
data[0, 0] = np.nan

# Get the shape of the data
num_rows, num_cols = data.shape

# Create the figure with size proportional to the data
fig, ax = plt.subplots(figsize=(num_cols, num_rows))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

# Set aspect='equal' to make the elements squares
im = ax.imshow(data, cmap='Blues', aspect='equal')

# Add padding between squares
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)

# Hide the axes
plt.axis('off')

# Add hover functionality
cursor = mplcursors.cursor(im, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text('Value: {}'.format(data[sel.index])))

# Set the y-axis labels to the days of the week
ax.set_yticks(np.arange(data.shape[0]))
ax.set_yticklabels(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

plt.show()
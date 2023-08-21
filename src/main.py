import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date, timedelta

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
data = list(map(list, zip(*data)))

# Create the heatmap
plt.figure(figsize=(10, 10))
plt.imshow(data, cmap='Blues', aspect='auto')
plt.axis('off')  # Hide the axes
plt.show()


# Notes:
# I should create an object to represent a calendar year - this will be a 2D array of weeks
# I should initialize the data to 0 for each week, so that I can increment it later
# I need to figure out a reasonably easy way for someone to set their data, and then have it be displayed

# It is probably easiest to represent the data as a dictionary, where each key is YYMMDD and the value
# is some number between 0-3, or some number that represents intensity/hours spent/etc.
# this should make setting a value for a day easy because you see the date and then say obj[YYMMDD] = num
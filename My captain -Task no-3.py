#!/usr/bin/env python
# coding: utf-8

# In[1]:


#note down the marks you have scored in all cycle tests in ur previous year of college and visualize the data in bar plot  in python

import matplotlib.pyplot as plt

# Replace these values with your actual marks
cycle_tests = [80, 85, 75, 90, 78]

# Corresponding cycle test numbers
test_numbers = ['Cycle 1', 'Cycle 2', 'Cycle 3', 'Cycle 4', 'Cycle 5']

# Creating bar plot
plt.bar(test_numbers, cycle_tests, color='blue')
plt.xlabel('Cycle Tests')
plt.ylabel('Marks')
plt.title('Cycle Test Marks')
plt.ylim(0, 100)  # Set the y-axis limits based on your grading system
plt.show()


# In[ ]:





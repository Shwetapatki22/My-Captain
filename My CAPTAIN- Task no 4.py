#!/usr/bin/env python
# coding: utf-8

# In[1]:


#record your productivity level 1-5 5 being most productive and 1 being least productive and the time of the day  from time u wake uo to when u sleep . the expected result is that the time of the day affects the productivity. perform bivriate analysis by plotting graph where x axis will be the time of the day and y axis will be productivity level(1-5) and stste whether the expected result holds true or not

import matplotlib.pyplot as plt
import random

# Generate hypothetical data
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
productivity_levels = [random.randint(1, 5) for _ in range(len(time_of_day))]

# Plotting the bivariate analysis
plt.scatter(time_of_day, productivity_levels, color='blue')
plt.xlabel('Time of the Day')
plt.ylabel('Productivity Level (1-5)')
plt.title('Bivariate Analysis of Time of Day and Productivity')
plt.show()


# In[ ]:





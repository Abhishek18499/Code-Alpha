#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Defining Function which will return Fibonacci Series upto desired term

def fibonacci(n):
    fib_series = [0, 1]  # Initialiing the series with the first two Fibonacci numbers

    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series[:n]

# got numbers upto 100 terms of fibonacci sequence
# You can put any number inside funciton

result = fibonacci(100)
print(result)


# In[ ]:





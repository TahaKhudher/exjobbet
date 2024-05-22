import matplotlib.pyplot as plt
import numpy as np

# Create your own data (replace with your actual data)
#x = np.logspace(0, 6, num=100, base=10)  # Logarithmic x-axis from 10⁰ to 10⁶
x = [500,5000,50000,500000,1000000] 
y1 = [2.16/1000,27.32/1000, 2.57, 262, 1061]  # Example data for graph 1
y2 =  [1.97/1000,16.91/1000, 1.37, 136, 550]  # Example data for graph 2
y3 =   [1.9/1000,2.33/1000, 6/1000, 43/1000, 80/1000] # Example data for graph 3

# Create the plot
# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y1, label='Quick sort', color='blue')
plt.scatter(x, y2, label='selection sort', color='green')
#plt.scatter(x, y3, label='Merge sort', color='red')

# Connect points with lines
plt.plot(x, y1, color='blue', linestyle='-', alpha=0.7)
plt.plot(x, y2, color='green', linestyle='-', alpha=0.7)
#plt.plot(x, y3, color='red', linestyle='-', alpha=0.7)

plt.xscale('log')  # Set x-axis to logarithmic scale
plt.xlabel('Algorithm Data Amount')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Time vs. Data Amount (C#)')
plt.grid(True)
plt.legend()
plt.show()

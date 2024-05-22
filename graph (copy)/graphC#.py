import matplotlib.pyplot as plt
import numpy as np

# Create your own data (replace with your actual data)
#x = np.logspace(0, 6, num=100, base=10)  # Logarithmic x-axis from 10⁰ to 10⁶
x = [500,5000,50000,500000,1000000]
x1 = [2.57/1000,135.3/1000, 44.5, 4533, 19100]  # Example data for graph 1
x2 =  [2.31/1000,37.7/1000, 23, 2421, 9790]  # Example data for graph 2
x3 =   [2.26/1000,4.24/1000, 13.4/1000, 187/1000, 448/1000] # Example data for graph 3

y1 = [2.16/1000,27.32/1000, 2.57, 262, 1061]  # Example data for graph 1
y2 =  [1.97/1000,16.91/1000, 1.37, 136, 550]  # Example data for graph 2
y3 =   [1.9/1000,2.33/1000, 6/1000, 43/1000, 80/1000] # Example data for graph 3

res = []
for i in range(len(x)):
    res.append((y3[i] / x[i])*1_000_000)
 
print(res)
# # Create the plot
# # Create the plot
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y1, label='Quick sort', color='blue')
# plt.scatter(x, y2, label='selection sort', color='green')
# #plt.scatter(x, y3, label='Merge sort', color='red')

# # Connect points with lines
# plt.plot(x, y1, color='blue', linestyle='-', alpha=0.7)
# plt.plot(x, y2, color='green', linestyle='-', alpha=0.7)
# #plt.plot(x, y3, color='red', linestyle='-', alpha=0.7)

# plt.xscale('log')  # Set x-axis to logarithmic scale
# plt.xlabel('Energy (Joules)')
# plt.ylabel('Time (seconds)')
# plt.title('Algorithm Time vs. Energy Joules(C#)')
# plt.grid(True)
# plt.legend()
# plt.show()

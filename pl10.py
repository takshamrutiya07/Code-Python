# import matplotlib.pyplot as plt
# x = [3, 1, 3]
# y = [3, 2, 1]
# plt.plot(x, y)
# plt.title("Line Chart")
# # Adding the legends
# plt.legend(["Line"])
# plt.show()

# import matplotlib.pyplot as plt 
# import numpy as np 
# x = np.linspace(0.1, 2 * np.pi, 41) 
# y = np.exp(np.sin(x)) 
# plt.stem(x, y, use_line_collection = True) 
# plt.show() 


# import matplotlib.pyplot as plt 
# # data to display on plots 
# x = [3, 1, 3, 12, 2, 4, 4] 
# y = [3, 2, 1, 4, 5, 6, 7] 
# plt.bar(x, y)
# # Title to the plot
# plt.title("Bar Chart")
# # Adding the legends
# plt.legend(["bar"])
# plt.show()

# import matplotlib.pyplot as plt 
# # data to display on plots 
# x = [1, 2, 3, 4, 5, 6, 7, 4] 
# # This will plot a simple histogram
# plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
# # Title to the plot
# plt.title("Histogram")
# # Adding the legends
# plt.legend(["bar"])
# plt.show()

# import matplotlib.pyplot as plt 
# # data to display on plots 
# x = [3, 1, 3, 12, 2, 4, 4]
# y = [3, 2, 1, 4, 5, 6, 7]
# # This will plot a simple scatter chart
# plt.scatter(x, y)
# # Adding legend to the plot
# plt.legend("A")
# plt.title("Scatter chart")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# # Creating dataset
# np.random.seed(10)
# data = np.random.normal(100, 20, 200)
# fig = plt.figure(figsize =(10, 7))
# # Creating plot
# plt.boxplot(data)
# # show plot
# plt.show()

# import matplotlib.pyplot as plt 
# # data to display on plots 
# x = [1, 2, 3, 4] 
# # this will explode the 1st wedge
# # i.e. will separate the 1st wedge
# # from the chart
# e  =(0.1, 0, 0, 0)
# # This will plot a simple pie chart
# plt.pie(x, explode = e)
# # Title to the plot
# plt.title("Pie chart")
# plt.show()


import matplotlib.pyplot as plt 
# making a simple plot
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]
# creating error
y_error = 0.2
# plotting graph
plt.plot(x, y)
plt.errorbar(x, y,yerr = y_error,fmt ='o')


# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# z = [1, 8, 27, 64, 125]
# # Creating the figure object
# fig = plt.figure()
# # keeping the projection = 3d
# # creates the 3d plot
# ax = plt.axes(projection = '3d')
# ax.plot3D(z, y, x)



import matplotlib.pyplot as plt 
data_John = [100, 123, 210, 178, 201]
data_Mary = [107, 121, 232, 155, 232]
width = 0.3
plt.bar(['Jan', 'Feb', 'Mar', 'Apr', 'May'], data_John, width=width)
plt.bar(['Jan', 'Feb', 'Mar', 'Apr', 'May'], data_Mary,bottom=data_John, width=width)

plt.xlabel("Months")
plt.ylabel("Number of units sold")
plt.show()

# Create simple chart with random values

data = [100, -123, 210, 178, 201]
width = 0.4
xlabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
plt.bar(xlabels, data, width=width)

for x in range(len(data)):
    plt.text(x-0.1, data[x]+2, data[x])

plt.show()
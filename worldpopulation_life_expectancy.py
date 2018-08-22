import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv(r"D:\Users\703183779\Documents\gapminder.csv", index_col =0, header=0)
#convert dataframe to list 
pop = list(data.population)
year = list(data.year)
life_exp = list(data.life_exp)
gdp_cap = list(data.gdp_cap)
cont = list(data.cont)
#col_c = list(data.c)

# plt.plot(gdp_cap,life_exp,'ro')
# plt.show()
dictionary = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
col = []
for i in cont:
    for key,value in dictionary.items():
        if key==i:
            col.append(value)
            

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2



# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp ,alpha = 0.8,c =col,s=np_pop/1000000)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,1500,2000,3000,4000,5000,6000, 10000, 100000],['1k','1.5k','2k','3k','4k','5k','6k','10k', '100k'])

# Additional customizations

plt.text(2500, 67.8, 'India', fontsize ="10")
plt.text(5000, 75.8, 'China')

# Add grid() call
plt.grid(True)

# Display the plot
plt.show()

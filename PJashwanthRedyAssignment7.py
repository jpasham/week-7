import pandas as pd
import matplotlib.pyplot as plt


def get_csv(web_link): #This function fetches the dataframe from the url.
    
    return pd.read_csv(web_link)
    


df = get_csv('https://vincentarelbundock.github.io/Rdatasets/csv/vcd/Trucks.csv')

#  calculating the number of accidents accrued at different time period

accidents = [0,0,0]

for i in df.light:
    if i == 'daylight':
        accidents[0] += 1
    elif i == "night, dark":
        accidents[2] += 1
    else:
        accidents[1] += 1

mylabels = ["daylight", "night, illuminate","night, dark"]

plt.pie(accidents,labels = mylabels)
plt.title("Truck Accidents")
plt.show()
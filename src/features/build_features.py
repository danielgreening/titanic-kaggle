import pandas as pd 
import matplotlib.pyplot as plt

# load the passenger data for inspection/exploration
passengers = pd.read_csv('data/external/train.csv')

print(passengers['Fare'])
_ = plt.hist(passengers['Survived'])

plt.show()
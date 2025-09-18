import matplotlib.pyplot as plt
import pandas as pd 

player_data = pd.read_csv('Dataset_Assignment1.csv')

#print(player_data.head())

#print(player_data.describe())

# player_data.hist(figsize=(12, 8), bins=20)
# plt.tight_layout()
# plt.show()

# player_data.plot(x='Weight', y='Height', kind="scatter")
# plt.title("Player Weight vs. Height")
# plt.show()

# Creating a new column to show player BMI 
player_data['Height_m'] = player_data['Height'] / 100
player_data['BMI'] = player_data['Weight'] / (player_data['Height_m'] ** 2)
print(player_data[['Weight', 'Height', 'BMI']].head())
player_data = player_data.drop(columns=['Weight', 'Height', 'Height_m'])
print(player_data.head())


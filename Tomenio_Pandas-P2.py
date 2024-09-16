
import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')
cars

# Display the first five rows with odd-numbered columns
cars.iloc[:5,1::2]  # Selects all rows and odd-numbered columns and the first five rows


# Display the row where the Model is 'Mazda RX4'
# Filter the DataFrame 'cars' to find rows where the 'Model' column matches 'Mazda RX4'
cars.loc[cars['Model'] == 'Mazda RX4']


# Filter the 'cars' DataFrame to select rows where the 'Model' column is equal to 'Camaro Z28'
# and return only the 'Model' and 'cyl' columns for those rows
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# Filter the DataFrame 'cars' to include only specific car models
cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') | 
    (cars['Model'] == 'Ford Pantera L') | 
    (cars['Model'] == 'Honda Civic')
# Return the 'cyl' and 'gear' columns for the filtered rows
] [['Model', 'cyl', 'gear']]


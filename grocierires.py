import pandas as pd
import numpy as np

# Define the number of rows and columns
num_rows = 1000
num_cols = 11

# Create a list of grocery items
groceries = [
    'Milk', 'Bread', 'Eggs', 'Cheese', 'Butter', 'Yogurt', 'Chicken', 'Beef', 'Fish', 'Apple', 'Banana',
    'Orange', 'Grapes', 'Tomato', 'Potato', 'Carrot', 'Broccoli', 'Lettuce', 'Onion', 'Garlic', 'Pepper',
    'Salt', 'Sugar', 'Flour', 'Rice', 'Pasta', 'Beans', 'Cereal', 'Juice', 'Water', 'Coffee', 'Tea',
    'Soda', 'Chocolate', 'Ice Cream', 'Cookies', 'Chips', 'Crackers', 'Peanut Butter', 'Jam', 'Honey',
    'Mustard', 'Ketchup', 'Mayonnaise', 'Olive Oil', 'Vinegar', 'Soy Sauce', 'Hot Sauce', 'Spaghetti Sauce',
    'Baking Powder', 'Baking Soda', 'Cornstarch', 'Yeast', 'Breadcrumbs', 'Oats', 'Nuts', 'Dried Fruit',
    'Canned Tomatoes', 'Canned Beans', 'Canned Tuna', 'Canned Soup', 'Pickles', 'Relish', 'Salsa', 'Maple Syrup',
    'Pancake Mix', 'Waffles', 'Frozen Vegetables', 'Frozen Pizza', 'Frozen Dinners', 'Frozen Fruits', 'Frozen Shrimp',
    'Frozen Fish', 'Butter Milk', 'Cottage Cheese', 'Sour Cream', 'Heavy Cream', 'Half and Half', 'Whipped Cream',
    'Almond Milk', 'Soy Milk', 'Coconut Milk', 'Brown Sugar', 'Powdered Sugar', 'Lemon', 'Lime', 'Strawberries',
    'Blueberries', 'Raspberries', 'Blackberries', 'Peaches', 'Plums', 'Nectarines', 'Pears', 'Mangoes', 'Pineapple',
    'Watermelon', 'Cantaloupe', 'Honeydew', 'Avocado', 'Cucumber', 'Bell Pepper', 'Chili Pepper', 'Spinach', 'Kale',
    'Zucchini', 'Eggplant', 'Brussels Sprouts', 'Asparagus', 'Cauliflower', 'Mushrooms', 'Radishes', 'Celery', 'Corn',
    'Green Beans', 'Peas', 'Lentils', 'Quinoa', 'Couscous', 'Barley', 'Farro', 'Chia Seeds', 'Flax Seeds'
]

# Create the dataset with NaN values
data = np.random.choice(groceries, (num_rows, num_cols))
nan_indices = np.random.choice([True, False], size=(num_rows, num_cols), p=[0.1, 0.9])
data[nan_indices] = np.nan

# Create DataFrame
columns = [f'item{i+1}' for i in range(num_cols)]
df = pd.DataFrame(data, columns=columns)

# Save the dataset to a CSV file
csv_path = 'New_grocerires.csv'
df.to_csv(csv_path, index=False)

csv_path

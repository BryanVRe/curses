import pandas as pd

#-----1------
dataframe = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print("\n", dataframe)

#-----2------
dataframe = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print("\n", dataframe)

#-----3------
dataframe = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print("\n", dataframe)

import pandas as pd

wine_reviews = pd.read_csv("../winer.csv")
print(wine_reviews)

print("\n", wine_reviews.shape)
print(wine_reviews.shape[0])
print(wine_reviews.shape[1])

print("\n\t head")
print("\n",wine_reviews.head())

import pandas as pd
reviews = pd.read_csv("./winer.csv", index_col=0)

#1

renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

# Check your answer
print(renamed)

#2

reindexed = reviews.rename_axis('wines', axis='rows')

# Check your answer
print(reindexed)

#3
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"


combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
print(combined_products)

#4
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")


powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

# Check your answer
print(powerlifting_combined)
import pandas as pd

df = pd.read_csv('movies.csv')

# Collecting Unique Genres
unique_genres = set()

for movie_genre in df["genres"].dropna():
    for genre in movie_genre.split('|'):
        unique_genres.add(genre.strip())

unique_genres = sorted(unique_genres)
unique_genres.pop(0)
print(unique_genres)

# cleaning dataset
print("Data Frame\n", df.count())
dupes = df[df.duplicated(subset="title")]
df.drop_duplicates(subset="title", inplace=True)
print("Duplicated\n", dupes.count())
print("Data Frame\n", df.count())
wrong_data = df.index[df["genres"] == '(no genres listed)'].to_list()
# for i in wrong_data:
#     df.drop(i, inplace=True)
print("Data Frame\n", df.count())

# Replacing movies.csv 'genres' into 'genresId'
insert_id = []

for movie_id, movie_genre in zip(df['movieId'], df['genres']):
    movie_genres = {(x): False for x in unique_genres}
    movie_genres = {'movie_id': movie_id, **movie_genres}
    for genre in movie_genre.split('|'):
        movie_genres[genre] = True
    insert_id.append(movie_genres)

df1 = pd.DataFrame(insert_id)

print(df1)


# df.droplevel(2)

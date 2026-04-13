import pickle

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie = movie.lower()

    matched_movies = movies[movies['title'].str.lower().str.contains(movie)]

    if matched_movies.empty:
        print("Movie not found. Try another movie.")
        return

    movie_index = matched_movies.index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for i in movies_list:
        print(movies.iloc[i[0]].title)


print("Movie Recommendation System")
movie_name = input("Enter movie name: ")

recommend(movie_name)
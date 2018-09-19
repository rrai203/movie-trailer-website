import media
import fresh_tomatoes

movie_name_1 = media.Data('Harry potter and goblet of fire')
movie_name_2 = media.Data('The Conjuring')
movie_name_3 = media.Data('Titanic')
movie_name_4 = media.Data('Star Wars: The Last Jedi')
movie_name_5 = media.Data('Beauty and the Beast')
movie_name_6 = media.Data('Zootopia')
movie_name_7 = media.Data('Justice League')
movie_name_8 = media.Data('John Wick')
movie_name_9 = media.Data('The Shape of Water')
movie_name_10 = media.Data("Schindler's List")
movie_name_11 = media.Data('The Dark Knight')
movie_name_12 = media.Data('Dunkirk')
movie_name_13 = media.Data('Wonder Woman')
movies = [
        movie_name_1,
        movie_name_2,
        movie_name_3,
        movie_name_4,
        movie_name_5,
        movie_name_6,
        movie_name_7,
        movie_name_8,
        movie_name_9,
        movie_name_10,
        movie_name_11,
        movie_name_12,
        movie_name_13]
fresh_tomatoes.open_movies_page(movies)

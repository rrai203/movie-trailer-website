""" stores requested movie data"""
import webbrowser
import urllib.request
import json
import tmdbsimple as tmdb
tmdb.API_KEY = 'aac44b70fb58af5b9eb79ce87fce9325'


class Data():

    """takes argument movie_name,searches the data from tmdb database
       tmdbSimple is wrapper&classes of tmdb
       movie name keyword should be precise so that api can fetch data
       accurately.Incomplete keyword could raise exception.

       Attributes:
           Search():search method in tmdbsimple.
           movie:movie method takes query and return results
           search_result:getd the result of searched movies includes
                         data regarding movies in list format.
           movie_id:stores the unique movie ID for a particular movie
           title:stores title of movie.
           imdb_rating:rating of movie.
           movie_overview:short description of movie.
           release_date:date on which movie released.
           data_yt:searches the movie keyword on youtube api for trailer.
           youtube_key:gets key from the search result in json format
           trailer.youtube_url:complete youtube link to the trailer
           poster_image_url:link to the poster of movie."""

    def get_movie_detail(self, movie_name):
        """search movie id related to query from tmdb api and gets detail
        of movie"""
        try:
            search = tmdb.Search()
            response_old = search.movie(query=movie_name)
            search_result = search.results
            # gets the first id of the search result
            s_find = search_result[0]
            movie_id = s_find['id']
            # uses movie id to get the details of movie
            movie = tmdb.Movies(movie_id)
            # stores the movie information in dict format
            response = movie.info()
            title = response['title']
            vote = response['vote_average']
            discript = response['overview']
            date = response['release_date']
            poster_id = response['poster_path']
            # information of movie in list format
            detail_list = [title, vote, discript, date, poster_id]
            return detail_list
        except IndexError:
            print('The name you are trying to search is not in'
                  'database,try removing integer from keyword')

    def get_trailer_link(self, movie_name):
        """function gets the youtube trailer link from youtube api"""
        query_new = urllib.parse.quote_plus(movie_name+'trailer')
        data_yt = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/"
            "search?part=snippet&maxResults=5&q="+query_new+"&"
            "type=video&key=AIzaSyDE_bEhkLMk077uvbeKqNGSElOMWJHCmfM"
            )
        trailer_data = data_yt.read()
        youtube_json = json.loads(trailer_data)
        youtube_key = str(youtube_json['items'][0]['id']['videoId'])
        return youtube_key

    def __init__(self, movie_name):
        """stores the atrributes of instances"""
        try:
            detail_new = self.get_movie_detail(movie_name)
            self.title = detail_new[0]
            self.imdb_rating = detail_new[1]
            self.movie_overview = detail_new[2]
            self.release_date = detail_new[3]
            # gets movie image from the database tmdbsimple api
            self.poster_image_url = (
                                     "http://image.tmdb.org/t/p"
                                     "/w185"+str(detail_new[4])
                                    )
            self.trailer_youtube_url = (
                         "https://www.youtube.com/watch?"
                         "v="+str(self.get_trailer_link(movie_name))
                                       )
        except TypeError:
            print("Error caused due to non availability of data related to"
                  "your search term dont include integer in search")

    def trailer(self):
        """opens youtube url"""
        webbrowser.open(self.trailer_youtube_url)

# Movie Trailer Website

Movie Trailer is an application that generate a static website
page which allows user to browse their favourite movies.The movies keywords is provided in `entertainment.py` , `python` class uses keyword and provides  information related to the provided movie which includes (title,imdb_rating,overview,release date,youtube trailer & poster image).

The class uses API from tmdb and youtube to get details of movie. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To understand few basic of the API used you can go through the **documentation** at [tmdb](https://www.themoviedb.org/documentation/api)

since i used tmdb wrapper **tmdbsimple** you can get its method at [tmdbsimple](https://github.com/celiao/tmdbsimple/)
there are many more wrapper available for tmdb but they are not compatible with python version 3.5. 

Before starting its required to get registered yourself at tmdb
and optain **api key** which helps in accessing the database.

Also get registers to **google developer** and obtain api key for the same which will be used to obtain link to the trailer of movie.
for more details read documentation at [Youtube](https://developers.google.com/youtube/documentation/)

`fresh_tomatoes.py` can be obtained from [starterCode](https://github.com/udacity/ud036_StarterCode). which generates a html website to display content.

### Installing

You need to install tmdbsimple to get your code running.you can install tmdbsimple by following given instruction.

open python console

>$pip install tmdbsimple

or 

`Download the .zip or .tar.gz file from PyPI and install it yourself
Download the source from Github and install it yourself
If you install it yourself, also install requests.`

tmdbsimple is available on the Python Package Index (PyPI) at 
 [tmdbsimpleDoc](https://pypi.python.org/pypi/tmdbsimple).

### Usage

#### Understanding file structure

this project contain three files `media.py` `entertainment.py` and
`fresh_tomatoes.py`. 

`media.py`:It consist of class Data() which stores the attributes of the instances.

`entertainment.py`:pass the movie name to media.py  

`fresh_tomatoes.py`:converts the obtained data to html website.

#### Using application 

open `entertainment.py` and create an instance name(the name should be unique),call media with the provided name(always pass string value).using of **integer** could raise an
**exception**.

example
```
movie_name_1=media.Data('Harry potter and goblet of fire')
movie_name_2=media.Data('The Conjuring')
movie_name_3=media.Data('Titanic')
movie_name_4=media.Data('Star Wars: The Last Jedi')
movie_name_5=media.Data('Beauty and the Beast')
```
You can obtain movie data as per your requirement.to know more method to obtain details you can read tmdbsimple documentation.

for example
```
self.imdb_rating = response['vote_average']
```
returns the average rating of the movie

for information regarding youtube link there is function ** get_trailer_link **
while obtaining **youtube trailer url** i added trailer keyword to the movie name so that only trailer search is returned.you can use other value to modify search result.

```
query_new = urllib.parse.quote_plus(movie_name+'trailer')
```

youtube returned search result in 'json' format.you can analyse
the whole data and index according to your need.here i used key from first result which gave me accurate result of the movie trailer.

```
youtube_key = str(youtube_json['items'][0]['id']['videoId'])
```

## Bugs

Use of `integer` or `float` in movie name Keyword leads to `exception` as the database could'nt filter the movie name.The api requires exact name of movies.

while using tmdb to get youtube url,few movies url were not present which resulted in false value.due to which have to use youtube api.youtube api gives youtube search result i used json to obtain first search result and filter down the key for youtube url.

database of these api keeps changing which could result in unexpected output.

## Acknowledgments

*fresh_tomatoes.py reffered by udacity.
*udacity helped me build this project.
*wrapper of tmdb helped me a lot.
*stackoverflow.com helped understand many errors. 

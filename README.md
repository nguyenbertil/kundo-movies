# kundo-movies
Kundo work case for potential job candidates. Let's implement a mini webapp!

## The Task

Together we will build a tiny competitor to IMDB, by using an existing
movie database API.

There are many ways to do this, so you can choose whichever tech stack you
are most comfortable with. You should be prepared to get a webpage up and
running, for example with [Django](https://www.djangoproject.com/),
[React](https://reactjs.org/), plain JavaScript, or something similiar
to deliver HTML to a browser.


The landing page should have a search box where you can search for movie
titles. Search results should have their poster, title, and year
displayed.

Clicking on a movie result should bring you to a small details page,
where you can see the director and plot of the movie.

## The API
We will use [OMDb API](http://www.omdbapi.com/) to have a simple API to work with.

To get started quickly and avoid potential network issues we have saved
the result of two API calls already:

### Search
You can search for movie titles from the API with the `s` query parameter:

    curl -XGET 'http://www.omdbapi.com/?apikey=[API-key]&s=[URL encoded search-string]'

The pre-saved data is in data/search.json.

### Details
You can get the details of a specific movie from the API with the `i` query parameter:

    curl -XGET 'http://www.omdbapi.com/?apikey=[API-key]&i=[imdbID]'

The pre-saved data is in data/details.json.

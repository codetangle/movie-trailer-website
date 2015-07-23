import webbrowser


# The movie class, acts as the model for the movie trailer website. 
# Instances of Movie() will be passed to fresh_tomatoes.py.
class Movie():
    def __init__(self, movie_title, storyline, poster_url, trailer_url, director, date, cast):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

        # I added the following additional fields to the class.
        self.director = director
        self.date = date
        self.cast = cast

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

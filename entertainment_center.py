import media
import fresh_tomatoes

# Instaniate movie objects to be displayed on the webpage
toy_story = media.Movie("Toy Story",
                        "A boy and his taking toy have an adventure",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY?t=5s")

star_wars = media.Movie("Star Wars",
                        "Good battles evil on alien worlds",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://youtu.be/9gvqpFbRKtQ")

american_history_x = media.Movie("American History X", "A felon is forced to confront his dark past.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                                 "https://www.youtube.com/watch?v=JsPW6Fj3BUI")

rounders = media.Movie("Rounders", "Two friends navigate the shady world of professional poker.",
                       "https://upload.wikimedia.org/wikipedia/en/6/67/RoundersPoster.jpg",
                       "https://youtu.be/-Qv4K-4-FZM")

mating_habits_of_the_earthbound_human = media.Movie("The Mating Habits of the Earth Bound Human",
                                                    "Dating rituals as seen by an alien race",
                                                    "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Mating_Habits_of_the_Earthbound_Human.jpg",
                                                    "https://youtu.be/9D4N4jrKnVM")

tao_of_steve = media.Movie("The Tao of Steve", "A man figures out what women want",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/The_Tao_of_Steve_VideoCover.jpeg/220px-The_Tao_of_Steve_VideoCover.jpeg",
                           "https://youtu.be/D-B23kX0cXk")

boondock_saints = media.Movie("Bookdock Saints",
                         "Two brothers, on a mission from god, clean up the streets of Boston.",
                         "https://upload.wikimedia.org/wikipedia/en/1/1b/The_Boondock_Saints_poster.jpeg",
                         "https://youtu.be/ydXojYfCF3I")

# Array of movies passed to fresh_tomatoes
movies = [star_wars, american_history_x, rounders, mating_habits_of_the_earthbound_human,
          tao_of_steve, boondock_saints]
         
# Build html and open in browser
fresh_tomatoes.open_movies_page(movies)


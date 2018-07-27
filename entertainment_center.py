import fresh_tomatoes
import media

# The function is used to get the toy story movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", #NOQA
                        "https://www.youtube.com/watch?v=O1pArhQRA8k")



# The function is used to get the avatar movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", #NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


# The function is used to get the midnight in paris movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
midnight_in_paris = media.Movie("Miidnight in Paris",
                               "A romantic comedy about a familiy travelling to French capital for business",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg", #NOQA
                               "https://www.youtube.com/watch?v=dtiklALGz20")


# The function is used to get the forest gump movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
forest_gump = media.Movie("Forest Gump",
                          "The life of a police officer who is very dedicated",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg", #NOQA
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")

# The function is used to get the school of rock movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", #NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# The function is used to get the ratatouille movie: the movie_title,
# movie_storyline, poster_image, trailer_youtube
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chief in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg", #NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, midnight_in_paris, forest_gump, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)

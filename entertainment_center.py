import fresh_tomatoes
import media

# Method used to get the movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/"
                        "1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=O1pArhQRA8k")

# Method used to get the movie
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en"
                     "/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Method used to get the movie
midnight_in_paris = media.Movie("Miidnight in Paris",
                                "A romantic comedy about a familiy"
                                "travelling to French capital for business",
                                "https://upload.wikimedia.org/wikipedia/en/"
                                "thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px"
                                "-Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=dtiklALGz20")

# Method used to get the movie
forest_gump = media.Movie("Forest Gump",
                          "The life of a police officer who is very dedicated",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/"
                          "6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_"
                          "poster.jpg",
                          "https://www.youtube.com/watch?v=uPIEn0M8su0")

# Method used to get the movie
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia"
                             "/en/thumb/1/11/School_of_Rock_Poster.jpg"
                             "/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Method used to get the movie
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chief in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/"
                          "50/RatatouillePoster.jpg/220px-Ratatouille"
                          "Poster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, midnight_in_paris,
          forest_gump, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)

class Movie:
    """Class for movies"""
    
    def __init__(self, movie_title, movie_story_line, poster_image, movie_trailer, release_date, starring):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer
        self.release_date = release_date
        self.starring = starring
               
#def main():
#    pass
    #open_movies_page(movies)

#if __name__ == "__main__":
#    main()
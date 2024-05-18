################################
# Homework5
# CISC 1215
# Points possible : 6
# Due data: May 11th 11:59 Pm
################################


class Movie:
    ''' This is the definition for the object Movie'''
    def __init__(self,name,year,director,budget):
        self.name=name
        self.year=year
        self.director=director
        self.budget=budget

    ############
    # Q7.d) Add a new method that allows two movie object instances
    #       like movie1 and movie2 to be compared with < operator.
    ############
    def __lt__(self, other):
        return self.budget < other.budget

class MovieList(Movie):
    ''' This is the definition for the object MovieList'''
    def __init__(self):
        self.movie_list=[]
    

    ############
    # Q7.a) Complete the method add_movie, make sure you add
    #       appropriate arguments. This method will add a Movie
    #       object instance to the list movie_list
    ############
    def add_movie(self, movie):
        ''' Method to add a movie'''
        self.movie_list.append(movie)

    ############
    # Q7.b) Complete the method remove_movie, make sure you add
    #       appropriate arguments. This method will remove a Movie
    #       object instance from the list movie_list
    ############
    def remove_movie(self, movie):
        ''' Method to remove a movie'''
        if movie in self.movie_list:
            self.movie_list.remove(movie)
        else:
            print("The movie is not in the list")
        
    ############
    # Q7.c) Complete the method most_expensive_movie, make sure you add
    #       appropriate arguments. This method will return most expensive 
    # Movie object instance based on the budget from the list movie_list
    ############
    def most_expensive_movie(self):
        ''' Method to find the most expensive movie'''
        most_exp = self.movie_list[0]
        for movie in self.movie_list:
            if movie.budget > most_exp.budget:
                most_exp = movie
        return most_exp.name

    ############
    # Q7.d) This method will work if you wrote the appropriate method
    #       in the Movie Object definition. You should not touch this
    #       method
    ############
    def most_expensive_movie_with_max(self):
        ''' Method to find the most expensive movie using max built-in function'''
        return max(self.movie_list).name


    
movie1 = Movie('Interstellar', 2014, 'Christopher Nolan', 200000000)
movie2 = Movie('Titanic', 1997, 'James Cameron', 300000000)
movie3 = Movie('Fight Club', 2006, 'Quentin Tarantino', 360000000)

print(movie1 < movie2)

movie_list = MovieList()
movie_list.add_movie(movie2)
movie_list.add_movie(movie1)
movie_list.add_movie(movie3)
movie_list.remove_movie(movie3)
print(movie_list.most_expensive_movie())
print(movie_list.most_expensive_movie_with_max())
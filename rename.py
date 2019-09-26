import os
import shutil
import time

# Ask where the movies are stored and where we have to sort them so we can use
# those variables in the script

movie_location = input("Where are your movies stored? \n")
movie_relocate = input("Where do you want to sort them? \n")
genre = "action"
genre_folder = movie_relocate + "\\" + genre

# Check wether the sorting directory exists or not, loop through as long as
# the folder is not valid

if not os.path.isdir(movie_relocate):
    while not os.path.isdir(movie_relocate):
        print("Folder doesn't exist!")
        print("Please enter an existing folder")
        movie_relocate = input()
    print("Folder found")
else:
    print("Folder found")

# Change location to the movie folder and read all folders inside.

os.chdir(movie_location)

# Read the directory for all files inside
# See in the relocation folder if the scraped movie genre has a folder
# if folder not available we make one

for movies in os.listdir(movie_location):
    if not os.path.isdir(genre_folder):
        print(f"{genre} folder has been created")
        os.makedirs(genre_folder)

# Move all movies from download folder to final location

    shutil.move(movies, genre_folder)
    print(f"{movies} has been moved")

# Sleep timer is just to follow along what happens

    time.sleep(1)

print("All movies have been moved")

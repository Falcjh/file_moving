import os
import shutil
import time
from bs4 import BeautifulSoup
import requests
import re

# Ask where the movies are stored and where we have to sort them so we can use
# those variables in the script

movie_location = "D:\\new"
# Movie_relocate will be a fixed value in the future
movie_relocate = input("Where do you want to sort them? \n")
genre = None

# Check wether the sorting directory exists or not, loop through as long as
# the folder is not valid.

while not os.path.isdir(movie_relocate):
    print("Folder doesn't exist!")
    print("Please enter an existing folder")
    movie_relocate = input()
    genre_folder = movie_relocate + "\\" + genre
print("Folder found")

# Change location to the movie folder and read all folders inside.

os.chdir(movie_location)

# Read all movies inside the folder and remove all non alphanumeric characters

for movie in os.listdir(movie_location):
    movie_sub = re.sub(r'[\.()]+', ' ', movie)
    split_name = re.split(r'[\d+]', movie_sub)
    clean_name = split_name[0]

    print(f"{movie} has been renamed to: {clean_name}")

# Search with clean name on imdb site for movie id and
# follow it to the movie information page

    source = requests.get("https://www.imdb.com/find?q="+clean_name+"&s=tt&ref_=fn_al_tt_mr").text
    soup = BeautifulSoup(source, 'html.parser')

    table = soup.find("table", class_="findList")
    row = table.find("tr", class_="findResult")

    for link in row.find_all("a"):
        movie_id = (link.get("href"))
        movie_url = "https://www.imdb.com" + movie_id + "?ref_=fn_al_tt_1"
    print("link to the movie is: " + movie_url)

    source2 = requests.get(movie_url).text
    soup2 = BeautifulSoup(source2, "html.parser")

    # Find the full movie title + year.

    div_title = soup2.find("div", class_="title_wrapper")
    movie_title = div_title.h1.text
    print("movie title is: " + movie_title)

    # Find the genre of the movie.

    div_genre = soup2.find("div", class_="subtext")
    genre = div_genre.a.text
    print("movie genre is: " + genre)

# check if genre folder exists

    genre_folder = movie_relocate+"\\"+genre

    print("Movie will be send to " + genre_folder)

    if not os.path.isdir(genre_folder):
        os.makedirs(genre_folder)
        print(f"{genre} folder has been created")

    # Move all movies from download folder to final location.

    shutil.move(movie, genre_folder)
    movie_location = genre_folder
    print(f"{movie} has been moved")

    old_name = movie_relocate + "\\" + genre + "\\" + movie
    new_name = movie_relocate + "\\" + genre + "\\" + movie_title

    os.rename(old_name, new_name)
    print(f"{movie} has been renamed to {clean_name}")

    # Sleep timer is just to act human towards IMDB.
    print("Acting Human \n")
    time.sleep(3)


print("All movies have been moved and renamed")

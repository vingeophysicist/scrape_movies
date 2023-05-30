from bs4 import BeautifulSoup
import requests




response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_100_movies = soup.find_all("h3", class_="_h3_cuogz_1")
movies_title = [movie.getText().replace('\xa0', '') for movie in all_100_movies]
del movies_title[-1]
with open("movies_title.txt", mode='w') as file:
	for i in movies_title:
		file.write(f"{i}\n")



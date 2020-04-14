# JSON in Python


import json

movie2 = {}

movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Collin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

# file2 = open("D:/GitHub/Python/Socratica/movie_2.txt", "w", encoding="utf-8")
# file2 = open("/Users/john/Desktop/Python/Socratica/movie_2.txt", "w", encoding="utf-8")
file2 = open("/home/joel/Desktop/Python/Socratica/movie_2.txt", "w", encoding="utf-8")

json.dump(movie2, file2, ensure_ascii=False)
file2.close()

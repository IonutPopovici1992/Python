# JSON in Python

# Key Methods
# json.load(f): Load JSON data from file (or file-like object)
# json.loads(s): Load JSON data from a string
# json.dump(j, f): Write JSON object to file (or file-like object)
# json.dumps(j): Output JSON object as string


import json

print(dir(json))

print(50 * "-")

# json_file = open("D:/GitHub/Python/Socratica/movie_1.txt")
json_file = open("/Users/john/Desktop/Python/Socratica/movie_1.txt")
movie = json.load(json_file)
json_file.close()

print(movie)

print(50 * "-")

print(type(movie))

print(50 * "-")

print(movie["title"])

print(50 * "-")

print(movie["release_year"])

print(50 * "-")

print(movie["actors"])

print(50 * "-")

value = """
    {"title": "Tron: Legacy",
     "composer": "Daft Punk",
     "release_year": 2010,
     "budget": 170000000,
     "actors": null,
     "won_oscar": false
     }
"""

tron = json.loads(value)
print(tron)

print(50 * "-")

print(movie)

print(50 * "-")

print(json.dumps(movie))

print(50 * "-")

print(json.dumps(movie, ensure_ascii=False))

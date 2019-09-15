# List Comprehension

# Problem
# p_remainders = [x ** 2 % p for x in range(0, p)]
# len(p_remainders) = (p + 1) / 2

# Gauss

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story",
          "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca",
          "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey",
          "Raiders of the Lost Ark", "Groundhog Day", "Close Encounters of the Third Kind"]

# Without List Comprehension

gmovies = []

for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

# With List Comprehension

print(80 * "-")

gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)

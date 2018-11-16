from collections import Counter

text = "Text number one is here... Text number two is here... Text number three is here..." \
       "Text number four is here... Text number five is here... Text number six is here..."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

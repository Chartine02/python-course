from operator import methodcaller

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]

clean_humpty = map(lambda x: x.strip(), humpty_dumpty)
print(*clean_humpty, sep='\n')

# 2
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
short_names = filter(lambda word: len(word) < 8, names)
print(list(map(methodcaller('title'), short_names)))

# I think is this better than my solution!! ;)
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
names_title = map(methodcaller("title"), filter(lambda name: len(name) < 8, names))


# 3

print(list(filter(lambda x: x > 0, range(-5,11))))






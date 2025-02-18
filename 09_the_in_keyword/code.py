friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)  # True
print("kob" not in friends)  # True

# --

movies_watched = {"The Matrix","Green Book","Her"}
user_movie = input("Enter something you 've watched recently: ")
print(user_movie in movies_watched)  # True or False

# The `in` keyword works in most sequences like lists, tuples, and sets.
name="Bob"
greeting = "Hello, Bob"

print(greeting)  # Hello, Bob

name = "Rolf"
print(greeting)  # Hello, Bob

# --Using f-strings--
print("-- Using f-strings --")

greeting = f"Hello, {name}"
print(greeting)  # Hello, Rolf

# --
name ="Anne"
print(greeting)  # Hello, Rolf
print(f"Hello, {name}")

# --Using .format()--
print("-- Using .format() --")

greeting ="Hello, {}"
with_name=greeting.format("Rolf")
print(with_name)

longer_phrase="Hello, {}. Today is {}."
formatted=longer_phrase.format("Kob", "Sunday")
print(formatted)


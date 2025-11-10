#Filter names from list that starts with "a" or "A" using lambda function

words = ["Alex", "Bob", "dan", "ash"]

filtered_words = list(filter(lambda word : word == "Alex" or word == "ash", words))
print(filtered_words)
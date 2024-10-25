def word_count(text):
    words = text.split()
    return len(words)

text_input = "ეს არის მაგალითი ტექსტი, სადაც უნდა გამოვითვალოთ სიტყვების რაოდენობა."
count = word_count(text_input)
print("სიტყვების რაოდენობა:", count)
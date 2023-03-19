from flask import Flask, render_template
from random import randint
from collections import Counter
import json

app = Flask(__name__)

@app.route("/")
def home():
    input_text = """
    Banana, watermelon, grape, pear, peach, and kiwi - these are just some of the fruits that we love to eat. Fruits are delicious and healthy, and they come in all shapes and sizes. Some fruits are small and round, like raspberries and blueberries, while others are large and oblong, like pineapples and melons.
    Fruits also have many different colors - red, green, yellow, orange, and even purple! Each color is associated with different nutrients and health benefits. For example, red fruits like strawberries and raspberries are high in antioxidants, which can help protect your body against diseases.
    But fruits aren't just good for your health - they can also be used in many different recipes. Have you ever tried making a fruit salad, a smoothie, or a fruit tart? These are just a few examples of the many delicious dishes you can make with fruits.
    Of course, not everyone likes the same fruits - some people prefer apples over oranges, while others might enjoy mangoes more than bananas. But no matter what your favorite fruit is, there's no denying the fact that fruits are an important part of a healthy diet.
    So the next time you're looking for a snack, consider reaching for a piece of fruit instead of a bag of chips or a candy bar. Your body will thank you for it!
    """
    # generate some example data
    words = input_text.split(" ")
    word_counts = dict(Counter(words))

    # transform word_counts to the format expected by d3-cloud
    word_list = [{'text': word, 'size': count} for word, count in word_counts.items()]

    # randomly assign colors to each word
    colors = ['#f44336', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5', '#2196f3', '#03a9f4', '#00bcd4', '#009688', '#4caf50', '#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff9800', '#ff5722', '#795548', '#9e9e9e', '#607d8b']
    for word in word_list:
        word['color'] = colors[randint(0, len(colors) - 1)]

    # convert word_list to JSON and pass it to the template
    word_list_json = json.dumps(word_list)
    return render_template("index.html", input_text=input_text, word_list=word_list_json)

if __name__ == "__main__":
    app.run(debug=True)

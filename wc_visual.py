from word_counter import WordCounter
import pygal

filename = input("What is the name of the file you want to load? ")
count = input("What is the minimum amount of words per word? ")

wc = WordCounter(filename, count)
wc.word_counter()
wc.adjust_values()

# Save funnel chart to svg file.
funnel_chart = pygal.Funnel()
funnel_chart.title = 'Word Count of ' + str(filename)
for key, value in wc.word_dict.items():
    funnel_chart.add(key, value)
funnel_chart.render_to_file('word_count.svg')

from word_counter import WordCounter
import pygal

filename = input("What is the name of the file you want to load? ")
count = input("What is the minimum amount of words per word? ")

wc = WordCounter(filename, count)
wc.word_counter()
wc.adjust_values()

radar_chart = pygal.Funnel()
radar_chart.title = 'Word Count of ' + str(filename)
for key, value in wc.word_dict.items():
    radar_chart.add(key, value)
radar_chart.render_to_file('word_count.svg')

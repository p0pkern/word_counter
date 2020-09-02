def word_counter(filename):
    """This program will count the selected words appearing in a text"""

    print("This program will count how many words are in a txt file\n" +
          "If you would like get a count of all words enter \'-all-\'")
    print("Currently this does not handle errors or run ons.")
    print("For accuracy, input the minimum frequency(greater than 0) that\n "+
          "you would like to count for.")

    # User enters how many minimum words a word should have to be counted.
    while True:
        frequency = input("How many minimum words should a word have to be counted? ")
        try:
            if int(frequency):
                break
        except ValueError:
            print("That is not a number. Please try again")

    try:
        f_obj = open(filename, 'r')

        word_dict = {}

        for line in f_obj:
            line = line.strip()
            line = line.lower()
            words = line.split(" ")

            for word in words:
                if word in word_dict:
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1

        for key in list(word_dict.keys()):
            if int(word_dict[key]) > int(frequency):
                print(key + ": " + str(word_dict[key]))


    except FileNotFoundError:
        print("File not found")

word_counter('alice.txt')

class WordCounter():
    """This will count the words in a file"""

    def __init__(self, filename, minimum_count=1):
        """
        Initializes the name of the file to count and the minimum amount of
        words the word needs to have to be counted. Defaults to 10
        """
        self.filename = filename
        self.minimum_count = int(minimum_count)
        self.word_dict = {}



    def word_counter(self):
        """
        Counts and adds words to the dictionary
        """
        try:
            f_obj = open(self.filename, 'r')

            for line in f_obj:
                line = line.strip()
                line = line.lower()
                words = line.split(" ")

                for word in words:
                    if word.isalpha():
                        if word in self.word_dict:
                            self.word_dict[word] = self.word_dict[word] + 1
                        else:
                            self.word_dict[word] = 1

        except FileNotFoundError:
            print("File not found")

    def adjust_values(self):
        """
        Prints the words and count to the screen
        """
        for key in list(self.word_dict.keys()):
            if int(self.word_dict[key]) < int(self.minimum_count):
                self.word_dict.pop(key)

import re
import sys
import time
import random


class Stochastic:

    def create_data():
        """Takes no parameters.
        Returns a list of all words in the file"""
        with open('dracula.txt') as words_file:
            raw_data = words_file.read()
            raw_data = raw_data.lower()
            raw_data = raw_data.replace('\n', ' ')
            raw_data = re.sub('[^a-z]+', ' ', raw_data)
            data_list = raw_data.split(" ")
            return data_list

    def create_histogram(data_list):
        """Takes in list of words.
        Returns dictionary of words and frequency"""
        histogram = {}
        get = histogram.get
        for word in data_list:
            histogram[word] = get(word, 0) + 1
        return histogram

    def create_sentence(word_num, histogram):
        """Takes in number of words in sentence, and histogram.
        Returns sentence."""
        total_word_count = 0
        for key in histogram:
            total_word_count += histogram[key]

        sentence = []
        for index in range(0, word_num):
            word = Stochastic.stochastic(histogram, total_word_count)
            sentence.append(word)
        return " ".join(sentence)
        # return sentence

    def stochastic(histogram, total_word_count):
        """Takes in histogram and total word count.
        Returns random word based on probability"""
        index = random.randint(1, total_word_count)

        for key in histogram:
            if index > histogram[key]:
                index -= histogram[key]
            else:
                return key


if __name__ == "__main__":
    start_time = time.time()
    word_num = int(sys.argv[1])
    data_list = Stochastic.create_data()
    histogram = Stochastic.create_histogram(data_list)
    sentence = Stochastic.create_sentence(word_num, histogram)
    # sentence_histogram = create_histogram(sentence)
    end_time = time.time()
    run_time = end_time - start_time
    # print(sentence_histogram)
    print(sentence)
    print("Run time:", run_time)
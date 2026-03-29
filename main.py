import requests
from collections import Counter

def get_text(url):
    response = requests.get(url)
    return response.text

def count_word_frequencies(url, words_to_count):
    text = get_text(url)
    word_counts = Counter(text.split())
    return {word: word_counts[word] for word in words_to_count}

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = []
    with open(words_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.append(word)

    frequencies = count_word_frequencies(url, words_to_count)
    print(frequencies)

if __name__ == "__main__":
    main()

import string
# Creating a Text Analyzer Assistant 
# That count words, count characters, find most frequent words etc...

# Taking user input as text
def get_user_text():
    text = input("Enter your paragraph:\n")
    return text


# Word count, character count, sentence count
def analyze_text(text):
    word_list = text.split()
    word_count = len(word_list)
    char_count = len(text)
    sentence_count = text.count(".")

    print(f"\n📊 Analysis report:")
    print(f"->Total Words: {word_count}")
    print(f"->Total Characters: {char_count}")
    print(f"->Total Sentences: {sentence_count}")


# Finding most frequent word
def most_frequent_word(text):
    # creating a list of stopwords that unneccessarily doesn't count in our frequency count function.
    stopWords = ["the", "is", "a", "an", "as", "of", "on", "in", "and", "to", "from", "with", "for"]
    words = text.lower().split()
    freq = {}

    for word in words:
        # strip punctualtion like . , ? !
        word = word.strip(string.punctuation)
        if word in stopWords:
            continue
        freq[word] = freq.get(word, 0) + 1

    max_word = max(freq, key=freq.get)
    print(f"->Most Frequent Word: '{max_word}' ({freq[max_word]} times)")


# Run the bot
def run_text_analyzer():
    text = get_user_text()
    analyze_text(text)
    most_frequent_word(text)

run_text_analyzer()
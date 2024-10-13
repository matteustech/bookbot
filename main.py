def main():
    count_words()
    count_chars()

def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        split_contents = file_contents.split()
        for i in range(0, len(split_contents)):
            word_count += 1
    print(f"{word_count} words found in the document \n")

def count_chars():
    with open("books/frankenstein.txt") as f:
        sentence = f.read()
        lower_sentence = sentence.lower()
        #split_sentence = sentence.split()
        frequency_count = {}
        unique_characters = []
        char_count = 0

        # Add unique characters to list
        for i in range(0, len(lower_sentence)):
            if lower_sentence[i] not in unique_characters and lower_sentence[i].isalpha():
                unique_characters.append(lower_sentence[i])
                #print(unique_characters)

        # Loop over unique characters and the lower_case sentence. If match, add to dict
        # with count
        for i in unique_characters:
            for j in lower_sentence:
                if i == j:
                    char_count += 1
                    frequency_count[i] = char_count  
            char_count = 0
        
        sorted_freq = dict(sorted(frequency_count.items(),key=lambda item: item[1], reverse=True))

        ## Loop over the dictionary and print report
        for i in sorted_freq:
            print(f"the '{i}' character was found {sorted_freq[i]} times")

main()

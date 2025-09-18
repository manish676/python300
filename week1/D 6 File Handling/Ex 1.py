# Count Words and Lines in a File

def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()  # read all lines into a list
            line_count = len(lines)   # number of lines
            word_count = sum(len(line.split()) for line in lines)  # count words in each line

            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Run function
count_words_and_lines("semple.txt")

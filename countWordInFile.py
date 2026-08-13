filename = input("Enter the Filename: ")

try:
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"Total number of words: {word_count}")
except FileNotFoundError:
    print("File not Found")
except UnicodeDecodeError:
    print("Unable to decode file. Try a different encoding.")
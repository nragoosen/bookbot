def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    report(num_chars)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

# Function to count and sort character frequencies
def get_num_chars(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered in char_count:
                char_count[lowered] += 1
            else:
                char_count[lowered] = 1
    
    # Convert dictionary to list of tuples
    char_count_list = list(char_count.items())

    # Sort list of tuples by the second item (count), in descending order
    char_count_list.sort(key=lambda item: item[1], reverse=True) 
    
    return char_count_list

# Function to print the report
def report(char_count_list):
    for char, count in char_count_list:
        print(f"The '{char}' character was found {count} times.")

# Main function call
main()
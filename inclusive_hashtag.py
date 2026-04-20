def create_inclusive_hashtag(sentence):
    # Split sentence into a list of words
    words = sentence.split()
    
    # Create a list to hold formatted words
    formatted_words = []
    
    # For each word in the list
    for word in words:
        # Capitalize first letter and lowercase the rest
        formatted_word = word.capitalize()
        formatted_words.append(formatted_word)
    
    # Join all words together with no spaces
    hashtag_body = "".join(formatted_words)
    
    # Add "#" at the beginning
    hashtag = "#" + hashtag_body
    
    # Return the finished hashtag
    return hashtag


# Step 3: Main program
def main():
    sentence = input("Enter a phrase to convert to an inclusive hashtag: ")
    hashtag = create_inclusive_hashtag(sentence)
    print("Your inclusive hashtag is:", hashtag)


# Call the main function
if __name__ == "__main__":
    main()
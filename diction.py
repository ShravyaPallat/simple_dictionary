from PyDictionary import PyDictionary

# Create an instance of PyDictionary
dictionary = PyDictionary()


# Get user input for the word
word = input("Enter your word: ")

# Fetch the meanings of the word
meanings = dictionary.meaning(word)
    
if meanings:
    # Initialize a list to hold formatted output
    formatted_output = []
        
    # Iterate through each part of speech and its definitions
    for part_of_speech, definitions in meanings.items():
        # Add the part of speech to the output list
        formatted_output.append(f"{part_of_speech}:")
            
        # Add each definition under the respective part of speech
        for definition in definitions:
            formatted_output.append(f"  - {definition}")
        
    # Print the formatted output, joining list items with new lines
    print("\n".join(formatted_output))
else:
    # Print a message if no meanings are found
    print("No meanings found")

"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = words[0]+ " " + words[2] + " " + words[7] + " " + words[9] + " " + words[1] + " " + words[15] + " " + words[10] + " " + words[8] + " " + words[4] + " " + words[14] + " " + words[5] + " " + words[7] + " " + words[3] + " " + "which bit his leg and made him cry."

#print(words[0])
#print(words[2])
#print([7])
#print([9])

# Create a story using the words in the list

# Display the story to the user
print(''.join(story))
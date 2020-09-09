import os
import re

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))
os.chdir("..")

# Path to collect data from the Resources folder
paragraph1_path = os.path.join("Resources", "paragraph_1.txt")

# Read in the text file
with open(paragraph1_path, "r") as text_file:
    paragraph_string = text_file.read()

# Split paragraph into sentences
paragraph_string = str(paragraph_string)
sentences = re.split("(?<=[.!?]) +", paragraph_string)
words = re.split(" ", paragraph_string)

word_count = len(words)
sentence_count = 0
letter_count = 0
average_letter_count = 0
average_sentence_length = 0

# Gets the word and sentence count
for sentence in sentences:
    sentence_count += 1

# Average Letter Count
for word in words:
    letter_count = letter_count + len(word)

average_letter_count = (letter_count) / (word_count)
word_float = average_letter_count
formatted_float = "{:.1f}".format(word_float)

# Average Sentence Length
average_sentence_length = (word_count) / (sentence_count)
sentence_float = average_sentence_length
formatted_float_2 = "{:.1f}".format(sentence_float)

# Export Analysis to output file
output = open('Analysis\Paragraph1_Analysis.txt', 'w')
output.write("Pararaph Analysis\n")
output.write("-----------------\n")
output.write("Approximate Word Count: " + str(word_count)+"\n")
output.write("Approximate Sentence Count: " + str(sentence_count)+"\n")
output.write("Averange Letter Count: " + str(formatted_float)+"\n")
output.write("Averange Sentence Length: " + str(formatted_float_2)+"\n")
output.close()

# Print to console
print("Pararaph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Averange Letter Count: " + str(formatted_float))
print("Averange Sentence Length: " + str(formatted_float_2))

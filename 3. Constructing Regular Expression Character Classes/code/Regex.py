import re

pattern = r'ab'
text = 'abc acb'

matches = re.findall(pattern, text)

print(f"Pattern: {pattern}\nText: {text}\nMatches: {matches}\n")


#The first statement is importing Python's regular expression library,
# to learn more about this library visit the official documentation.

#The fourth statement uses the variables and the findall method of the re library,
# to search the text for strings matching the pattern.

#Finally, the fifth statement prints the results using a feature of Python 3 called
# "f strings" which interpolates variables into a string.

#Notice that the value of the pattern variable has an r in front of the opening single quote.
#This is Python syntax for defining a raw string literal,
# and it means that backslashes in the string will be treated as a literal character.
#Backslashes are normally used for escape sequences such as newlines (\n).
#Regular expressions also use characters with backslashes to perform certain operations.
#It's good practice in Python to define a regular expression pattern as a
# raw string literal so that it isn't misinterpreted.

pattern = r'.'
text = 'abcdef'
#The pattern contains a period (.), this is a character class and a period
# by itself will match any single character.
#Character Classes are sometimes called Special Sequences.
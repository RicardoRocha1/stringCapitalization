uncapitalizedString = input("Insert the string that needs to be capitalized \n")
words = uncapitalizedString.split()
capitalizedWords = list()
for x in range (len(words)):
    capitalizedWords.append(words[x].capitalize())
end= ' '.join(capitalizedWords)
print(capitalizedWords)
print(end)
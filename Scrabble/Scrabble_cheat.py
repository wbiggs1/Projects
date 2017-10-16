## Scrabble Cheat
# Input 7 letters (a scrabble rack) and output the highest scoring word.

# 1 - construct word list

f = open('sowpods.txt', 'r')
# Strip whitespace/newlines
x = f.readlines()
words = []
for line in x:
    line = line.strip('\n')
    line = str.lower(line)
    words.append(line)

# 2 - Get the rack


while True:
    print("Please input your Scrabble rack, as a string of the 7 letters, e.g. 'abcdefg'.")
    print(">>> ")
    rack = str(input(''))

#Test if there are 7 letters:

    if len(rack) != 7:
        print("You didn't enter 7 letters!")
    else:
        break

#Convert to lowercase
rack = str.lower(rack)

# 3 - Find Valid Words

valid_words = []
for word in words:
    r = rack
    a = True
    while a == True:
        for i in word:
            if i in r:
                r = r.replace(i, '')
            else:
                a = False
                break
        if a == True:
            valid_words.append(word)
            break
        break

 # 4 - Scoring

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
result = {}

for word in valid_words:
    score = 0
    for i in word:
        score += scores[i]
    result[word] = score

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
for w in sorted_result:
    print(w[0] + '   ' + str(w[1]))
    


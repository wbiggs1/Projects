def reverse(text):
    word = []
    l = len(text)
    for i in range(l):
        word.append(text[l-i-1])
    Word = "".join(word)
    return print(Word)

reverse("abcd#")



        

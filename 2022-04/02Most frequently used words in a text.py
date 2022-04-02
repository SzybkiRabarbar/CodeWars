def top_3_words(text):
    new_text = str()
    for i, letter in enumerate(text):
        if letter.isalpha():
            new_text += letter
        else:
            if letter=="'" and (text[i-1].isalpha() or text[i+1].isalpha()):
                new_text += "'"
            new_text += ' '
        


    return new_text

print(top_3_words("Dzie'n 'dobry ''' polsko"))
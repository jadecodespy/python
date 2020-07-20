

def comb_srt(first_word, second_word):
    string_one =list(first_word) 
    string_two =list(second_word)
      comb=1

    for i in string_two:
        string_one.insert(comb,i)
        a=+ 2
    return "" .join(string_one)    

print(comb_srt(Lion, Tiger))
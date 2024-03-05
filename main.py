
with open("books/frankenstein.txt") as f:
    file_contents =f.read()
    dic_num_letters = {}
    list_of_dics = []
    counter = 0
    lower_file_contents = file_contents.lower()
    num_words = len(file_contents.split())
    for letter in lower_file_contents:
        if letter.isalpha():
            if letter in dic_num_letters:
                dic_num_letters[letter] += 1
            else:
                dic_num_letters[letter] = 1
                
    for letter, count in dic_num_letters.items():
        list_of_dics.append({"letter": letter,"num": count})
    list_of_dics.sort(key=lambda x: x['num'], reverse=True)
    print(list_of_dics)

    

#Remove pass and complete the code
def check_character(word, index):
    char = word[index]
    if char.isdigit():
        return "digit"
    elif char.isalpha():
        return "letter"
    elif char.isspace():
        return "white space"
    else:
        return "unknown"
#pushing it all again rn and making sure the autograder works
#hopefully fork is working
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
#!/usr/bin/python3

def format(string):
    char = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    string_format = string.lower()
    for character in char:
        if character in string:
            string_format = string_format.replace(character, "")
    return normalize(string_format)

def normalize(string):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        string = string.replace(a, b)
    return compare(string)

def compare(string):
    large = len(string) - 1
    middle = int(len(string)/2)

    for count in range(middle):
        if count != large - count:
            if string[count] == string[large - count]:
                is_palin = 1
            else:
                is_palin = 0
                break
        else:
            break

    if is_palin == 1:
        return 1
    else:
        return 0

def run():
    string = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ")
    value = format(string)
    if value == 1:
        print(">> '{}': es un palindromo".format(string))
    else:
        print(">> '{}': no es un palindromo".format(string))

if __name__ == "__main__":
    print("____________________________________________")
    print('\nB I E N V E N I D O  A  P A L I N D R O M E')
    print("____________________________________________")
    run()

''' format("A luna ese anula.")
format("oso")
format("anita lava la tina")
format("A la catalana banal, atácala.")
format("A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá.")
format("A Mercedes, ese de crema.")
format("A mi loca Colima.")
format("A ti no, bonita.")
format("Adán no cede con Eva y Yavé no cede con nada.") '''

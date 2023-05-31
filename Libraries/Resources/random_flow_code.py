from random import choice


def random_string_generator(str_len: int) -> str:
    valid_characters = "ABCDELMNOPQRSTUVWXYZ0123456789"
    random_string = ""
    for character in range(0, str_len):
        random_string += choice(valid_characters)
    return random_string

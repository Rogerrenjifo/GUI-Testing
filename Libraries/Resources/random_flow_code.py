from random import choice


def random_string_generator(str_len: int) -> str:
    """Generates a random string of the specified length."""
    valid_characters = "ABCDELMNOPQRSTUVWXYZ0123456789"
    random_string = ""
    for character in range(0, str_len):
        random_string += choice(valid_characters)
    return random_string

def random_num_generator(self):
    """Generates a random single-digit number."""
    valid_characters = "123456789"
    number = choice(valid_characters)
    return number

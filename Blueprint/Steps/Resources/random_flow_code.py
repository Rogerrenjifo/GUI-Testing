from random import choice

class RandomGenerator():

    def random_flow_code(self):
        valid_characters = "ABCDELMNOPQRSTUVWXYZ0123456789"
        code = ""
        for character in range(0, 3):
            code += choice(valid_characters)
        return code


    def random_num_generator(self):
        valid_characters = "0123456789"
        number = choice(valid_characters)
        return number

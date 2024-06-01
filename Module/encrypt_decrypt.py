import random
import re

characters = {'alphabet_u': ['A', 'Ą', 'B', 'C', 'Č', 'D', 'E', 'Ę', 'Ė', 'F', 'G', 'H', 'I', 'Į', 'Y', 'J', 'K', 'L',
                             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'Š', 'T', 'U', 'Ų', 'Ū', 'V', 'W', 'X', 'Z', 'Ž'],
              'alphabet_l': ['a', 'ą', 'b', 'c', 'č', 'd', 'e', 'ę', 'ė', 'f', 'g', 'h', 'i', 'į', 'y', 'j','k', 'l',
                             'm', 'n', 'o', 'p', 'q', 'r', 's', 'š', 't', 'u', 'ų', 'ū', 'v', 'w', 'x', 'z', 'ž'],
              'symbols':  ['~', '!', '@', '#', '$', '%', '^', '&', '(', ')', '–', '_', '=', '+', '[', ']', '{', '}',
                           ';', '“', '"', ',','.', '\\', '/', ':', '*', '?', '"', '<', '>', '|'],
              'numbers':  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

              'whitespace': ['\n', ' ']
              }


class Coder:
    def __init__(self, u_input, u_shift):
        self.u_input = u_input
        self.u_shift = u_shift
        self.counter = 0
        self.shift = []
        self.message = []
        self.encrypted_message = []
        self.decoded_message = []
        self.coded_file = []
        
    def user_input(self):
        pattern = re.findall(r'[-+]?\d?', self.u_shift)
        pattern.remove(pattern[-1])
        self.shift = [int(s) for s in pattern]
        letters = [list(x) for x in self.u_input]
        len_letters = len(letters)
        for let in letters:
            len_letters = len(let)
            for n in range(0, len_letters):
                self.message.append(let[n])

    def encrypt(self):
        for char in self.message:
            if char in characters['alphabet_u']:
                c_index = characters['alphabet_u'].index(char)
                characters_len = (len(characters['alphabet_u']))
                if c_index + self.shift[0] > characters_len - 1:
                    shift_index = (c_index + self.shift[0]) - characters_len
                    self.encrypted_message.append(characters['alphabet_u'][shift_index])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
                elif c_index + self.shift[0] <= characters_len - 1:
                    self.encrypted_message.append(characters['alphabet_u'][c_index + self.shift[0]])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
            elif char in characters['alphabet_l']:
                c_index = characters['alphabet_l'].index(char)
                characters_len = (len(characters['alphabet_l']))
                if c_index + self.shift[0] > characters_len - 1:
                    shift_index = (c_index + self.shift[0]) - characters_len
                    self.encrypted_message.append(characters['alphabet_l'][shift_index])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
                elif c_index + self.shift[0] <= characters_len - 1:
                    self.encrypted_message.append(characters['alphabet_l'][c_index + self.shift[0]])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
            elif char in characters['whitespace']:
                if char == " ":
                    self.encrypted_message.append(" ")
                if char == "\n":
                    self.encrypted_message.append("\n")
            elif char in characters['symbols']:
                c_index = characters['symbols'].index(char)
                characters_len = (len(characters['symbols']))
                if c_index + self.shift[0] > characters_len - 1:
                    shift_index = (c_index + self.shift[0]) - characters_len
                    self.encrypted_message.append(characters['symbols'][shift_index])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
                elif c_index + self.shift[0] <= characters_len - 1:
                    self.encrypted_message.append(characters['symbols'][c_index + self.shift[0]])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
            elif char in characters['numbers']:
                c_index = characters['numbers'].index(char)
                characters_len = (len(characters['numbers']))
                if c_index + self.shift[0] > characters_len - 1:
                    shift_index = (c_index + self.shift[0]) - characters_len
                    self.encrypted_message.append(characters['numbers'][shift_index])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
                elif c_index + self.shift[0] <= characters_len - 1:
                    self.encrypted_message.append(characters['numbers'][c_index + self.shift[0]])
                    self.shift.append(self.shift[0])
                    self.shift.remove(self.shift[0])
        self.counter = 0
        self.shift = []
        self.message = []
        encrypted_message_str = ""
        listToStr = ''.join([str(elem) for elem in self.encrypted_message])
        return listToStr

    def decrypt(self, encrypted_message):
        letters = [list(x) for x in encrypted_message]
        len_letters = len(letters)
        for let in letters:
            len_letters = len(let)
            for n in range(0, len_letters):
                self.coded_file.append(let[n])
        pattern = re.findall(r'[-+]?\d?', self.u_shift)
        pattern.remove(pattern[-1])    
        shift = [(int(i)*(-1)) for i in pattern]
        for char in self.coded_file:
            if char in characters['alphabet_u']:
                c_index = characters['alphabet_u'].index(char)
                characters_len = (len(characters['alphabet_u']))
                if c_index + shift[0] > characters_len - 1:
                    shift_index = (c_index + shift[0]) - characters_len
                    self.decoded_message.append(characters['alphabet_u'][shift_index])
                    shift.append(shift[0])
                    shift.remove(shift[0])
                elif c_index + shift[0] <= characters_len - 1:
                    self.decoded_message.append(characters['alphabet_u'][c_index + shift[0]])
                    shift.append(shift[0])
                    shift.remove(shift[0])
            elif char in characters['alphabet_l']:
                c_index = characters['alphabet_l'].index(char)
                characters_len = (len(characters['alphabet_l']))
                if c_index + shift[0] > characters_len - 1:
                    shift_index = (c_index + shift[0]) - characters_len
                    self.decoded_message.append(characters['alphabet_l'][shift_index])
                    shift.append(shift[0])
                    shift.remove(shift[0])
                elif c_index + shift[0] <= characters_len - 1:
                    self.decoded_message.append(characters['alphabet_l'][c_index + shift[0]])
                    shift.append(shift[0])
                    shift.remove(shift[0])
            elif char in characters['whitespace']:
                if char == " ":
                    self.decoded_message.append(" ")
                if char == "\n":
                    self.decoded_message.append("\n")
            elif char in characters['symbols']:
                c_index = characters['symbols'].index(char)
                characters_len = (len(characters['symbols']))
                if c_index + shift[0] > characters_len - 1:
                    shift_index = (c_index + shift[0]) - characters_len
                    self.decoded_message.append(characters['symbols'][shift_index])
                    shift.append(shift[0])
                    shift.remove(shift[0])
                elif c_index + shift[0] <= characters_len - 1:
                    self.decoded_message.append(characters['symbols'][c_index + shift[0]])
                    shift.append(shift[0])
                    shift.remove(shift[0])
            elif char in characters['numbers']:
                c_index = characters['numbers'].index(char)
                characters_len = (len(characters['numbers']))
                if c_index + shift[0] > characters_len - 1:
                    shift_index = (c_index + shift[0]) - characters_len
                    self.decoded_message.append(characters['numbers'][shift_index])
                    shift.append(shift[0])
                    shift.remove(shift[0])
                elif c_index + shift[0] <= characters_len - 1:
                    self.decoded_message.append(characters['numbers'][c_index + shift[0]])
                    shift.append(shift[0])
                    shift.remove(shift[0])
        self.counter = 0
        self.shift = []
        decrypted_message_str = ""
        delistToStr = ''.join([str(elem) for elem in self.decoded_message])
        return delistToStr


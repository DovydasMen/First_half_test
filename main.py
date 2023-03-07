"""
Saugių slaptažodžių generatorius (Safe password generator)
Requirements: OOP (Inheritance as minimum), functions, modules, import, types, clean code , naming, logging.
"""
from RandomWordGenerator import RandomWord
import logging
from user_input import get_password_lenght

logging.basicConfig(level=logging.DEBUG, filename='generator_logging.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class PasswordGenerator:

    def __init__(self, password_length: int) -> None:
        self.password_length = password_length
        logging.info(f"Client entered value {self.password_length}")

    def get_safe_random_password(self) -> str:
        safe_random_password = RandomWord(max_word_size=self.password_length,
                                          constant_word_size=True,
                                          include_digits=True,
                                          special_chars="@_!#$%^&*()<>?/\|}{~:`",
                                          include_special_chars=True)

        return safe_random_password.generate()


class OwnSpecifiedPassword(PasswordGenerator):

    def __init__(self) -> None:
        self.password_lenght = get_password_lenght()
        logging.info(f"Client entered value {self.password_lenght}")
        super().__init__(password_length=self.password_lenght)

    def get_random_password_of_letters_and_special_chars(self)-> str:
        random_password_letters_and_special_chars = RandomWord(max_word_size=self.password_lenght,
                                                constant_word_size=True,
                                                include_digits=False,
                                                special_chars="@_!#$%^&*()<>?/\|}{~:`",
                                                include_special_chars=True)
        
        return random_password_letters_and_special_chars.generate()
    
    def get_random_password_of_letters(self)-> str:
        random_password_of_letters = RandomWord(max_word_size=self.password_lenght,
                                                constant_word_size=True,
                                                include_digits=False,
                                                special_chars="@_!#$%^&*()<>?/\|}{~:`",
                                                include_special_chars=False)
        
        return random_password_of_letters.generate()


my_password = OwnSpecifiedPassword()
print(my_password.get_random_password_of_letters())
print(my_password.get_random_password_of_letters_and_special_chars())
print(my_password.get_safe_random_password())

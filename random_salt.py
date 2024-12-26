import random
import string

class RandomSalt:
    def __init__(self, length: int):
        """
        :param length: The length of the salt
        """
        self.length = length

    def generate(self) -> str:
        """
        Generate a random salt
        :return: The salt
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
    
    def generate_with_prefix(self, prefix: str) -> str:
        """
        Generate a random salt with a prefix
        :param prefix: The prefix
        :return: The salt with the prefix
        """
        return prefix + self.generate()
    
    def generate_with_suffix(self, suffix: str) -> str:
        """
        Generate a random salt with a suffix
        :param suffix: The suffix
        :return: The salt with the suffix
        """
        return self.generate() + suffix
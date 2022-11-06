import random

class PasswordService:

    def generate_password(self, length):
        words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T',
                 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P',
                 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G',
                 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z',
                 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N',
                 'm', 'M', '_']
        new_password = ""
        for i in range(length):
            new_password = new_password + str(random.choice(words))
        return new_password

    def generate_number_password(self, length):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        new_password = ""
        for i in range(length):
            new_password = new_password + str(random.choice(numbers))
        return new_password

    def hack_number_password(self, pswd):

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        password = self.generate_number_password(len(pswd))
        attempt = 1

        print("Начинается взлом")
        while pswd != password:
            print(f"Попытка №{attempt} - '{password}'")
            attempt = attempt + 1
            password = self.generate_number_password(len(pswd))

        print(f"Удача! Пароль: '{password}'")


    def hack_password2(self, pswd):
        words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T',
                 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P',
                 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G',
                 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z',
                 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N',
                 'm', 'M', '_']

        password = self.generate_password(len(pswd))
        attempt = 1

        print("Начинается взлом")
        while pswd != password:
            print(f"Попытка №{attempt} - '{password}'")
            attempt = attempt + 1
            password = self.generate_password(len(pswd))

        print(f"Удача! Пароль: '{password}'")


psw_service = PasswordService()
psw_service.hack_number_password("11234456")
# print(f"Новый пароль - '{psw_service.generate_password(4)}'")
# print(f"Новый пароль - '{psw_service.generate_password(6)}'")
# print(f"Новый пароль - '{psw_service.generate_password(8)}'")
# print(f"Новый пароль - '{psw_service.generate_password(50)}'")



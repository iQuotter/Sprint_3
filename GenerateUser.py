import random


class User:
    def generation_of_user_data(self):
        self.list_FirstName = ['Evgeniy', 'Nikalay', 'Sergey', 'Kirill', 'Igor']
        self.list_LastName = ['Grekov', 'Kozlikin', 'Kobzev', 'Kafanov', 'Krasilnokov']

        self.FirstName = random.choice(self.list_FirstName)
        self.LastName = random.choice(self.list_LastName)
        self.Email = self.FirstName + self.LastName + str(random.randint(100, 999)) + '@email.ru'

        self.Password = str(random.randint(100, 999)) + self.FirstName + str(random.randint(100, 999))
    
        return self.FirstName, self.Email, self.Password


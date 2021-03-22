from datetime import date

class Member:
    
    def __init__(self, first_name, second_name, date_of_birth, photo, platinum, id=None):

        self.first_name = first_name
        self.second_name = second_name
        self.date_of_birth = date_of_birth
        self.photo = photo
        self.platinum = platinum
        self.id = id


    def calculate_age(date_of_birth):
        today = date.today()
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
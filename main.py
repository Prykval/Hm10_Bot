from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 digits')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self,):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.validate(new_phone)
                phone.value = new_phone
                return
        raise ValueError(f"Phone {old_phone} not found")

    def remove_phone(self, phone_number):
         self.phones = [phone for phone in self.phones if phone.value != phone_number]


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self,name):
       return self.data.get(name)
    
    def delete(self,name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted"
        else:
            return f"Contact with name {name} not found"

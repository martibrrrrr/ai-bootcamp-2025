#assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
#assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
#assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
#assert [el.name for el in directory.find("333")] == ["Vedrai"]

class Directory:
    def __init__(self):# Implement qui il codice
        self.contacts= [] #inizializzo la lista che memorizza le voci in rubrica senza contatti

    def __len__(self):
        return len(self.contacts) #calcolo il n di elementi nella voce self.contact

    def add(self,contact): #aggiungo person o business
        self.contacts.append(contact)

    def query(self,name):
        res = []
        for contact in self.contacts:
            if contact.name == name:
                res.append(contact) #creo una lista. aggiungo il contatto alla lista
        return res #lista contatti

    def find(self,search_contact):
        result = []
        for contact in self.contacts:
            if isinstance(contact, Person): #controllo l'istanza della classe: Person o Business
                if search_contact in contact.name or search_contact in contact.surname or search_contact in contact.phone:
                    result.append(contact)
            elif isinstance(contact,Business):
                if search_contact in contact.name or search_contact in contact.phone:
                    result.append(contact)
        return [self._get_phone(contact) for contact in result]

    def _get_phone(self, contact):
        return contact.phone if contact.phone else None

class Person:
    def __init__(self,name,surname,phone = ""):
        self.name=name
        self.surname=surname
        self.phone = phone

class Business:
    def __init__(self, name, phone= ""):
        self.name = name
        self.phone = phone

#directory = Directory()
#directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
#directory.add(Business(name="Vedrai", phone="+39-333-333333"))
#directory.add(Person(name="Linda", surname="Hamilton"))
#assert len(directory) == 3

"""   class Entry:
    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone
    def matches(self, keyword):
        return keyword in self.name or (self.phone and keyword in self.phone)

class Person(Entry):
    def __init__(self, name, surname, phone=None):
        super().__init__(name, phone)
        self.surname = surname

    def matches(self, keyword):
        return super().matches(keyword) or keyword in self.surname

class Business(Entry):
    def __init__(self, name, phone):
        super().__init__(name, phone)

class Directory:
    def __init__(self):
        self.entries = []

    def __len__(self):
        return len(self.entries)

    def add(self, entry):
        self.entries.append(entry)

    def query(self, name):
        return [entry for entry in self.entries if entry.name == name]

    def find(self, keyword):
        return [entry for entry in self.entries if entry.matches(keyword)]
 """
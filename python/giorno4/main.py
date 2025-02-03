class Directory:
    def __init__(self):# Implement qui il codice
        self.contacts= [] #initialize the list that save contact Items in the Directory as empty

    def __len__(self):
        return len(self.contacts) #calculation of the number of elements  present in the item self.contact

    def add(self,contact): #aggiungo person o business
        self.contacts.append(contact)

    def query(self,name):
        result_c = []
        for contact in self.contacts:
            if contact.name == name:
                result_c.append(contact) #contact list. I add the contact to the list
        return result_c #contact list

    def find(self,search_contact):
        result_c = []
        #i add this in case i'm looking for contacts without number
        for contact in self.contacts:
            if search_contact == "":
                #if not contact.phone:
                if contact.phone is None or contact.phone == "":
                    result_c.append(contact)  #Returns people with no number ""

            elif isinstance(contact, Person):
                if search_contact in contact.name or (contact.surname and search_contact in contact.surname):
                    result_c.append(contact)  #We return the item `Person`
                elif contact.phone and search_contact in contact.phone:
                    result_c.append(contact)  #If we are looking for a number, we return the entire contact

            elif isinstance(contact, Business):
                if search_contact in contact.name or (contact.phone and search_contact in contact.phone):
                    result_c.append(contact)  #If it is a company, return the name
        return result_c

class Person:
    def __init__(self,name,surname,phone=""):
        self.name=name
        self.surname=surname
        self.phone = phone if phone else None #register as None ( inside phone object ) if i don't have the number phone (contact)

class Business:
    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone if phone else None #None - inside phone object -

help(Directory)
help(Business)
help(Person)
##ADDITIONAL CONTROLS. PASS THIS TO test.py file
##result = [el.name for el in directory.find("")]
##print(f"Risultato attuale di find(\"\"): {result}") #print for test "find a empty number phone"
#assert [el.name for el in directory.find("")] == ["Linda"]
#assert [el.phone for el in directory.find("Margaret")] == ["01-234-567"]

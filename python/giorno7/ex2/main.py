import json
#import os #se voglio far scegliere i file .json presenti nella mia cartella. i controlli sarebbero da aggiunggere nel main(da provare)

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
        #search_contact = search_contact.lower()
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

    def save(self, path):
        data = []
        for contact in self.contacts:
            if isinstance(contact, Person):
                data.append({
                    "data_type": "person",
                    "name": contact.name,
                    "surname": contact.surname,
                    "phone": contact.phone
                })
            elif isinstance(contact, Business):
                data.append({
                    "data_type": "business",
                    "name": contact.name,
                    "phone": contact.phone
                })

        with open(path, "w") as fd:
            fd.write(json.dumps(data,indent=2)) # oopure json.dump(data,fd,indent=2)
            print(f"Database saved in {path}")

    def load(self, path):
        try:
            with open(path, "r") as fd:
                data = json.load(fd)
            self.contacts = []

            for entry in data:
                if entry["data_type"] == "person":
                    self.contacts.append(Person(entry["name"], entry["surname"], entry["phone"]))
                elif entry["data_type"] == "business":
                    self.contacts.append(Business(entry["name"], entry["phone"]))
            print(f"Database upload from {path}")

        except FileNotFoundError:
            print(f"Error: file {path} doesn't exist")
        except json.JSONDecodeError:
            print(f"Error: file {path}is not JSON")

class Person:
    def __init__(self,name,surname,phone=""):
        self.name=name
        self.surname=surname
        self.phone = phone if phone else None #register as None ( inside phone object ) if i don't have the number phone (contact)

    #dovrebbe essere utile per stampare o ispezionare con differente rappresentazione l'oggetto
    def __repr__(self):
        return f"Person: {self.name} {self.surname} - Phone: {self.phone}"

class Business:
    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone if phone else None #None - inside phone object -

    #per stampare in modo più leggibile l'oggetto
    def __repr__(self):
        return f"Business: {self.name} - Phone: {self.phone}"

#help(Directory)
#help(Business)
#help(Person)

def main():
    directory = Directory()
    print("Welcome to interactive directory. \n press h for help")

    while True:
        input_data_1=input("> ").strip()

        if input_data_1 == "h":
            print("""   
            Commands:
            a (person|business)     Add
            f <text>                Find
            s <path>                Save (JSON)
            l <path>                Load (JSON)
            q                       Quit     
            """)

        elif input_data_1.startswith("a "):
            input_data = input_data_1.split(" ",1)
            contact_type = input_data[1]
            if contact_type == "person":
                ### add di un record Person
                name = input("Add the name: ")
                surname = input("Add the surname: ")
                phone = input("Add th phone number: ")
                directory.add(Person(name, surname, phone))
            ### add di un record Business
            elif contact_type == "business":
                name = input("Add the name of the Business: ")
                phone = input("Add th phone number: ")
                directory.add(Business(name, phone))
            else:
                print("Invalid type. Use 'a person' or 'a business'.")

        elif input_data_1.startswith("f "):
            results_contact = input_data_1[2:].strip()
            if len(results_contact) < 2:
                results_contact = input("Enter a search term: ").strip() #qua deevo inserire cosa voglio cercare con la funzione find nome,cognome,parte del numero, nome azienda

            results = directory.find(results_contact) #restituisco una lista di risultati
            if results:
                for result in results:
                    print(result)
            else:
                print("! Not found")

        elif input_data_1.startswith("s "):
            path = input_data_1[2:].strip()
            if len(path)<2:
                path = input("Enter the file.json path to save the file:").strip()
            if path:
                directory.save(path)
            else:
                print("Error:missing file path")
        #C:\Users\marti\OneDrive - Politecnico di Torino\Desktop\my_cont.json
        #name.json per salvarlo qui
        elif input_data_1.startswith("l "):
            path=input_data_1[2:].strip()
            if len(path)<2:
                path = input("Enter the file path to load the file: ").strip()
            if path:
                directory.load(path)
            else:
                print("Error:missing file path")

        elif input_data_1 == "q":
            print("Bye Bye")
            break
        else:
            print("Type h for help or q to quit")


#richiamo il main per abilitare i comandi
main()
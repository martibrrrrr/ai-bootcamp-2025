#import os

#Programmazione a ogetti: classi e istanze
class Studente:
    ore_settimanali = 36 #variabili di istanza
    corpo_studentesco= 0 #variabili di classe
    def __init__(self,nome,cognome,corso): #metodo costruttore init = inizializzazione
    #attributi:nome cognome corso
    #istanza = ciascun oggetto creato dalla classe,
    #l'stanza rappresenta l'oggetto a cui associo le proprietà passate nel metodo inizializzazione
    #self rappresenta una referenza a ciascun oggetto creato dalla classe.
    #self: istanza passata automaticamente da python
    #init inizializza le proprietà di ciascu oggetto o istanza
        self.nome = nome
        self.cognome=cognome
        self.corso=corso
        Studente.corpo_studentesco+=1
    #variabili dell'istanza =  attributi della classe

    # aggiungo un secondo metodo alla classe
    def scheda_personale(self):
        return f"Scheda Studente:\n " \
               f"Nome:{self.nome}\n" \
               f"Cognome:{self.cognome}\n "\
               f"Corso di Studi:{self.corso}\n"\
               f"Ore Settimanali:{self.ore_settimanali}"

#creo degli studenti partendo dalla stessa classe: DUE ISTANZE
studente_uno = Studente("Py","Mike","programmazione")
studente_due = Studente("Marta","Bruno","matematica")
print(studente_due)
print(studente_uno)

print(studente_uno.scheda_personale()) #secondo metodo
print(Studente.scheda_personale(studente_uno)) #come parametro passo l'istanza

#incremento allo studente 1 le ore settimanali
studente_uno.ore_settimanali+=4
print(studente_uno.scheda_personale())

#stampo e caratteristiche di
print(Studente.__dict__)
print(studente_uno.__dict__)







"""class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index ={}
        self.surname_index = {}
        self.phone_index = {}

    def __len__(self):
        return len(self.contacts)

    def add(self, contact):
        self.contacts.append(contact)

        if contact.name not in self.name_index:
            self.name_index[contact.name] = []
        self.name_index[contact.name].append(contact)

        if isinstance(contact, Person) and contact.surname:
            if contact.surname not in self.surname_index:
                self.surname_index[contact.surname]=[]
                self.surname_index[contact.surname].append(contact)

        if contact.phone:
            if contact.phone not in self.phone_index:
                self.phone_index[contact.phone] = []
                self.phone_index[contact.phone].append(contact)
        def query(self, name):
            self.name_index.get(name,[])

        def find(self,search_contact):
            result = []
            if search_contact in self.phone_index:
                result =self.phone_index[search_contact]
            else:
                result+=self.query(search_contact)
                result+=self.surname_index.get(search_contact, [])
            return result

class Person:
    def __init__(self,name,surname,phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self,name,phone=""):
        self.name=name
        self.phone=phone

directory = Directory()

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

print([el.name for el in directory.find("Hamilton")])  # Ricerca per cognome
#print([el.name for el in directory.find("01-234-567")])  # Ricerca per numero
#print([el.name for el in directory.find("Vedrai")])

"""

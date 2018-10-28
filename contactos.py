# -*- coding: utf-8 -*-
import csv


class Contact:


    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email


 

class ContactBook:

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))

    def actualizar(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower()==name.lower():
                Newname = str(input('Digite nuevo nombre'))
                NewNumber=str(input('Digite nuev numero'))
                NewEmail=str(input('Digite nuev numero'))

                NewContact=Contact(Newname,NewNumber,NewEmail)
                
                self._contacts[idx]=NewContact
                self._save()
                break

            else:
                self._not_found()
        

    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower()==name.lower():
                del self._contacts[idx]
                self._save()
                break
        

    def __init__(self):
        self._contacts=[]


    def add(self,name,phone,email):
         contact= Contact(name, phone, email)
         self._contacts.append(contact)
         self._save()


    def show_all(self):
        
        for contact in self._contacts:
            self._print_contact(contact)



    def _print_contact(self,contact):
        print('--- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * ---')


    def _not_found(self):
        print('************')
        print('NO LO ENCONTRAMOS!')
        print('************')
        

def run():

    contact_book=ContactBook()

    with open('contacts.csv','rt') as f:
        reader= csv.reader(f)

        for idx, row in enumerate(reader):
            if idx==0:
                continue
            if row == []:
                continue

            contact_book.add(row[0],row[1],row[2])
    
    
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name= str(input('Escribe el nombre del contacto: '))
            phone= str(input('Escribe el tel del contacto: '))
            email=str(input('Escribe el correo del contacto: '))
            contact_book.add(name,phone,email)
            
        elif command == 'ac':
            name= str(input('Escribe el nombre del contacto: '))

            contact_book.actualizar(name)

        elif command == 'b':
             name= str(input('Escribe el nombre del contacto: '))

             contact_book.search(name)

        elif command == 'e':
            name= str(input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
                contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()

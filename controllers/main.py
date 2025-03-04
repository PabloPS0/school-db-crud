# Dados de entrada:
# Name
# Age
# Gender (M/F)
# CPF or ID
# Grade or Class
# Optional: Adress, Phone, Email, Parent's Name

# Menu de Opções:
# Add student
# Update student   
    # Search student by ID or CPF
# Search student
    # Filter    
    # Id (database)
    # CPF
# Delete student
    # Search student by ID or CPF 
import os, sys, time, traceback, itertools
from repositories.connect_db import Connect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Main():
    def __init__(self):
        print('iniciando')
        self.db = Connect()
        
        print(self.db)

    def display_menu(self):
        while True:
            print('''---- OPTIONS ----   
            [1] Add student
            [2] Update student
            [3] Search student
            [4] Delete student
            [5] List all students 
            [6] Exit
                ''')
            chosen_option = input('Digite: ')   

            match chosen_option:
                case '1':
                    os.system('cls')
                    self.add_student()
                case '2':
                    os.system('cls')
                    self.update_student()
                case '3':
                    os.system('cls')
                    self.search_student()
                case '4':
                    os.system('cls')
                    self.delete_student()
                case '5':
                    os.system('cls')
                    self.list_all()
                case '6':
                    self.exit_sys()
                    break
                case _:
                    print('Invalid Option')
                    input('Press Enter to continue...')

    def get_student_data(self):
        print('\nEnter student data:')
        return {
            'name': input('Nome: ').strip(),
            'age': int(input('Idade: ')),
            'gender': input('Gênero (M/F/O): ').upper().strip(),
            'id_doc': input('CPF/ID: ').strip(),
            'class_student': input('Turma: ').strip()
        }
    
    def get_id_data(self):
        print('\nEnter student ID:')
        return {
            'id_doc': input('CPF/ID: ').strip()
        }
    
    def add_student(self): # OK
        student_data = self.get_student_data()
        self.db.add(student_data)
        input('\nRegistered Student! Press Enter to continue...')

    def update_student(self): # ERROR
        # Search for student to update data
        id_student = input('\nEnter ID student: ')
        os.system('cls')
        self.loading_bar(5)
        print('New Data Students')
        if self.db.student_id_exists(id_student):
            new_data = {
                'name': input('\nNome: ').strip(),
                'age': int(input('Idade: ')),
                'gender': input('Gênero (M/F/O): ').upper().strip(),
                'id_doc': input('CPF/ID: ').strip(),
                'class_student': input('Turma: ').strip()
            }
            # Add new data
            self.db.update(new_data)
            input('\nUpdate Student! Press Enter to continue...')
        else:
            print('Invalid Data')

    def search_student(self): # ERROR
        # Search: Id
        input_data = input('ID: ')
        if input_data:
            self.db.search()

    def list_all(self): # OK
        self.db.list_all()
        time.sleep(3)
        input('\nStudent List! Press Enter to continue...')

    def delete_student(self): # OK
        id_student = input('\nEnter ID student: ')
        if self.db.student_id_exists(id_student):
            self.db.delete(id_student)
            time.sleep(3)
            input('\nStudent Deleted! Press Enter to continue...')
        else:
            input('\nStudent Not Found! Press Enter to continue...')

    def exit_sys(self): # OK
        self.db.close_sys()
        print('Exiting the system....')
        time.sleep(3)

    def loading_bar(self, duration=3):
        """
        Exibe uma barra de carregamento animada no terminal por um tempo determinado.

        :param duration: Tempo total da animação em segundos (padrão: 3s).
        """
        end_time = time.time() + duration  # Define o tempo final da animação

        for frame in itertools.cycle(["-", "\\", "|", "/"]):
            if time.time() > end_time:
                break  # Para a animação após o tempo definido
            print(f"\rLoading {frame}", end="", flush=True)
            time.sleep(0.1)

        print("\rLoading Completed!   ")  # Mensagem final para limpar a linha



    
if __name__ == "__main__":
    app = Main()
    app.display_menu()

"""
name = input("Name: ")
age = int(input('Age: '))
gender = input('Gender (M/F/O): ')
id_doc = input('Identification Document: ')
class_student = input('Class: ')
"""
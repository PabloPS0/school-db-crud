from dotenv import load_dotenv
import os, sqlite3

load_dotenv()

class Connect():
    def __init__(self):
        self.db_path = os.getenv("DATABASE_PATH", "repositories/book.db")
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    
    def add(self, student_data): #OK
        self.cursor.execute('''
                INSERT INTO students
                VALUES (NULL, :name, :age, :gender, :id_doc, :class_student)
                ''', student_data)
        self.conn.commit()
# :name = placeholder que evita ataques de SQL Injection e torna o código mais legível (Substitui o método que utiliza o ?)

    def update(self, new_data): #ERROR
        try:
            with sqlite3.connect('book.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE students 
                    SET name = ?, age = ?, gender = ?, id_doc = ?, class_student = ?
                    WHERE id_doc = ?
                    ''', (
                            new_data["name"],
                            new_data["age"],
                            new_data["gender"],
                            new_data["id_doc"],
                            new_data["class_student"],
                            new_data["id_doc"],  # ID antigo para referência no WHERE
                        ))
                conn.commit()
                return cursor.rowcount() # Número de registros atualizados
        except sqlite3.OperationalError as e:
            print(f'Database Error: {e}')

    def search(self): #NO TEST
        try:
            with sqlite3.connect('book.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE name = :name OR id_doc = :id_doc")
                row = cursor.fetchone()
                if row:
                    print(row)
        except sqlite3.OperationalErro as e:
            print(e)

    def list_all(self): #OK
        try:
            with sqlite3.connect('book.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.OperationalError as e:
            print(e)  

    def delete(self, id_student): #Ok
        try:
            with sqlite3.connect('book.db') as conn:
                cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id_doc = ?", (id_student,))
            conn.commit()
        except sqlite3.OperationalError as e:
            print(e)

    def student_id_exists(self, id_student): #OK
        try:
            with sqlite3.connect('book.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT 1 FROM students WHERE id_doc = :id_doc', {"id_doc": id_student})
                row = cursor.fetchone()
                return row is not None
        except sqlite3.OperationalError as e:
            print(e)

    def close_sys(self): #OK
        self.conn.close()
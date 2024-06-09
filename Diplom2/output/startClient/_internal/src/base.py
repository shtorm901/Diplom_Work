import os
import sqlite3

class BaseWorker:

    def set_base_path(self, base_path:str):
        self.base_path = base_path

    def base_check(self):
        return os.path.exists(self.base_path)

    def create_base(self, sql_file:str):
        con = sqlite3.connect(self.base_path)
        cur = con.cursor()

        with open(sql_file, 'r') as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                con.commit()
            except sqlite3.Error as error:
                print(error)


dbmanager = BaseWorker()
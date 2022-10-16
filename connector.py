import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.connector = mysql.connector.connect(host="localhost", user="root", password="", database="my first")

            self.cursor = self.connector.cursor()
        except:
            print("Could not connect to database")
        else:
            print("successfully connected to database")


    def register(self, name, email, password):
        try:
            self.cursor.execute("""
            INSERT INTO `users` (`ID`, `Name`, `Email`, `Password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))
            self.connector.commit()
        except:
            return False
        else:
            return True

    def login(self, email, password):
        self.cursor.execute("""
        SELECT * FROM `users` WHERE `Email` LIKE '{}' AND `Password` LIKE '{}'
        """.format(email, password))
        output = self.cursor.fetchall()
        return output

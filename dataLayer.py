import sqlite3  as sql

class DataBaseHandle():  
    conn = 0

    @staticmethod
    def getCursor():
        DataBaseHandle.__conn__().cursor()

    @staticmethod
    def close():
        DataBaseHandle.__conn__().close()

    @staticmethod
    def commit():
        DataBaseHandle.__conn__().commit()

    @staticmethod
    def execute(query):
        DataBaseHandle.__conn__().execute(query)

    @staticmethod
    def instantiate():
        DataBaseHandle.conn = sql.connect('C:/raycast/example.db')
        return DataBaseHandle.conn

    @staticmethod
    def __conn__():
        pass
        
import sqlite3

sql=sqlite3.connect('Register_Hostel', check_same_thread = False)
base=sql.cursor( )

base.execute("""CREATE TABLE IF NOT EXISTS register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    tel_number TEXT,
    otel_num INTEGER
); """)

def add_client(name, tel_number, otel_num):
    base.execute("""INSERT INTO register (name,tel_number,otel_num) VALUES(?,?,?); """,(name,tel_number,otel_num))
    sql.commit()
def show_info():
    return base.execute("SELECT name, tel_number, otel_num FROM register").fetchall()


#CREATE	Создание таблиц
#INSERT	Вставка новых данных
#SELECT	Чтение данных
#UPDATE	Обновление существующих строк
#DELETE	Удаление строк
#DROP	Удаление таблиц
#ALTER	Изменение структуры таблицы
#COUNT, SUM, AVG и т.д.	Статистика по данным
#WHERE, ORDER BY, LIMIT	Условия и сортировка
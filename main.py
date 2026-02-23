import sqlite3

print("""
Oleg Shlygin's poem database
!del to remove a poem
!add to append a poem
!exit to close database
""")

fulltext_ = ""
name_ = ""
poems_to_delete = []

while True:
    prompt = input("-")
    
    if prompt == "!exit":
        print("closing program")
        break

    if prompt == "!del":
        del_quantity = input("Which ones? (poem1, poem2, ...) _")
        poems_to_delete = [(name.strip(),) for name in del_quantity.split(',')]
    elif prompt == "!add":
        name_ = input("Name _")
        fulltext_ = input("Text _")
    else:
        print("misstake")
        continue

    with sqlite3.connect('pdatabase1.db') as db:
        c = db.cursor()
        
        def new_table():
            c.execute("""--sql
            CREATE TABLE IF NOT EXISTS poems (name TEXT, full_text TEXT)""")

        def func_delete():
            c.execute("""--sql
            DROP TABLE IF EXISTS func""")

        def func_table():
            c.execute("CREATE TABLE IF NOT EXISTS func (func NOT NULL)")

        def func_append2():
            c.executemany("INSERT INTO func VALUES (?)", poems_to_delete)

        def delete_table():
            c.execute("""--sql
                    DROP TABLE IF EXISTS poems""")

        def poem_append():
            c.execute(
                "INSERT INTO poems (name, full_text) VALUES (?,?)", (name_, fulltext_))

        def poem_del_many():
            c.execute("""--sql
            SELECT rowid FROM poems WHERE name IN (SELECT func FROM func)""")
            result = c.fetchall()[:]
            if result == []:
                print("misstake")
            else:
                c.execute("""--sql
                DELETE FROM poems WHERE rowid IN (SELECT rowid FROM poems WHERE name IN (SELECT func FROM func))""")

        # delete_table()

        new_table()

        if prompt == "!del":

            func_delete()

            func_table()

            func_append2()

            poem_del_many()


        if prompt == "!add":
            poem_append()

        db.commit()

        c.close()
        
        
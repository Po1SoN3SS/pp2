import psycopg2
from config import config

def connect():
    params = config()
    conn = psycopg2.connect(**params)  # подключение
    cur = conn.cursor()  # доступ

    # Создать таблицу
    command = """
        CREATE TABLE IF NOT EXISTS phonebook (
            name VARCHAR(255) NOT NULL,
            number INTEGER NOT NULL);
        """
    cur.execute(command)

    print("Какой режим вы хотите выбрать? Введите число...")
    print("1) Загрузить из файла CSV")
    print("2) Добавить нового пользователя")
    print("3) Обновить у пользователя (по нику) его номер.")
    print("4) Обновить у пользователя (по номеру) его ник.")
    print("5) Вывести список всех пользователей с таким номером")
    print("6) Вывести список всех пользователей с таким ником")
    print("7) Удалить всех пользователей с таким номером")
    print("8) Удалить всех пользователей с таким ником")
    mode = int(input("Введите число... "))
    # Это как switch в C++
    match mode:
        case 1:
            command2 = """
                COPY phonebook(name, number)
                FROM 'phonebook.csv'
                DELIMITER ','
                CSV HEADER;
                """
            cur.execute(command2)
        case 2:
            name = input("Введите имя нового пользователя: ")
            number = input("Введите его номре: ")
            new_name = str(name)
            number1 = int(
                number
            )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
            command1 = f"""
                    INSERT INTO phonebook(name, number)
                    VALUES ('{new_name}', {number1});
                    """
            cur.execute(command1)
        case 3:
            filter_name = input("Введите ник нужного пользователя: ")
            new_number = input("Введите новый номер: ")
            filter_name = str(filter_name)
            new_number = int(
                new_number
            )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
            command3 = f"""
                    UPDATE phonebook
                    SET number={new_number}
                    WHERE name='{filter_name}';
                    """
            cur.execute(command3)
        case 4:
            filter_number = input("Введите номер нужного пользователя: ")
            new_nick = input("Введите новый ник: ")
            new_name = str(new_nick)
            filter_number = int(
                filter_number
            )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
            command4 = f"""
                    UPDATE phonebook
                    SET name='{new_nick}'
                    WHERE number={filter_number};
                    """
            cur.execute(command4)
        case 5:
            filter_number = input("Введите номер: ")
            filter_number = int(filter_number)
            command5 = f"""
                    SELECT * FROM phonebook
                    WHERE number={filter_number}
                    """
            cur.execute(command5)
            printed_lines = cur.fetchall()
            for printed_line in printed_lines:
                print(f"{printed_line}")
        case 6:
            filter_nick = input("Введите ник: ")
            filter_nick = str(filter_nick)
            command6 = f"""
                    SELECT * FROM phonebook
                    WHERE name='{filter_nick}'
                    """
            cur.execute(command6)
            lines = cur.fetchall()
            for line in lines:
                print(f"{line}")
        case 7:
            filter_number = input("Введите номер: ")
            filter_number = int(filter_number)
            command7 = f"""
                    DELETE FROM phonebook
                    WHERE number={filter_number}
                    """
            cur.execute(command7)
        case 8:
            filter_nick = input("Введите ник: ")
            filter_nick = str(filter_nick)
            command8 = f"""
                    DELETE FROM phonebook
                    WHERE name='{filter_nick}'
                    """
            cur.execute(command8)
        case _:  # если другие условия не подходят
            print("Неизвестное действие!")

    conn.commit()  # Сохранить в базу данных
    cur.close()  # Закрыть доступ
    # Если conn (подключение) ещё существует
    if conn is not None:
        conn.close()  # Закрыть подключение
        print("Подключение к базе данных закрыто.")


# Главная функция (как main в C++) это curect
if __name__ == "__main__":
    connect()

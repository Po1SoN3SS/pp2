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
    print("9) Вернуть всех пользователей с фильтром по нику")
    print("10) Вернуть всех пользователей с фильтром по номеру")
    print("11) Создать нового пользователя с таким ником или обновить существующего")
    print("12) Зарегистрировать список пользователей")
    print("13) Получить список пользователей с пагинацией (по лимиту и отступу):")
    mode = int(input("Введите число... "))
    # Это как switch в C++
    match mode:
        case 1:
            command1 = """
                COPY phonebook(name, number)
                FROM 'phonebook.csv'
                DELIMITER ','
                CSV HEADER;
                """
            cur.execute(command1)
        case 2:
            name = input("Введите имя нового пользователя: ")
            number = input("Введите его номре: ")
            new_name = str(name)
            number1 = int(
                number
            )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
            command2 = f"""
                    INSERT INTO phonebook(name, number)
                    VALUES ('{new_name}', {number1});
                    """
            cur.execute(command2)
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
            command6 = f"""
                    UPDATE phonebook
                    SET name='{new_nick}'
                    WHERE number={filter_number};
                    """
            cur.execute(command6)
        case 5:
            filter_number = input("Введите номер: ")
            filter_number = int(filter_number)
            command5 = f"""
                    SELECT * FROM phonebook
                    WHERE number={filter_number}
                    """
            cur.execute(command5)
            lines = cur.fetchall()
            for line in lines:
                print(f"{line}")
        case 6:
            filter_nick = input("Введите ник: ")
            filter_nick = str(filter_nick)
            command4 = f"""
                    SELECT * FROM phonebook
                    WHERE name='{filter_nick}'
                    """
            cur.execute(command4)
            printed_lines = cur.fetchall()
            for printed_line in printed_lines:
                print(f"{printed_line}")
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
                    WHERE name='{filter_nick}';
                    """
            cur.execute(command8)
        case 9:
            part_of_name = input("Введите часть имени: ")
            command9 = f"""
                SELECT * FROM phonebook
                WHERE name SIMILAR TO '{part_of_name}';
            """
            cur.execute(command9)
            users = cur.fetchall()
            for user in users:
                print(f"{user}")
        case 10:
            part_of_number = int(input("Введите часть номера телефона: "))
            command10 = f"""
               SELECT * FROM phonebook
               WHERE number SIMILAR TO {part_of_number};
            """
            cur.execute(command10)
            of_users = cur.fetchall()
            for user1 in of_users:
                print(f"{user1}")
        case 11:
            name = input("Введите имя нового пользователя: ")
            number = input("Введите его номре: ")
            command11 = f"""
                SELECT * FROM phonebook
                WHERE name='{name}';
            """
            cur.execute(command11)
            users1 = cur.fetchall()
            # Если список пустой и такого пользователя нет
            if len(users1) == 0:
                # создать его
                name2 = str(name)
                number2 = int(
                    number
                )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
                command_ = f"""
                            INSERT INTO phonebook(name, number)
                            VALUES ('{name2}', {number2});
                            """
                cur.execute(command_)
            else:
                # Этот пользователь уже существует
                name1 = str(name)
                number2 = int(
                    number
                )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
                command_1 = f"""
                            UPDATE phonebook
                            SET number={number}
                            WHERE name='{name}';
                            """
                cur.execute(command_1)
        case 12:
            list_of_users = list()
            while True:
                name = input("Введите имя пользователя или q, чтобы закончить список: ")
                if name == "q":
                    break
                else:
                    number = input("Введите номер телефона: ")
                    name_and_number = (name, number)  # сунуть имя и номер в один элемент
                    list_of_users.append(name_and_number)  # добавить в список
            incorrect_numbers = list()
            for name4, number3 in list_of_users:
                try:
                    number3 = int(number3)
                except:
                    print(
                        f"Пропускаю пользователя '{name4}', его номер '{number3}' неверный. Добавляю в список плохих номеров!"
                    )
                    incorrect_numbers.append(number3)
                    continue
                command12 = f"""
                        SELECT * FROM phonebook
                        WHERE name='{name4}';
                    """
                cur.execute(command12)
                users2 = cur.fetchall()
                # Если список пустой и такого пользователя нет
                if len(users2) == 0:
                    # создать его
                    name5 = str(name4)
                    number4 = int(
                        number3
                    )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
                    command_2 = f"""
                                    INSERT INTO phonebook(name, number)
                                    VALUES ('{name5}', {number4});
                                    """
                    cur.execute(command_2)
                else:
                    # Этот пользователь уже существует
                    name3 = str(name4)
                    number4 = int(
                        number3
                    )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
                    command_3 = f"""
                                    UPDATE phonebook
                                    SET number={number3}
                                    WHERE name='{name4}';
                                    """
                    cur.execute(command_3)
            print("Список неверных номеров: ")
            for incorrect_number in incorrect_numbers:
                print(f"{incorrect_number}")
        case 13:
            limit_per_page = int(input("Введите максимальное количество напечатанных строк: "))
            offset_per_line = int(input("С какой строки начать поиск (сколько строк пропустить): "))
            command13 = f"""
                    SELECT * FROM phonebook
                    LIMIT {limit_per_page} OFFSET {offset_per_line};
                """
            cur.execute(command13)
            users3 = cur.fetchall()
            for user2 in users3:
                print(user2)
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

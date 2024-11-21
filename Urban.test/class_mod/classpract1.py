class Database:
    """
    База данных с информацией пользователя
    """

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


def check_password(password):
    if len(password) < 4:
        print("Слишком короткий пароль!")
    tip = False
    for i in "12345678":
        if i in password:
            tip = True
    if tip == False:
        print("Добавьте хотя бы одну цифру!")
        exit()
    return tip


if __name__ == "__main__":
    database = Database()
    while True:
        choise = int(input("Приветствуем! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choise == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Выполнен вход, {login}")
                    break
                else:
                    print("Неверный пароль.")
            else:
                print("Пользователь не найден")
        if choise == 2:
            """
            Ввод атрибутов и сравнение паролей через password :=
            """
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз. ")
                continue
            database.add_user(user.username, user.password)
        print(database.data)
        check_password(password)


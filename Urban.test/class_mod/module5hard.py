class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.adult_mode = False

    def toggle_adult_mode(self):
        self.adult_mode = not self.adult_mode


class Video:
    def __init__(self, title, description, adult_mode):
        self.title = title
        self.description = description
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []

    def register(self, nickname, password, age):
        if nickname in self.users:
            print("Пользователь с таким именем уже существует.")
        self.users[nickname] = User(nickname, password, age)
        print(f"Пользователь {nickname} успешно зарегистрирован.")

    def log_out(self, nickname):
        if nickname not in self.users:
            print("Пользователь не найден.")
        print(f"Пользователь {nickname}  вышел.")

    def login(self, nickname, password):
        user = self.users.get(nickname)
        if not user:
            print("Пользователь не найден.")
        if user.password != hash(password):
            print("Неверный пароль.")

    def add_video(self, title, description, adult_mode):
        video = Video(title, description, adult_mode)
        self.videos.append(video)
        print(f"Видео {title} добавлено.")

    def watch_video(self, nickname, title):
        user = self.users.get(nickname)
        if not user:
            print("Пользователь не найден.")

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and not user.adult_mode and user.age < 18:
                    print("Доступ запрещен: неподходящий возраст.")
                video.time_now += 1
                return f"Вы смотрите видео: {video.title} - {video.description} на секунде {video.time_now}"

        print("Видео не найдено.")

    def get_videos(self):
        return [(video.title, video.description)
                for video in self.videos
                if not video.adult_mode or (video.adult_mode and any(user.adult_mode for user in self.users.values()))]



urtube = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200,False)
v2 = Video('Для чего девушкам парень программист?', 10, True)
# Добавление видео
urtube.add_video(v1, v2,True)
# Проверка поиска

# Проверка на вход пользователя и возрастное ограничение

urtube.register('vasya_pupkin', 'lolkekcheburek', 13)
urtube.watch_video('Для чего девушкам парень программист?')
urtube.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
urtube.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
urtube.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(urtube.current_user)
# Попытка воспроизведения несуществующего видео
urtube.watch_video('Лучший язык программирования 2024 года!')

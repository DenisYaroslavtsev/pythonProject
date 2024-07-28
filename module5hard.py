import time
class Video:
    def __init__(self, title, duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname,password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return

    def register(self,nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
        self.current_user = new_user
    def log_out(self):
        self.current_user = None

    def get_videos(self,keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self,title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы просмотреть видео!")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.duration):
                    print(f'{second}')
                    time.sleep(1)
                print("Конец видео")
                return
        print("Видео не найдено")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

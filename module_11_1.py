import requests
import matplotlib.pyplot as plt
import concurrent.futures
import pandas as pd


class Repositories_gitHub:

    def __init__(self, languages):
        self.languages = languages
        self.language_count = {}

    def run(self, language):
        url = "https://api.github.com/search/repositories"
        headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        params = {
            "q": f'language:{language}',
            "per_page": 1}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return language, response.json()["total_count"]
        else:
            print(f"Ошибка при получении данных для {language}: {response.status_code}")
            return language, 0

    def get_repositories(self):
        with concurrent.futures.ThreadPoolExecutor() as exc:
            result = exc.map(self.run, self.languages)
        for language, count in result:
            self.language_count[language] = count

        df = pd.DataFrame(list(self.language_count.items()), columns=['Language', 'Count'])
        df.to_csv('repositories_count.csv', index=False)


class Plotter:
    @staticmethod
    def result_count(file_name):
        df = pd.read_csv(file_name)
        df.plot(kind='bar', x='Language', y='Count', legend=False)
        plt.xlabel('Языки программирования')
        plt.ylabel('Кол-во репозиториев(млн)')
        plt.title('Кол-во репозиториев по языкам программирования')
        plt.gcf().set_size_inches(8, 6)
        plt.show()


if __name__ == '__main__':
    languages = ["Python", "JavaScript", "HTML", "Java", "CSS", "Ruby", "C#", "PHP", "C++"]
    counter = Repositories_gitHub(languages)
    counter.get_repositories()
    Plotter.result_count('repositories_count.csv')

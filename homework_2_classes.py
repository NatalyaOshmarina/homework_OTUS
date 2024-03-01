import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time


class MediaFiles:
    """
    Общие данные о медиа-файлах: аудио, видео, фото

    Args:
    file_size (int): объем файла
    file_name (str): название файла
    """

    def __init__(self, file_name, file_size=0):
        self.file_size = file_size
        self.file_name = file_name

    def check_file(self, list_formats):
        """
        Проверяет формат файла и возращает имя файля

        :param list_formats: перечисление форматов
        :type: tuple
        :return: имя файла
        :rtype: строка
        """
        try:
            if self.file_name.split('.')[1] not in list_formats:
                print('Неверный формат файла: {}'.format(self.file_name))
            return self.file_name
        except TypeError:
            print('Неверные данные: {}'.format(self.file_name))
            exit(1)
        except IndexError:
            print('Неверный путь: {}'.format(self.file_name))
            exit(2)


class AudioFiles(MediaFiles):
    """
    Данные об аудио
    Args:
    _audio_format (tuple): кортеж расширений аудио-файлов
    """

    def __init__(self, file_name, file_size=0):
        super().__init__(file_name, file_size)
        self._audio_format = ('WAV', 'AIFF', 'APE', 'FLAC', 'MP3')

    def get_name(self):
        """
        Устанавиливает новое имя файла или возвращает сообщение о неверном формате файла

        :return: новое имя файла
        :rtype: строка
        """
        self.file_name = self.check_file(self._audio_format)
        return self.file_name


class VideoFiles(MediaFiles):
    """
    Данные о видео
    Args:
    _video_format (tuple): кортеж расширений видео-файлов
    """
    def __init__(self, file_name, file_size=0):
        super().__init__(file_name, file_size)
        self._video_format = ('webm', 'mkv', 'flv', 'vob', 'drc')

    def get_name(self):
        """
        Устанавиливает новое имя файла или возвращает сообщение о неверном формате файла

        :return: новое имя файла
        :rtype: строка
        """
        self.file_name = self.check_file(self._video_format)
        return self.file_name


class ImageFiles(MediaFiles):
    """
    Данные о картинках
    Args:
    _img_format (tuple): кортеж расширений файлов изображений
    """
    def __init__(self, file_name, file_size=0, flag_web=False):
        if flag_web:
            super().__init__(file_name, file_size)
        self._img_format = ('gif', 'jpeg', 'png', 'jpg', 'webp')

    def get_name(self):
        """
        Устанавиливает новое имя файла или возвращает сообщение о неверном формате файла

        :return: новое имя файла
        :rtype: строка
        """
        self.file_name = self.check_file(self._img_format)
        return self.file_name


class ParserImageFiles(ImageFiles):
    """
    Данные о картинках, скачанных с сайтов
    Args:
    img_url (str): URL сайта, с которого скачивается картинка
    _list_image (list): список названий файлов картинок сайта
    """

    def __init__(self, img_url, flag_web=True, _img_format=None):
        super().__init__(_img_format, flag_web)
        self.img_url = img_url
        self._list_image = list()

    def __get_list_image(self):
        """
        Возвращает список файлов картинок на сайте

        :return: список имен файлов
        :rtype: список
        """
        response = requests.get(self.img_url, headers={'User-Agent': UserAgent().chrome})
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.findAll('img'):
            self._list_image.append(img['src'].split('/')[-1])
            time.sleep(0.3)
        return self._list_image

    def get_name(self):
        """
        Устанавиливает имя файла или возвращает сообщение о неверном формате файла

        :return: новое имя файла
        :rtype: строка
        """
        self._list_image = self.__get_list_image()
        for self.file_name in self._list_image:
            self.file_name = self.check_file(self._img_format)
            return self.file_name


audio = AudioFiles('Audio.WAV')
print(audio.get_name())
audio = AudioFiles('Audio.txt')
print(audio.get_name())
video = VideoFiles('Video')
video.get_name()
image = ParserImageFiles('https://matroskin-perm.ru/cats/')
print(image.get_name())




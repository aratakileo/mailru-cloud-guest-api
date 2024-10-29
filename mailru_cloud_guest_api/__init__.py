from urllib.request import urlretrieve
from typing import Callable
from requests import get
from os import PathLike
from json import loads


MAX_LIFETIME = 86400
API_VERSION = 2


class FileStreamLink:
    def __init__(self, file_id: str, stream_path: str):
        self.__file_id = file_id
        self.__stream_path = stream_path

    @property
    def public_link(self):
        return 'https://cloud.mail.ru/public/' + self.__file_id

    @property
    def stream_link(self):
        return self.__stream_path + '/' + self.__file_id

    def download(
            self,
            filename: str | bytes | PathLike[str] | PathLike[bytes] = None,
            reporthook: Callable[[int, int, int], object] = None
    ):
        return urlretrieve(self.stream_link, filename, reporthook)


class FileStreamGenerator:
    def __init__(self, file_id: str):
        self.__file_id = file_id
        self.__lifetime = MAX_LIFETIME
        self.__email = 'mail@mail.ru'

    def set_mail(self, email: str):
        self.__email = email
        return self

    def set_lifetime_in_hours(self, hours: int):
        return self.set_lifetime_in_seconds(hours * 3600)

    def set_lifetime_in_minutes(self, minutes: int):
        return self.set_lifetime_in_seconds(minutes * 60)

    def set_lifetime_in_seconds(self, seconds: int):
        if self.__lifetime > MAX_LIFETIME:
            raise ValueError(f'{seconds} seconds is more than the maximum allowed {MAX_LIFETIME}')

        self.__lifetime = seconds

        return self

    def generate(self):
        response = get(self.dispatcher_request_link)

        if response.status_code != 200:
            raise InvalidResponse(f'server returned response with status code {response.status_code}')

        return FileStreamLink(
            self.__file_id,
            loads(response.text)['body']['weblink_get'][0]['url']
        )

    @property
    def dispatcher_request_link(self):
        return f'https://cloud.mail.ru/api/v2/dispatcher?api={API_VERSION}&email={self.__email}&_={self.__lifetime}'

    @staticmethod
    def of(public_link: str):
        segments = public_link.split('/')[-2:]

        if len(segments) != 2:
            raise ValueError(f'invalid public link `{public_link}`')

        return FileStreamGenerator('/'.join(segments))


class InvalidResponse(Exception):
    def __init__(self, message: str):
        super().__init__(message)


__all__ = 'FileStreamGenerator', 'FileStreamLink', 'InvalidResponse'

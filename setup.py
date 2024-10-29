try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mailru_cloud_guest_api',
    version='1.0.1',
    packages=['mailru_cloud_guest_api'],
    url='https://github.com/aratakileo/mailru-cloud-guest-api',
    license='MIT',
    author='Arataki Leo',
    author_email='aratakileo@gmail.com',
    description='Non-official wrapper API for mail.ru cloud designed to generate a link or links to a file stream '
                'via a public link, for example to download file as a guest'
)

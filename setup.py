import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "validfilter",
        version = "1.0",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "A simple validation module ,support regex",
        license = "MIT",
        keywords = "validation dictionary validate valid list json request validator",
        url = "https://github.com/rfyiamcool",
        packages = find_packages(),
        long_description = read('README.md'),
        classifiers = [
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License'
            ]
        )


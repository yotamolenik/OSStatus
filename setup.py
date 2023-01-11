from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent.resolve(strict=True)
VERSION = '1.0.1'
PACKAGE_NAME = 'osstatus'
DATA_FILES_EXTENSIONS = ['*.txt', '*.json', '*.js']
PACKAGES = [p for p in find_packages() if not p.startswith('tests')]


def parse_requirements():
    reqs = []
    with open(BASE_DIR / 'requirements.txt', 'r') as fd:
        for line in fd.readlines():
            line = line.strip()
            if line:
                reqs.append(line)
    return reqs


def get_description():
    return (BASE_DIR / 'README.md').read_text()


if __name__ == '__main__':
    setup(
        version=VERSION,
        name=PACKAGE_NAME,
        description='Get os status from the OSStatus website',
        long_description=get_description(),
        long_description_content_type='text/markdown',
        packages=PACKAGES,
        author='Yotam',
        author_email='yotamolenik@gmail.com',
        license='GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007',
        install_requires=parse_requirements(),
        include_package_data=True,
        package_data={PACKAGE_NAME: ['cache.pickle', ]},
        entry_points={
            'console_scripts': ['osstatus=osstatus.__main__:cli',
                                ],
        },
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
        url='https://github.com/yotamolenik/OSStatus',
        project_urls={
            'mobileconfig': 'https://github.com/yotamolenik/OSStatus'
        },
        tests_require=['pytest', ],
    )

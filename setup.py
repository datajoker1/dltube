from setuptools import setup, find_packages

setup(
    name="dltube",
    version="0.1",
    description="Made to download YouTube videos comfortably.",
    packages=find_packages(),
    install_requires=['dltube'],
    python_requires='>=3',
    author="gtpark",
    author_email='datajoker1@gmail.com',   
    entry_points = {
        'console_scripts': [
            'dltube = dltube.__main__:main'
        ]
    }
)

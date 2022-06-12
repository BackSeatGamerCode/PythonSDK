from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='BSGPythonSDK',
    version='1.0',
    packages=['BSGPythonSDK'],
    url='https://backseatgamer.pythonanywhere.com/',
    license='MIT',
    author='BackSeatGamer',
    author_email='cpsuperstoreinc@gmail.com',
    description=' The generic BackSeatGamer SDK for games written in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/BackSeatGamerCode/PythonSDK/issues",
        "Discussions": "https://github.com/BackSeatGamerCode/PythonSDK/discussions"
    },
    keywords=['BACK', 'SEAT', 'GAMER', 'BACKSEATGAMER', 'AUDIENCE', 'INTERACTION', 'LIVESTREAM', 'VIDEOGAME', 'GAME'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Desktop Environment",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Multimedia",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Networking"
    ]
)

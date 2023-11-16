from setuptools import setup, find_packages

setup(
    name='math-quiz-game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here if any
    ],
    entry_points={
        'console_scripts': [
            'math-quiz=math_quiz.__main__:math_quiz',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
    ],
)

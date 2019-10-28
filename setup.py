from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='work_calendar_ru',
    version='1.0.6',
    packages=find_packages(),
    url='https://github.com/SLRover/work-calendar-ru',
    license='MIT',
    author='Ilya Sapunov',
    author_email='ilya.sapunov@gmail.com',
    description='Russian work calendar',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

from setuptools import setup
from typing import List


# Declaring Variable for setup funtion
PROJECT_NAME = 'housing predictor'
VERSION ='0.0.1'
AUTHOR= 'Sohel'
DESCRIPTION = 'Housing Prediction Using CICD Pipeline , Github, Docker with Heroku '
PACKAGES=['Housing']
REQUIREMENTS_FILE_NAME= 'requirements.txt'

def get_requirements_list()->List[str]:
    '''This funtion going to return requirement from text file'''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version =VERSION,
author = AUTHOR,
Description = DESCRIPTION,
Packages=PACKAGES,
install_requirement=get_requirements_list()
)



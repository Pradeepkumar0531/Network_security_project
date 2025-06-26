# this file is essential part of packaging and distributing python projects.

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    # this function will return the list of requirements
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Pradeep Kumar",
    author_email="pradeepkumar0531@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools
(or distutils in Python older versions) to define the configuration
of your projects, such as it's metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('[ERROR] requirements.txt not found.')
        
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sripraneeth Salapareddi",
    author_email="sripraneethsalapareddi@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)
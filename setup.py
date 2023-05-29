from setuptools import setup, find_packages
from typing import List

def get_requirements(file_name:str)-> List[str]:
    '''Get requirements from requirements.txt'''
    requirement =[]
    with open(file_name) as f:
            for line in f:
                requirement.append(line.strip())

    if '-e .' in requirement:
         requirement.remove('-e .')

    return requirement  


'''Set up methods'''
setup(
    name='walletitpricing',
    version='0.0.1',
    author='Geekay Ncube',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)


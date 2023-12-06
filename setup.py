from setuptools import find_packages, setup
from typing import List

def get_requirements(requirement_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''

    requirements = []
    with open(requirement_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        try:
            requirements.remove('-e .')
        except:
            pass
    return(requirements)

setup(
    name='loan_approval',
    version='0.0.1',
    author='Apratim',
    author_email='apratim.bajpai@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
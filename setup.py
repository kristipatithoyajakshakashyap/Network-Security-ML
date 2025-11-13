from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Thoyajaksha Kashyap',
    author_email='kristipatithoyajakshakashyap@gmail.com',
    packages=find_packages(),
    install_required=get_requirements()
)
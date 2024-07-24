from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    #this function will return a list of requirements

    requirements=[]

    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [requirement.replace("\n","") for requirement in requirements]
    
    if "-e ." in requirements:
        requirements.remove("-e .")
    
    return requirements


setup(
    name="ML-PRO",
    version= "0.0.1",
    author= "Karan",
    author_email="karthikkaran5@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements("requirements.txt")
    )
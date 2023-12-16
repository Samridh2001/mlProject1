from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    
    #this will return  the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        #replace blank space \n
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Samridh',
    author_email='samridhagarwal3@gmail.com',
    packages= find_packages(),
    # install_requires=['pandas','numpy','seaborn'] this way of having packages is not feasible as there are many packages
    install_requires=get_requirements('requirements.txt')
)

#-e . in requirements.txt will automatically trigger the setup file
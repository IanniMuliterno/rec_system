from setuptools import setup 
  

SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy','sklearn']

setup( 
    name='Book Recommendation', 
    version='0.1', 
    description='A personal project', 
    author='Ian Muliterno', 
    author_email='ianmuliterno@gmail.com', 
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
) 
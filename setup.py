from setuptools import setup, find_packages

setup(
    name='inference-client-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'cryptography',
    ],
    author='jamesavechives',
    author_email='your_email@example.com',
    description='SDK for interacting with the Inference API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

from setuptools import setup

setup(
    name='novaposhta-python-client',
    version='0.0.9',
    packages=['novaposhta'],
    url='https://github.com/semolex/novaposhta-python-client',
    install_requires=[
        'httpx',
    ],
    license='MIT',
    author='semolex',
    author_email='semolex@live.com',
    description='Python client for Nova Poshta API.'
)

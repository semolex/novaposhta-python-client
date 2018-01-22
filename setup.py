from distutils.core import setup

setup(
    name='novaposhta-api-client',
    version='0.0.9',
    packages=['novaposhta'],
    url='https://github.com/semolex/novaposhta-api-client',
    install_requires=[
        'requests',
    ],
    license='MIT',
    author='semolex (Oleksii Semeshchuk)',
    author_email='semolex@live.com',
    description='Python client for Nova Poshta company\'s API.'
)

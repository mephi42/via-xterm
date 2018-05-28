import setuptools

with open('README.rst') as fp:
    long_description = fp.read()

setuptools.setup(
    name='via-xterm',
    version='0.1.2',
    author='mephi42',
    author_email='mephi42@gmail.com',
    description='Connect Python script to xterm',
    long_description=long_description,
    url='https://github.com/mephi42/via-xterm',
    scripts=['via-xterm'],
    classifiers=(
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
    ),
)

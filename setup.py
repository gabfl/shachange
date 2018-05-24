from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='shachange',
    version='1.2',
    description='Change an image sha signature',
    long_description=long_description,
    author='Gabriel Bordeaux',
    author_email='pypi@gab.lc',
    url='https://github.com/gabfl/shachange',
    license='MIT',
    packages=['shachange'],
    package_dir={'shachange': 'src'},
    install_requires=['argparse', 'pillow'],  # external dependencies
    entry_points={
        'console_scripts': [
            'shachange = shachange.shachange:main',
        ],
    },
    classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Security',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        #  'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        #  'Development Status :: 5 - Production/Stable',
    ],
)

import sys

sys.path.insert(0, '.')
import liphtePy

from setuptools import setup, find_packages

setup(
    name='LiphtePy',
    version=liphtePy.__version__,
    description='''An s-expression style template engine.''',
    long_description='''
        LiphtePY is a fork of Python template engine called Breve that is designed to be clean and elegant with
        minimal syntax.  Unlike most Python template engines, LiphtePY and Breve is implemented as an
        `internal DSL`_ rather than a parser.

        LiphtePY was heavily inspired by `Nevow Stan`_ and is, in fact, the successor to
        TurboStan (defunct), my earlier attempt to bring a Stan-like engine to TurboGears.

        .. _Nevow Stan: http://divmod.org/trac/wiki/DivmodNevow
        .. _`internal DSL`: http://martinfowler.com/bliki/DomainSpecificLanguage.html
    ''',
    author='Michał Ligus, Grzegorz Przydryga, Cliff Wells',
    author_email='maveilthain@gmail.com',
    url='http://maveius.pl/liphte.py/',
    download_url='https://github.com/maveius/liphte.py/archive/master.zip',
    classifiers=[
        'Development Status :: 5 - Production',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Buffet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['python.templating.engines'],
    install_requires=[],
    scripts=[],
    packages=find_packages(),
    zip_safe=True,
    entry_points='''
        [python.templating.engines]
    ''',
    test_suite='liphtePy.tests.testsuite'
)

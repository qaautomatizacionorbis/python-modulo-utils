from python_modulo_utils import get_version
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages

long_description = "Modulo contenedor de utilitarios python"
requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name             = 'python_modulo_utils',
    description      = 'Modulo contenedor de utilitarios python',
    packages         = find_packages(),
    author           = 'George Castrejon Sandoval',
    author_email     = 'automatizaciones.qa.orbis [at] gmail.com',
    install_requires = install_requires,
    version          = get_version(),
    license          = "MIT",
    zip_safe         = False,
    keywords         = "python-modulo-utils",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 1 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                      ]
)
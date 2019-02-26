Modulo contenedor de utilitarios python
========================================
Proyecto de utilitarios 

Instalar
--------
Mediante setup.py
```console
(venv) ~/python-modulo-utils ❯❯❯ python setup.py install
Processing dependencies for module==0.0.1
Searching for marshmallow==2.15.3
Finished processing dependencies for module==0.0.1
```

Para instalar usando pip desde un repositorio en git, agregar al archivo requirements.txt:

```console
git+https://github.com/qaautomatizacionorbis/python-modulo-utils.git
```

Instalar modo development
-------------------------
```console
(venv) ~/python-modulo-utils ❯❯❯ python setup.py devlopment
Processing dependencies for module==0.0.1
Searching for marshmallow==2.15.3
Finished processing dependencies for module==0.0.1
```

Usar
----
```console
Python 3.7.0 (default, Jul 23 2018, 20:22:55)
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from python_modulo_utils.utils import date
>>> date.getDate()
2019-02-26 10:43:12.543707
>>>
```

Test
----
Instalar pytest
```console
(venv) ~/python-modulo-utils ❯❯❯ pip install pytest
```

Ejecutar pytest -v
```console
(venv) ~/python-modulo-utils ❯❯❯ pytest -v
```
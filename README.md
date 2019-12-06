# How to Install

### From Github

```{python}
$ pip install git+https://github.com/joaopcnogueira/jptools#egg=jptools
```

### Locally

1. Download or clone the project

2. In the project root folder `jptools`, run:

```
$ python setup.py sdist bdist_wheel
```

3. It will generate two files under the `dist` folder:

```
dist/
    jptools.0.0.1-py3-none-any.whl
    jptools.0.0.1.tar.gz
```

4. To install locally, just `pip` it:

```
$ cd dist
$ pip install jptools.0.0.1-py3-none-any.whl
```

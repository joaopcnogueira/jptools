# How to Install

### Locally

1. Clone the repo:

```
```

2. In the `project root` folder, run:

```
python setup.py sdist bdist_wheel
```

3. It will generate two files under the `dist` folder:

```
dist/
    pkgname_YOUR_USERNAME-0.0.1-py3-none-any.whl
    pkgname_YOUR_USERNAME-0.0.1.tar.gz
```

4. To install locally, just `pip` it:

```
pip install pkgname_YOUR_USERNAME-0.0.1-py3-none-any.whl
```

5. To install from GitHub:


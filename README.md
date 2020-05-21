# clscreate, benchmarking class creation time for fun and profit

See for more https://github.com/PyO3/pyo3/issues/661

You can test this again with:

```
$ pip install -r requirements.txt
$ cythonize -a -i clscreate_cython.pyx
$ pytest
```
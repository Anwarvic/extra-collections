# Generating the documentation

You only need to generate the documentation to inspect it locally (if you're planning changes and want to 
check how they look like before committing for instance). You don't have to commit the built documentation.

---

## Packages installed

Here's an overview of all the packages installed. There are no requirements for
this package. So building it requires only installing the package `sphinx` that
you can install using:

```bash
pip install -U sphinx
```

You would also need the custom installed
[theme](https://github.com/readthedocs/sphinx_rtd_theme) by
[Read The Docs](https://readthedocs.org/). You can install it using the
following command:

```bash
pip install sphinx_rtd_theme
```

## Building the documentation

Once you have setup `sphinx`, you can build the documentation by running the
following command in the `/docs` folder:

```bash
make html
```

A folder called `build/html` should have been created. You can now open the file
`build/html/index.html` in your browser. 

**NOTE**

If you are adding/removing elements from the toc-tree or from any structural
item, it is recommended to clean the build directory before rebuilding.
Run the following command to clean and build:

```bash
make clean && make html
```

---

It should build the static app that will be available under `/docs/_build/html`


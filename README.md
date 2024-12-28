# python-template

A Python project template built based on PDM. It has integrated the basic tool chain required for Python development.

# Devlop environment

We use [pdm](https://github.com/pdm-project/pdm) as our project's dependency management and build system.

Please refer to the [official documentation](https://github.com/pdm-project/pdm) to set up pdm on your device

Or run:

```
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

## Ruff
[Ruff](https://github.com/astral-sh/ruff) is Python linter and code formatter.

Execute the following command to run ruff for inspection.

```
pdm run tox -e ruff_check
```

## Mypy
[Mypy](https://github.com/python/mypy) is a static type checker for Python.

Execute the following command to run ruff for inspection.

```
pdm run tox -e mypy_check
```

## Static check
Run mypy and ruff at the same time.

```
pdm run tox -e static_check
```

## Package
We use [shiv](https://github.com/linkedin/shiv/tree/main) to build the distributable pyz package.

Please run the following command to build it.

```
pdm run tox -e package
```

# PYTIA UI Tools

Helper functions and widgets for all pytia ui apps.

![state](https://img.shields.io/badge/State-Alpha-brown.svg?style=for-the-badge)
![version](https://img.shields.io/badge/Version-0.1.0-orange.svg?style=for-the-badge)

[![python](https://img.shields.io/badge/Python-3.10-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
![OS](https://img.shields.io/badge/OS-WIN10%20|%20WIN11-blue.svg?style=for-the-badge)

> ✏️ This package only provides helper functions, widgets and some other stuff for all pytia ui apps. This package is therefore a required dependency for almost all pytia apps, but does nothing on its own.
>
> ⚠️ The layout of this app is heavily biased towards the workflow and needs of my companies' engineering team.
>
> 🔒 This is currently a private repo.

## 1 installation

### 1.1 system requirements

- Windows 10/11
- [Python 3.10](https://www.python.org/downloads/)
- MS Outlook (optional)

### 1.2 pip

To pip-install this module you need to have access to this repo (which you obviously have if you can read this README). You then have two options:

#### 1.2.1 access token

Create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for pip'ing it.

```powershell
python -m pip install git+https://${GITHUB_TOKEN}@github.com/deloarts/pytia-ui-tools.git{VERSION}
```

Use your access token instead of *GITHUB_TOKEN*.
You can omit the *VERSION*-tag if you want to install the latest version.

#### 1.2.2 ssh

Create a [ssh key and add it to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) for access. Make sure your ssh key is working:

```powershell
ssh -T git@github.com
```

```powershell
python -m pip install git+ssh://git@github.com/deloarts/pytia-ui-tools.git
```

If you're using poetry add this to you **pyproject.toml** file:

```toml
[tool.poetry.dependencies]
pytia-ui-tools = { git = "ssh://git@github.com/deloarts/pytia-ui-tools.git", branch="main" }
```

## 2 developing

For developing you would, additionally to the system requirements, need to install:

- [Poetry](https://python-poetry.org/docs/master/#installation)
- [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)

> ❗️ Never develop new features and fixes in the main branch!

### 2.1 clone the repo

Clone the repo to your local machine:

```powershell
cd $HOME
New-Item -Path '.\git\pytia-ui-tools' -ItemType Directory
cd .\git\pytia-ui-tools\
git clone git@github.com:deloarts/pytia-ui-tools.git
```

Or use GitHub Desktop.

### 2.2 poetry

#### 2.2.1 setup

If you prefer the environment inside the projects root, use:

```powershell
poetry config virtualenvs.in-project true
```

> ⚠️ Make sure not to commit the virtual environment to GitHub. See [.gitignore](.gitignore) to find out which folders are ignored.

#### 2.2.2 install

Install all dependencies (assuming you are inside the projects root folder):

```powershell
poetry install
```

Check your active environment with:

```powershell
poetry env list
poetry env info
```

Update dependencies with:

```powershell
poetry update
```

### 2.2.3 tests

Tests are done with pytest. Tests require a **tests.settings.json** file inside the [tests folder](tests/), which will be generated on your first run (or automatically on VS Code test discovery). Open this new file and fill out all required settings.

For testing with poetry run:

```powershell
poetry run pytest
```

> ⚠️ Test discovery in VS Code only works when CATIA is running.

#### 2.2.4 build

```powershell
poetry build
```

This exports the package to the [dist](/dist/) folder.

> ⚠️ Make sure not to commit dev-builds (the dist folder isn't ignored, because this package isn't published on pip yet).

### 2.3 pre-commit hooks

Don't forget to install the pre-commit hooks:

```powershell
pre-commit install
```

### 2.4 docs

Documentation is done with [pdoc3](https://pdoc3.github.io/pdoc/).

To update the documentation run:

```powershell
python -m pdoc --html --output-dir docs pytia_ui_tools
```

For preview run:

```powershell
python -m pdoc --http : pytia_ui_tools
```

### 2.5 new revision checklist

On a new revision, do the following:

1. Update **dependencies**: `poetry update`
2. Update the **version** in
   - [pyproject.toml](pyproject.toml)
   - [__ init __.py](pytia_ui_tools/__init__.py)
   - [README.md](README.md)
3. Run all **tests**: `poetry run pytest`
4. Check **pylint** output: `poetry run pylint pytia_ui_tools/`
5. Update the **documentation**: `poetry run pdoc --html --output-dir docs pytia_ui_tools`
6. Update the **lockfile**: `poetry lock`
7. Update the **requirements.txt**: `poetry export --dev -f requirements.txt -o requirements.txt`
8. **Build** the package: `poetry build`

## 3 license

[MIT License](LICENSE)

## 4 changelog

**v0.1.0**: Initial commit.  

## 5 to do

- [ ] Make more to-dos

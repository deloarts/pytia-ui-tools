# pytia ui tools

Helper functions and widgets for all pytia ui apps.

![state](https://img.shields.io/badge/State-beta-brown.svg?style=for-the-badge)
![version](https://img.shields.io/badge/Version-0.7.0-orange.svg?style=for-the-badge)

[![python](https://img.shields.io/badge/Python-3.10-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
![OS](https://img.shields.io/badge/OS-WIN10%20|%20WIN11-blue.svg?style=for-the-badge)

> ✏️ This package only provides helper functions, widgets and some other stuff for all pytia ui apps. This package is therefore a required dependency for almost all pytia apps, but does nothing on its own.
>
> ⚠️ The layout of this app is heavily biased towards the workflow and needs of my companies' engineering team.

Check out the pytia ecosystem:

- **pytia** ([web](https://pytia.deloarts.com/), [repo](https://github.com/deloarts/pytia)): The heart of this project.
- **pytia-property-manager** ([web](https://pytia.deloarts.com/property-manager/v0.html), [repo](https://github.com/deloarts/pytia-property-manager)) : An app to edit part and product properties.
- **pytia-bounding-box** ([web](https://pytia.deloarts.com/bounding-box/v0.html), [repo](https://github.com/deloarts/pytia-bounding-box)): For retrieving the bounding box of a part.
- **pytia-bill-of-material** ([web](https://pytia.deloarts.com/bill-of-material/v0.html), [repo](https://github.com/deloarts/pytia-bill-of-material)): Exports the bill of material and data of a product.
- **pytia-title-block** ([web](https://pytia.deloarts.com/title-block/v0.html), [repo](https://github.com/deloarts/pytia-title-block)): An app to edit a drawing's title block.
- **pytia-quick-export** ([web](https://pytia.deloarts.com/quick-export/v0.html), [repo](https://github.com/deloarts/pytia-quick-export)): Single file export with useful features.
- **pytia-reorder-tree** ([web](https://pytia.deloarts.com/reorder-tree/v0.html), [repo](https://github.com/deloarts/pytia-reorder-tree)): Brings order in your product graph tree.
- **pytia-ui-tools** ([web](https://pytia.deloarts.com/), [repo](https://github.com/deloarts/pytia-ui-tools)): A toolbox for all pytia apps.

Table of contents:

- [pytia ui tools](#pytia-ui-tools)
  - [1 installation](#1-installation)
    - [1.1 system requirements](#11-system-requirements)
    - [1.2 pip](#12-pip)
      - [1.2.1 pip from wheel](#121-pip-from-wheel)
      - [1.2.2 ssh](#122-ssh)
  - [2 developing](#2-developing)
    - [2.1 repository](#21-repository)
      - [2.1.1 cloning](#211-cloning)
      - [2.1.2 main branch protection](#212-main-branch-protection)
      - [2.1.3 branch naming convention](#213-branch-naming-convention)
      - [2.1.4 issues](#214-issues)
    - [2.2 poetry](#22-poetry)
      - [2.2.1 setup](#221-setup)
      - [2.2.2 install](#222-install)
    - [2.2.3 tests](#223-tests)
      - [2.2.4 build](#224-build)
    - [2.3 pre-commit hooks](#23-pre-commit-hooks)
    - [2.4 docs](#24-docs)
    - [2.5 new revision checklist](#25-new-revision-checklist)
  - [3 license](#3-license)
  - [4 changelog](#4-changelog)
  - [5 to do](#5-to-do)

## 1 installation

### 1.1 system requirements

- Windows 10/11
- [Python 3.10](https://www.python.org/downloads/)
- MS Outlook (optional)

### 1.2 pip

PYTIA isn't available on PyPi, but you still can install it via pip. Here are two options, choose the one you like best:

#### 1.2.1 pip from wheel

If you want to install PYTIA-UI-TOOLS from the published wheel file, use:

```powershell
python -m pip install https://github.com/deloarts/pytia-ui-tools/releases/download/v0.7.0/pytia_ui_tools-0.7.0-py3-none-any.whl
```

This command installs PYTIA-UI-TOOLS v0.7.0.

#### 1.2.2 ssh

Create a [ssh key and add it to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) for access. Make sure your ssh key is working:

```powershell
ssh -T git@github.com
```

```powershell
python -m pip install git+ssh://git@github.com/deloarts/pytia-ui-tools.git
```

This command installs the latest stable version of PYTIA-UI-TOOLS.

If you're using poetry add this to you **pyproject.toml** file:

```toml
[tool.poetry.dependencies]
pytia = { git = "ssh://git@github.com/deloarts/pytia-ui-tools.git", branch="main" }
```

## 2 developing

For developing you would, additionally to the system requirements, need to install:

- [Poetry](https://python-poetry.org/docs/master/#installation)
- [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)

### 2.1 repository

#### 2.1.1 cloning

Clone the repo to your local machine:

```powershell
cd $HOME
New-Item -Path '.\git\pytia-ui-tools' -ItemType Directory
cd .\git\pytia-ui-tools\
git clone git@github.com:deloarts/pytia-ui-tools.git
```

Or use GitHub Desktop.

#### 2.1.2 main branch protection

> ❗️ Never develop new features and fixes in the main branch!

The main branch is protected: it's not allowed to make changes directly to it. Create a new branch in order work on issues. The new branch should follow the naming convention from below.

#### 2.1.3 branch naming convention

1. Use grouping tokens at the beginning of your branch names, such as:
    - feature: A new feature that will be added to the project
    - fix: For bugfixes
    - tests: Adding or updating tests
    - docs: For updating the docs
    - wip: Work in progress, won't be finished soon
    - junk: Just for experimenting
2. Use slashes `/` as delimiter in branch names (`feature/docket-export`)
3. Avoid long descriptive names, rather refer to an issue
4. Do not use bare numbers as leading parts (`fix/108` is bad, `fix/issue108` is good)

#### 2.1.4 issues

Use the issue templates for creating an issue. Please don't open a new issue if you haven't met the requirements and add as much information as possible. Further:

- Format your code in an issue correctly with three backticks, see the [markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- Add the full error trace.
- Do not add screenshots for code or traces.

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
5. Update the **documentation**: `poetry run pdoc --force --html --output-dir docs pytia_ui_tools`
6. Update the **lockfile**: `poetry lock`
7. Update the **requirements.txt**: `poetry export --with dev -f requirements.txt -o requirements.txt`
8. **Build** the package: `poetry build`

## 3 license

[MIT License](LICENSE)

## 4 changelog

**v0.7.0**: Add ttkbootstrap themes.  
**v0.6.6**: Update pywin32 dependency.  
**v0.6.5**: Add groups to workspace model.  
**v0.6.4**: Add png folder to workspace model.  
**v0.6.3**: Bump pillow to 9.3.0.  
**v0.6.2**: Update deps due to vulnerability issue.  
**v0.6.1**: Remove dependency py.  
**v0.6.0**: Add file utility.  
**v0.5.3**: Add drawing export folder to workspace model.  
**v0.5.2**: Improve text editor.  
**v0.5.1**: Fix workspace encoding.  
**v0.5.0**: Add qr code functions.  
**v0.4.1**: Add configure method to SnapScale.  
**v0.4.0**: Add workspace handler.  
**v0.3.1**: Fix ScrolledText widget.  
**v0.3.0**: Add ScrolledText and text editor.  
**v0.2.0**: Add NumberVar.  
**v0.1.2**: Fix comma issue on NumberEntry.  
**v0.1.1**: Bump pillow to 9.1.1.  
**v0.1.0**: Initial commit.  

## 5 to do

Using VS Code [Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) to keep track of to-dos.

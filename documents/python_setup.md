# Getting Started

The Python workshop makes extensive use of [Jupyter Notebooks](https://jupyterlab.readthedocs.io/en/latest/user/notebook.html), a web-based interactive computing environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text. Jupyter Notebooks lets you write and execute code in small, easily modifiable code cells, which allow you to experiment and quickly see the results. 

## The Easy Way

The easy way to get set up is by installing the [Anaconda Python Distribution](https://www.anaconda.com/products/distribution), which contains all the modules and packages needed for this workshop, is available for all platforms, and provides a simple installation procedure. You can download the installer from the link above. You should be able to install it just like any other piece of software, but if you need detailed instructions, you can find them [here for Mac OS X](https://www.datacamp.com/tutorial/installing-anaconda-mac-os-x), or [here for Windows](https://www.datacamp.com/tutorial/installing-anaconda-windows).

The user guide for Anaconda is available [here](https://docs.anaconda.com/anaconda/user-guide/). To use Jupyter Notebooks, open the [Anaconda navigator](https://docs.anaconda.com/navigator/), and follow the instructions in the `Run Python in a Jupyter Notebook` section.

## The Interesting Way

If you’re feeling adventurous, you can try the manual installation. In the instructions below, we’ll setup packages to manage multiple Python installations (a way to avoid breaking complex code when versions of packages are updated), as well as Python itself, and Jupyter Notebooks.

# Instructions for MacOS   

We’ll start by installing [Homebrew](https://brew.sh/), a package manager for MacOS. Open `Terminal` and run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After Homebrew is successfully installed we can proceed to install [Pyenv](https://github.com/pyenv/pyenv), a version manager that allows you to install, manage, and switch between multiple versions of Python on your computer. Run the following command in the Terminal window:

```bash
brew install pyenv
```

Now we can install Python itself by running:

```bash
pyenv install 3.11.3
```

Next, we’ll install [Virtualenv](https://virtualenv.pypa.io/en/latest/), a tool that allows users to create isolated Python environments for different projects:

```bash
pip install virtualenv
```

Now we can create an environment for the workshop. First, let’s create a folder to store virtual environments. The commands below will create a folder called `Virtualenvs` in your `Home` directory (both can be changed if you prefer a different folder name or location), and then move there:

```bash
mkdir ~/Virtualenvs
cd ~/Virtualenvs
```

To create the environment, run:

```bash
pyenv virtualenv 3.11.3 intro_to_python
```

Virtual environments need to be activated in order to be used. The following command activates the environment we just created:

```bash
pyenv activate intro_to_python
```

Once the virtual environment is activated, we can use `pip` to install packages specific to that environment. For example, to install the `Jupyter` package, run the following command:

```bash
pip install jupyter
```

Lastly, to start Jupyter notebooks, run:

```bash
jupyter notebook
```

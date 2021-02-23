Development environments
========================

Many modern programming langauges, such as Python, make it very easy to access libraries of code which are written and maintained by other people.
A good example of this in Python is the ``numpy`` package.

This ease of installation comes with some downsides, especially when it comes to making your code available to other people in the future, and making sure that they can run it.
Keeping track of the "dependencies": the software libraries which your code relies on can be helped by running your code inside its own development environment.
This also allows you to install different versions of various libraries without causing problems for other code which might use it on your machine.

There are two common approaches to managing development environments in Python; ``venv``, which comes packaged with Python, and ``conda`` environments, which are part of the ``anaconda`` distribution of Python.

Python virtual environments
---------------------------

Python virtual environments isolate all of the load paths for Python code from your operating system, so that Python will only look in that environment for libraries when it tries to import them, and doesn't search among libraries installed in the system.

You can make a new environment by running this command:

.. code-block:: console

   $ python3 -m venv /path/to/new/virtual/environment

There are a couple of different approaches which are sensible with regards to choosing a location for your virtual environment.
I prefer keeping them in a directory inside my ``$HOME`` directory, so for me a typical way of creating a new virtual environment would be

.. code-block:: console

   $ python3 -m venv ~/.virtualenvs/newenvironment

A good alternative to this is keeping them in the same directory as the rest of your project.
However, you should be careful with this not to add the environment directory accidentally to your repository.

.. sidebar:: ``.gitignore``

   You can add this directory to your ``.gitignore`` file, which is a text file you can create in the root directory of your repository.
   If you make your environment in a directory called ``env`` then adding a line with ``env/`` to your ``.gitignore`` will prevent it being accidentally staged or committed.

Once you've made the environment you'll need to activate it.
You can do this by running

.. code-block:: console

   $ source /path/to/environment/bin/activate

You'll need to run this line each time you open a new terminal where you want to use the environment.
You can leave the environment by running

.. code-block:: console

   $ deactivate

When the environment is active you can use python normally, and you can install packages which you need for your code using pip.
For example:

.. code-block:: console

   (env) $ pip install numpy

By default the virtual environment will append its name to the prompt in the terminal.
   
Conda environments
------------------

Conda environments (see their `documentation`_) are designed to solve similar problems to python's ``venv`` environments, but they offer some additional flexibility.
They're integrated into the anaconda ecosystem, so they can be used for managing non-python libraries as well.

Creating a conda environment is very similar to a ``venv``:

.. code-block:: console

   $ conda create --name env

It will then suggest a location to store the environment. Type :kbd:`y` if you're happy with this.

You can then activate a conda environment by running

.. code-block:: console

   $ conda activate env

Replacing ``env`` with the name of your environment.

Like with a ``venv`` you can run ``pip`` inside a conda environment, however you should be causious of mixing this with conda's own package management tool if you're using it.

.. _`documentation`: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Using different python versions with Pyenv
------------------------------------------

There may come times when you need a different version of python from the one which is installed on your system.
If this is the case you have two simple options; either using a conda environment, or installing `pyenv`_.

Once you've followed the installation and setup of ``pyenv`` you can install new versions (e.g. ``3.8.0``) of python using

.. code-block:: console

   $ pyenv install 3.8.0

You can then specify this as the python version you want to use for a venv by first activating this python version:

.. code-block::

   $ pyenv shell 3.8.0
   $ python -m venv environment
   $ source environment/bin/activate

.. _`pyenv`: https://github.com/pyenv/pyenv

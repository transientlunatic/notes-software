Packaging software
==================

Once you've got some code which you want to make available, be it to collaborators, or more widely to the public, it's time to start thinking about packaging the code so that it can be installed on other computers.

There are a few considerations before we get to the actual mechanics of producing a software package.
Perhaps the most important is choosing a license for your software: that is, explicitly stating what other people are allowed to do with your code, and how that applies to your legal rights to retain copyright.

Licensing your code
-------------------

.. note:: This is not legal advice.

   Your funder or employer may have specific requirements of how you handle intellectual property.
   It's worth checking what their policies are before choosing a license if you're in any doubt.

In order to allow other people to download and use your code you'll need to explicity permit it.
This is normally done by *licensing* your code under some pre-existing software license; the choice of license affects what people are able to do with your code, the extent to which it can be modified.

In this section I assume that you'll be releasing code as *open-source* software, which means that the end-user will have open access to the code which you wrote.
This is good practice with respect to reproducibility of results from your software.
However, if you need to protect the code for some reason you'll probably need some form of proprietary license.

Open source licenses fall into two broad categories: "permissive" and "copyleft".
In terms of the rights which a user gets under both of these families of contract they are broadly comparable.
Generally a user is permitted to run, read, copy, and modify your code under both types of license.
They're also allowed to redistribute your code, but they can't change the license attached to it.

The main difference arises with a practice known as "sub-licensing", and specifically whether parts of your code can be used in another project which uses a different license.

Copyleft & GPL
~~~~~~~~~~~~~~

The two major "copyleft" licenses are the ``GNU General Public License`` and the ``Creative Commons share-alike`` licenses.
Both of these licenses allow your code to be used by other people, as well as modified.
People are free to both redistribute your code, and redistribute modified versions, however these must be distributed under the same license as your code.
In practical terms this means that your code can't be modified to be incorporated in paid-for software.

Permissive licenses
~~~~~~~~~~~~~~~~~~~

Permissive licenses aim to be much less restrictive, and are often much shorter.
Popular examples are the BSD licenses, the MIT license, and the ISC license.


Adding a license to your repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's standard practice to include a file with the text of your license in the root of your project repository, with the name LICENSE.
For example, if you were using the MIT license this would be a file containing the following text:

.. code-block:: rst

   Copyright (c) <year> <copyright holders>

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

Services such as Github may allow you to add a file with the license automatically when you're creating the repository.

Versioning
----------

.. _`setuptools_scm`: https://github.com/pypa/setuptools_scm/

Packaging with python
---------------------

Organising your code
~~~~~~~~~~~~~~~~~~~~

In this tutorial I'm going to make a very simple package which only does a few things.
In fact, it only does one thing, which is to make up contrived names for python packages.

.. code-block:: python

   import random
   def generate_name():
	   """
	   Generate a randomised package name, e.g. "lachrymose_manatee" or "parsimonious_spider".
	   """
	   animals = ["rabbit", "gull", "spider", "manatee", "pug"]
	   adjectives = ["adamant", "boorish", "didactic", "lachrymose", "parsimonious"]

	   return "{}_{}".format(random.choice(adjectives), random.choice(animals))

What’s in a name?
~~~~~~~~~~~~~~~~~

It’s important to have a name for our package, and it’s useful to follow
some guidelines for this:

1. Make the name all lowercase
2. Make sure there isn’t a package with that name already on
   pypi.python.org
3. Don’t include spaces or hyphens in the name, so “lachrymose_manatee”
   is fine, but “parsimonious possum” wouldn’t be.

Let’s go ahead and call ours “lachrymose_manatee” (though more normal
human beings might choose a more descriptive name).

Planning the package
~~~~~~~~~~~~~~~~~~~~

The structure of a python package is dictated by the structure of the directories which make it up.
Let’s assume that we’ve been sensible and put our code into a git repository.
To start making our project we should have a directory structure inside our repository like this:

::

   .
   ├── lachrymose_manatee
   │   └── __init__.py
   └── setup.py

It may seem slightly odd that there’s a directory with the name of the project inside your repository, but this is just the structure which is most commonly used for python packages.

In order to make a directory into a module we need to add an ``__init__.py`` file.
This is the file which will be loaded when you run ``import lachrymose_manatee`` in a project.
We can add the ``generate_name()`` function to this file.

The other essential file is the ``setup.py`` in the root of the repository.
This file contains the information which python needs to install the code.
It can contain normal python code, but it needs a call to the ``setuptools.setup()`` function, so a minimal ``setup.py`` would look something like this:

.. code:: python

   from setuptools import setup

   setup(name='lachrymose_manatee',
         version = 0.1,
         description = "Generates fun and pretentious names for packages.",
         author = "Daniel Williams",
         author_email = "daniel.williams@ligo.org",
         license = "MIT",
         packages = ["lachrymose_manatee"],
         python_requires='>=3.5'
         zip_safe = False)

You can then install your package by running ``pip install .`` in the root directory of the repository.
(It’s now considered bad practice to run ``python setup.py install`` directly in the repository, as this causes python to skip some of the checks which it really should be doing on packages.)


Python & Poetry
---------------

Publishing your code
--------------------

Ideally you’d now want everyone in the world to be able to easily install your fantastic new package by running ``pip install lachrymose_manatee`` so that everyone can have entertainingly named code.

To do this we need to upload it to the python package index, PyPI.

First we need to install ``wheel``, which is used for creating binary distributions of python code.

.. code:: bash

   $ pip install wheel

We can prepare a package to be uploaded by running

.. code:: bash

   $ python setup.py sdist bdist_wheel

This will create a directory called ``dist`` which will contain packaged versions of your code, ready to be shipped to other users.

To upload this to the package repository we need another package, ``twine``:

.. code:: bash

   $ pip install twine

We can then use this to upload our package to PyPI:

.. code:: bash

   $ twine upload dist/*

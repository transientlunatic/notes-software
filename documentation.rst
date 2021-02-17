Documenting code and projects
=============================


It's generally a good idea to make sure that you document your code.
Whether you expect to be the only person using it, or you're writing it for a wider audience, making it clear what the code is meant to do, how it does it, and how you use it is an important part of the software development process.

It's generally a good idea to make sure you set some time aside to document your code as you go along, and this document will discuss some of the tools which can make this easier.

.. note:: This section uses Python as its example langauge and development environment. However, documentation tools exist for all languages which you're likely to encounter.

The README file
---------------

The most fundamental unit of documentation in most software projects is the ``README`` file.
This is traditionally a plain text file which sits at the root of your project's directory structure (that is, at the root of the project repository in the era of version control).

Modern code-sharing websites such as Github allow you to add some additional formatting into a README file, and can support a variety of markup formats, such as ``markdown`` and ``restructured text``.
``Markdown`` is probably the most common of these (you'll spot these as ``README.md`` files in projects), but ``restructured text`` is common in python projects, because it's the format which python documentation is often written in.

.. note::

   I'm going to use ``restructured text`` (rst) in the examples here so that everything's consistent when I discuss other documentation tools.
   Markdown is a little less complicated, so you may find that's easier to use.
   You can find various tutorials and cheatsheets online for it.

The README file behaves a bit like a front page for your project, and it's a good idea to make sure that it covers a number of important pieces of data concisely:

- The name of the software
- A brief description of the software
- A "getting started" section
- Installation instructions
- A brief summary of the software's features [this one's a bit more optional]
- A brief guide for potential contributors
- A brief description of the copyright on the code, and license you're releasing your software under

I'll discuss things like :ref:`licensing` in the discussion about publishing your code.

Let's quickly look at a very minimalist README file for inspiration:

.. code-block:: rst

   Example Project
   ---------------

   This is an example project which is used to motivate projects which are perhaps more useful.
   It's meant to be the simplest example the author can think of.

   Getting started
   ---------------

   .. code-block:: rst

      $ foo

   at the command line.

   Installation
   ------------

   You can install this example by running

   .. code-block:: console

      $ pip install example

   Or you can install it from source using ``Make``:

   .. code-block:: console 

      $ ./configure
      $ make
      $ make install

   Features
   --------

   - Can explain how to write README files
   - Can help you learn to document code better than before

   Contributing
   ------------

   If you'd like to contribute to this project please fork its repository, and submit changes as a pull request on Github.

   License
   -------

   The code of the ``example`` project is copyright 2021 Daniel Williams, and is licensed under the MIT license.

From this example you can see the general gist of what should go into a README file, to give someone an impression of what the project does at a glance.


.. note:: Even if you don't intend to distribute you code widely a README can be valuable even for your own purposes; trying to work out what a repository does a decade after you made it can be challenging!

If you're looking for inspiration for good README files take a look at the `awesome README`_ repository on Github.

.. _`awesome README`: https://github.com/matiassingers/awesome-readme

Code-level documentation
------------------------

As your project gets larger the amount of code you need to remember the ins and outs of is going to increase.
It can be time consuming to need to read-through your own code months or years down the line just to remember details of how some function or class works, however.

This is where we turn to "code-level" documentation, where we describe the code itself, and things like which arguments each function takes, and what it returns.

We can also add comments in the middle of the code to clarify lines which might be especially confusing or unclear.

All programming languages have a syntax for comments, and most have an additional syntax for multi-line comments.
In python anything on a line following a ``#`` character becomes a comment.
Python also designates a special string following a function or a class definition as a "doc string".

Let's have a look at a function as an example:

.. code-block:: python

   def example(pigs, blankets):
       """
       This function wraps pigs in blankets.

       Parameters
       ----------
       pig : str
          A digital pig object.
       blanket : str
          The digital blanket with which to wrap the pig.

       Returns
       -------
       wrapped_pig : str
          A cosy and enrobed digital pig.
       """

       wrapping = pig + blanket
       # The pig must be wrapped on both sides
       wrapping = blanket + wrapping

       return wrapping

We can see examples of both a comment and a docstring; the former as a line within the code starting with a ``#`` character, and the latter as text wrapped by three double-quotes, but not assigned to a variable.
The docstring must be the first thing in the function for python to identify it as a docstring rather than a normal string literal within the code.

.. sidebar:: ``"""what's this?"""``

   There's nothing especially magical about the triple double quotes; it's how Python designates multi-line strings (also called `HERE docs`_ in other contexts).

Anything can go into a docstring, however judicious choice of formatting can make your life much easier, and if you're working on someone else's code you may be asked to follow a given standard.
The one I used in the example above uses the `numpydoc`_ standard, which was developed for documenting the large and complex ``numpy`` library.
One of the advantages of following a standard like this is that it allows automated tools to read your docstrings and assist with the process of building documentation.


.. _`HERE docs`: https://en.wikipedia.org/wiki/Here_document
.. _`numpydoc`: https://numpydoc.readthedocs.io/en/latest/

Additional documentation
------------------------

Normally you'll need to include more information about your code than just details of how the code itself works, but which is too lengthy for the README file.

It's a good practice to keep a directory in your project for this: calling it ``docs`` is a common practice.
Here you can keep additional details explaining how to build the code in more detail, tutorials, and notes.

Again, in python is is common practice to write these in ``restructured text`` format, but this will depend on the choice of tool you make for converting your documentation into something more accessible, using a :ref:`documentation building tool<docbuilders>`.

.. _docbuilders:
Documentation builders
----------------------

Once you've written your documentation chances are you'll want to be able to read it.
While text files in your repository might be an effective solution for smaller projects you may eventually want a way to give more structure to your documentation, and automate some of the tasks required in making really useful docs.

There are many such tools, two of the most frequently encountered are ``doxygen`` and ``sphinx``.
Both are capable of producing documentation for projects written in a variety of languages, but I'll focus on ``sphinx`` here, which was developed to document the python language, and which is now widely used in scientific python codes.

.. sidebar:: This document

   This document is in fact written using ``sphinx``! It's more flexible than just being for code!

You can install ``sphinx`` using ``pip``:

.. code-block:: console

   $ pip install sphinx

Then to set things up in a directory called ``docs`` you can run

.. code-block:: console

   $ sphinx-quickstart docs

in the root of your project repository. Sphinx will then ask you some questions about your project.
Answer these, and it will set up a few files to get you started.

So, for example,

.. code-block:: console
   
   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   > Separate source and build directories (y/n) [n]: n

   The project name will occur in several places in the built documentation.
   > Project name: SWC Example
   > Author name(s): Daniel Williams
   > Project release []: v1.0

   If the documents are to be written in a language other than English,
   you can select a language here by its language code. Sphinx will then
   translate text that it generates into that language.

   For a list of supported codes, see
   https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
   > Project language [en]: en

   Creating file /home/daniel/tmp/swc/docs/conf.py.
   Creating file /home/daniel/tmp/swc/docs/index.rst.
   Creating file /home/daniel/tmp/swc/docs/Makefile.
   Creating file /home/daniel/tmp/swc/docs/make.bat.

Here I've mostly used the default options, and it's made four different files.
Two of these are useful utilities: ``Makefile`` and ``make.bat`` allow us to simply run ``make html`` in the ``docs`` directory in order to produce a website for the documentation.

The ``index.rst`` file will serve as the home page (or first page, depending on the format we convert things into), and ``conf.py``, which contains the settings required to generate the documentation.

The configuration file
~~~~~~~~~~~~~~~~~~~~~~

Let's look at the ``conf.py`` file first.

.. sidebar:: Getting meta

   This is in fact the ``conf.py`` responsible for making this page.

.. literalinclude:: conf.py
   :language: python

There's not too much to pick apart here; this is a normal python program, so we can import things into it as normal.
The import at the top, for ``kentigern`` loads the theme which sphinx uses on these pages.
Many of these are available, but the default one (called ``alabaster``) which ``sphinx-quickstart`` uses doesn't need to be imported.

Then there are a few variables which need to be set (and which ``sphinx-quickstart`` should have set up for you) with the name of the project, some copyright information, and the name of the author.
The release number should normally correspond to the release number of your code.

Trivially the ``extensions`` variable can just be an empty list, but as we'll see shortly, there are a number of extensions which can make your life easier.
The ``templates_path`` and ``exclude_patterns`` variables can normally be left alone.

The ``html_theme`` variable allows you to change the theme applied to the web pages sphinx produces.
Take a look at the `sphinx themes`_ documentation for more details about this.
Similarly, ``html_theme_options`` lets specific options be passed to that theme.

.. _`sphinx themes`: https://www.sphinx-doc.org/en/master/usage/theming.html

The index
~~~~~~~~~

The ``index.rst`` file which ``sphinx-quickstart`` is just a restructured text file like any other you might write, but it will include a few additional bits of data: called ``directives`` which allow sphinx to infer the structure of your documentation.

Let's take a look at the ``index.rst`` for this website.

.. literalinclude:: index.rst
   :language: rst

The thing to look out for here is the block which starts with the line ``.. toctree::`` which is a special directive to build the table of contents. Underneath that there are some options (lines like ``:caption: Contents``), which we can gloss over for now, but after a new line there is an indented list of pages.

Each of these is a restructured text file which lives in the same directory as ``index.rst`` (but we can skip the file extension, so ``ci`` refers to the file ``ci.rst``).
When the table of contents is generated the files will appear in this order.
To be included in the final documentation a file needs to appear inside a table of contents (though you can have multiple different tables of contents throughout your documentation).

You can build your documentation by running

.. sidebar:: Other formats

   Sphinx can build a large number of alternative formats; try running just ``make`` for a list of them.

.. code-block:: console

   $ make html
   
which will generate a website (if you chose the defaults in ``sphinx-quickstart`` these will be in a directory inside your current directory, called ``_build/html``)

Auto-building documentation
---------------------------

Publishing your documentation
-----------------------------

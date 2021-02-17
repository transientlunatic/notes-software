Testing your code
=================

Suppose you collaborate on writing code: how do you make sure none of your collaborators break your code? The answer: introduce quality controls.
We can do this by testing the code frequently.
To make sure you do this (and do it consistently), we should automate this process, so that we can make sure it happens every time that the code is committed to your repository.

.. note::

   As with other parts of this book, the tools and examples in this chapter use python as an example.
   The principles which are being introduced are very general, however, and the vast majority of mature programming languages will have testing toolkits available or built-in.

Static Analysis
---------------

The simplest level of quality control which most large coding projects expect (or sometimes demand) is that your code follows a given "style guide".
Much like how different publishers will have a view on whether an article should (or should not) make use of the serial (so-called "Oxford) comma, project maintainers will often have strong feelings about the formatting of code in their codebase.
This can be both for performance reasons, and to make reading the code easier.

While it's less important to do this if you're working along on your own code, it can still be helpful to maintain some conventions (such as capitalising the names of classes, in the case of Python).
A popuarly used style guide for Python is `PEP8`_, which aims to make your code as readible as possible.

Enforcing, or checking that code follows a given set of guidelines can be done with tools which perform "static analysis" on the code.
These read and parse the code, but they don't actually run it.
They then check the code against a style guide, and against the grammar rules for the language, and attempt to indentify problems.

Two of the most popular analysis tools for Python are ``Pylint`` and ``flake8``.
These have overlapping feature sets, but running both can sometimes be helpful.

To get to grips with what these do, let's take two different code examples; the first one has good style, and the other bad.

.. literalinclude:: goodstyle.py
   :language: python
   :linenos:

.. literalinclude:: badstyle.py
   :language: python
   :linenos:
      
``Pylint``
~~~~~~~~~~

Pylint tries to identify a series of stylistic errors in your code, and then provide a score at the end.

The code in ``goodstyle.py`` does pretty well:

.. code-block:: console

   $ pylint goodstyle.py
		
   ------------------------------------
   Your code has been rated at 10.00/10

But we score a 0/10 for our ``badstyle.py`` code...

.. code-block:: console

   $ pylint badstyle.py
		
   bad-style.py:5:0: C0303: Trailing whitespace (trailing-whitespace)
   bad-style.py:10:0: C0303: Trailing whitespace (trailing-whitespace)
   bad-style.py:1:0: C0114: Missing module docstring (missing-module-docstring)
   bad-style.py:2:0: C0103: Function name "HelloWorld" doesn't conform to snake_case naming style (invalid-name)
   bad-style.py:2:0: C0116: Missing function or method docstring (missing-function-docstring)
   
   ------------------------------------
   Your code has been rated at 0.00/10

The linter tells us which line the problem arises in (the first warning is for line 5, for example), and then gives a short description of how the code is breaking the style guide.


``flake8``
~~~~~~~~~~

The good code provides no output, as no problems are found.

.. code-block:: console

   $ flake8 goodstyle.py

For the badly styled code we get a series of errors and warnings.


.. code-block:: console

   $ flake8 badstyle.py

   bad-style.py:2:3: E999 IndentationError: unexpected indent
   bad-style.py:2:4: E111 indentation is not a multiple of four
   bad-style.py:2:4: E113 unexpected indentation
   bad-style.py:2:25: E251 unexpected spaces around keyword / parameter equals
   bad-style.py:2:27: E251 unexpected spaces around keyword / parameter equals
   bad-style.py:5:1: W293 blank line contains whitespace
   bad-style.py:6:7: E303 too many blank lines (3)
   bad-style.py:6:7: E111 indentation is not a multiple of four
   bad-style.py:7:11: E111 indentation is not a multiple of four
   bad-style.py:7:16: E225 missing whitespace around operator
   bad-style.py:8:7: E111 indentation is not a multiple of four
   bad-style.py:9:11: E111 indentation is not a multiple of four
   bad-style.py:9:16: E225 missing whitespace around operator
   bad-style.py:11:7: E111 indentation is not a multiple of four

You can see that in comparison to ``pylint`` there's a lot of output, and a lot of it relates to spacing and line breaks.
I'll pull-out the ``E111 indentation is not a multiple of four`` lines for special mention.
These are grumbling about the use of tabs to indent code rather than four spaces; either will work (though spaces are generally preferred in most style guides). However, if you're using ``python3`` then you can't mix both indenting styles in the same file.

.. _`PEP8`: https://pep8.org/

Unit testing
------------

.. code-block:: console

   $ python -m unittest discover -s tests/unit

.. _`hitchhiker`: https://docs.python-guide.org/writing/tests/

End-to-end testing
------------------

.. code-block:: console

   $ python -m unittest discover -s tests/integration

While testing individual methods and functions can be valuable for identifying bugs and breaking changes which are caused by

.. _`pytest integration`: https://doc.pytest.org/en/latest/goodpractices.html

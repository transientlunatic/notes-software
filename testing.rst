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

While static analysis can show up problems with the syntax or the style of your code, most bugs won't show-up until you've actually executed the code.
There are a few approaches to testing your code for these sorts of bugs.
The simplest is called "unit testing", where individual units of code are run, and the behaviour of the unit is examined.
In Python a unit is likely to be a function or a class method.

Units are tested in isolation from each other, which allows problems to be identified quickly, but generally aren't a realistic representation of how code is used; I'll cover the additional methods for this later in this chapter.

There are a number of tools in Python to help you create tests; I'll use the ``unittest`` library here, because it's part of the standard python libraries which should be present in any python installation.
Other tools, such as ``Pytest`` make some things simpler, however.

Let's write a function which we want to test; this is one which checks if a given input is prime.

.. literalinclude:: examples/prime.py
   :language: python

Now, this is a very simple function, which just searches for factors of a number.
If it can't find any it returns ``True``, since that number is prime.

We want to test this; there are some things we might regard as "edge cases" which we should look out for, and we should check that it actually identifies a prime number correctly.
Here are some things I can think of which we might want to check are handled correctly:

- Is 2 identified as prime?
- Is 1 identified as not prime?
- What happens when 0 or a negative number is provided?
- What happens if the input isn't an integer?

Before we even start writing tests we can see that we actually need to put some thought into answering some of these, especially the last two.
We need to define a behaviour in both cases, since it's likely that most approaches we'll take to writing an algorithm won't cover these.
This highlights one of the reasons that writing tests is important: they can act like a design specification for your code.
In fact, practitioners of `test-driven development`_ would suggest that you should write the tests before you write any code.

.. sidebar:: Test-driven development

   There's a lot of merit in this approach, but it can be difficult to get started.
   In this chapter I'm starting with a simple unit of code, but once you understand the basics of writing tests I would strongly encourage you to introduce test-driven principles into some or all of your development.

Let's look at an example test.

.. code-block:: python

   def is_prime(number):
    """Test if a number is prime. Return True if prime, and False if not."""
    for i in range(number):
        if number % 2 == 0:
            return False
        elif (num % i) == 0:
            return False
        else:
            return True

So, what's going on here?
Well, fundamentally this file is just a python script, and we've added in some *boilerplate* to help the ``unittest`` tool do its job.
The first thing is importing both ``unittest`` and our function (which lives in a file called ``prime.py``).
The tool groups together tests into classes, with each individual test defined by a method on that class.
The class needs to inherit the ``unittest.TestCase`` class.

.. note::
   Don't worry if you're not too clear on what's going on here with things like class inheritence, it just gives our testing class access to a number of additional tools from the library.
   For now you can just modify these samples, and as you get more confident in what you're doing you can consult the `documentation`_ on writing more complex tests.

The code which defines the test is contained in the ``test_number_two`` method.
All that is does is evaluate the ``is_prime`` function, and checks that it returns ``True``.
The ``assertTrue`` method is one of the methods which ``unittest`` provides to help us; if the result is ``False`` it will cause the test to fail.

Let's run the test.
I've saved the script above in a file called ``test_prime.py``.
In order to run the test I need to call ``python`` on it with an additional option, ``-m unittest``:

.. code-block:: console

   $ python -m unittest test-prime.py

   F
   ======================================================================
   FAIL: test_number_two (test-prime.PrimeTests)
   Test that two is prime.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
   File "test-prime.py", line 9, in test_number_two
   self.assertTrue(is_prime(2))
   AssertionError: False is not true

   ----------------------------------------------------------------------
   Ran 1 test in 0.000s

   FAILED (failures=1)

Well, you can see that we didn't exactly pass with flying colours...
Looking back at the code we can see that it will reject all even numbers as non-prime; we need to handle 2 differently.

Adding a case in the if statement for 2 is one way to do this:

.. code-block:: python

   def is_prime(number):
      """Test if a number is prime. Return True if prime, and False if not."""
      if (number == 2):
          return True
      for i in range(number):
          if number % 2 == 0:
              return False
          elif (num % i) == 0:
              return False
          else:
              return True

Now our test gives us:

.. code-block:: console
		
   $ python -m unittest test-prime.py
   
   .
   ----------------------------------------------------------------------
   Ran 1 test in 0.000s
   
   OK

Which is good! We've fixed a problem in our code!
Let's go on to write tests for the remaining conditions I identified earlier.

.. code-block:: python

   import unittest
   from prime import is_prime

   class PrimeTests(unittest.TestCase):
       """Test prime number checking."""

       def test_number_two(self):
	   """Test that two is prime."""
	   self.assertTrue(is_prime(2))

       def test_number_one(self):
	   """Test that one is not prime."""
	   self.assertFalse(is_prime(1))

       def test_number_zero(self):
	   """Test that zero is not prime."""
	   self.assertFalse(is_prime(0))

       def test_number_negative(self):
	   """Test that negative numbers are not prime."""
	   self.assertFalse(is_prime(-3))

       def test_actual_prime(self):
	   """Test that a known prime is prime."""
	   self.assertTrue(is_prime(13))

Running this we find that there are still problems:

.. code-block:: console

   E.E..
   ======================================================================
   ERROR: test_actual_prime (test-prime.PrimeTests)
   Test that a known prime is prime.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "/home/daniel/academic-notes/notes-software/examples/test-prime.py", line 25, in test_actual_prime
       self.assertTrue(is_prime(13))
     File "/home/daniel/academic-notes/notes-software/examples/prime.py", line 8, in is_prime
       elif (num % i) == 0:
   NameError: name 'num' is not defined

   ======================================================================
   ERROR: test_number_one (test-prime.PrimeTests)
   Test that one is not prime.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "/home/daniel/academic-notes/notes-software/examples/test-prime.py", line 13, in test_number_one
       self.assertFalse(is_prime(1))
     File "/home/daniel/academic-notes/notes-software/examples/prime.py", line 8, in is_prime
       elif (num % i) == 0:
   NameError: name 'num' is not defined

   ----------------------------------------------------------------------
   Ran 5 tests in 0.001s

   FAILED (errors=2)

The first line here, ``E.E..`` reveals that two of the tests had errors; the first and third ones which were run.
Then there are individual messages which reveal why the test couldn't finish; there's a bug in the code! ``num`` isn't defined.
If we fix this (changing ``num`` to ``number``) and run again... only to find another error.

.. code-block:: console

   $ python -m unittest test-prime.py

   E.E..
   ======================================================================
   ERROR: test_actual_prime (test-prime.PrimeTests)
   Test that a known prime is prime.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "/home/daniel/academic-notes/notes-software/examples/test-prime.py", line 25, in test_actual_prime
       self.assertTrue(is_prime(13))
     File "/home/daniel/academic-notes/notes-software/examples/prime.py", line 8, in is_prime
       elif (number % i) == 0:
   ZeroDivisionError: integer division or modulo by zero

   ======================================================================
   ERROR: test_number_one (test-prime.PrimeTests)
   Test that one is not prime.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "/home/daniel/academic-notes/notes-software/examples/test-prime.py", line 13, in test_number_one
       self.assertFalse(is_prime(1))
     File "/home/daniel/academic-notes/notes-software/examples/prime.py", line 8, in is_prime
       elif (number % i) == 0:
   ZeroDivisionError: integer division or modulo by zero

   ----------------------------------------------------------------------
   Ran 5 tests in 0.001s

   FAILED (errors=2)

This one's a result of choosing to use ``range(number)``; we can update this to ``range(2, number)`` and get...

.. code-block:: console

   .....
   ----------------------------------------------------------------------
   Ran 5 tests in 0.000s

   OK

We've passed our tests!

.. sidebar:: Non-integers

   There are a couple of plausible approaches for this which I'll lay out.
   One option is that you have your function ``raise`` a ``ValueError`` if ``type(number) != int``, and then test using an ``assertRaise`` that the correct exception gets raised.
   Alternatively you could define anything else as non-prime; the best solution will vary depending on the scenario, though I'd generally favour the former.

I've still not included a test for non-integer input, but that one, in classical academic style, is left as an exercise to the reader.

As your codebase evolves you're likely to end-up with large amounts of code you'll need to test.
A good practice here is to keep all your test scripts in a directory called ``tests`` within your project repositorty.
It can also be a good idea to separate the unit tests into their own ``tests/unit`` directory.

``unittest`` can then be used to run all the tests in that directory using the command

.. code-block:: console

   $ python -m unittest discover -s tests/unit

For this to work the scripts need to have names of the form ``test_foo``; the individual test classes in those scripts should have names starting in ``Test``, such as ``TestSpam``, and then the individual test methods should have names like ``test_eggs``.

.. _`hitchhiker`: https://docs.python-guide.org/writing/tests/
.. _`test-driven development`: https://en.wikipedia.org/wiki/Test-driven_development
.. _`documentation`: https://docs.python.org/3/library/unittest.html

Coverage
~~~~~~~~

Unit testing is most useful when all of the code in the codebase is checked by your test suite.
*Code coverage* is a measure of the fraction of lines of the code which are run by a given test suite.

A tool called ``coverage.py`` can be used to assess this for the unittests in this section.
You can install it by running

.. code-block:: console

   $ pip install coverage

and then changing the way that you call your tests to

.. code-block:: console

   $ coverage -m unittest test-prime.py

This will gather the information which is needed to measure the coverage, and a report can be made by running

.. code-block:: console

   $ coverage report -m
   Name            Stmts   Miss  Cover   Missing
   ---------------------------------------------
   prime.py            9      2    78%   7, 9
   test-prime.py      13      0   100%
   ---------------------------------------------
   TOTAL              22      2    91%

So we can see lines 7 and 9 are never called by our test suite as it currently stands.

End-to-end testing
------------------

Testing that individual functions produce the results we expect is a powerful technique, but it doesn't reflect the way that code actually runs.
End-to-end, or *integration* testing is used to ensure that several units of code interact the way that we expect.

Writing integration tests doesn't differ much from writing a unit test, but we need to include all the components of the workflow.
This is why separating these from unittests can be sensible; your code might take minutes or hours to run its integration tests, and running them every time we make a change might be time consuming. Instead, by keeping them in e.g. a ``tests/integration`` directory we can run them with

.. code-block:: console

   $ python -m unittest discover -s tests/integration


Regression testing
------------------

When you add new features or tidy-up (refactor) code, you want to ensure that it continues to provide the same results as older versions of the code.

This is where *regression* testing comes into play.
The way that you go about writing this type of test will vary depending on how your code works, but also if you have external requirements, such as whether the code needs to be able to reproduce reviewed results.

For example, if you have a set of reviewed results, you could write a test script which attempts to reproduce these under the same configuration, and checks that the results are still produced after the code is updated.

.. _`pytest integration`: https://doc.pytest.org/en/latest/goodpractices.html

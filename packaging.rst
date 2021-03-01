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

Python & Poetry
---------------

Publishing your code
--------------------

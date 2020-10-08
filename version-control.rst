Version Control
===============

When writing code, in any language, it can be useful to make sure that you have a way of keeping track of how the entire codebase changes over time.
Specialised software for managing the process of tracking these changes are called **version control systems**.
There are a number of different systems available, but in these notes I'll focus on one called ``git``, which has come to dominate both the world of scientific computing and the more general open-source software community in the last decade.

Most version control systems follow similar principles, however ``git`` possesses some idiosyncracies which other systems don't have.
Some of these are by design, and some of these are a result of its own history.
I'll try and note situations where ``git`` does something unusual or potentially confusing as we go along, and try to justify (where I can) why it does things that way.

If you're starting a new project I **strongly** recommend using ``git`` to operate its source control.
You may, however, encounter older systems if you're working with an older codebase (though even then many of these are moving to use ``git`` thanks to widespread community support, and websites like Gitlab and Github, which I'll talk more about later).

.. note::
   Before we go on, if you need to find out something about ``git`` which isn't covered in these notes (and there are *many* things about ``git`` which are beyond their scope) you can find the excellent Git book free online: https://git-scm.com/book/en/v2
   Printed copies can also be purchased from Apress.



What is version control?
------------------------

(And why do I need it?)

Most modern version control systems are designed to make it easier for teams of people to work on the same large codebase at the same time, but that's not the only situation they're useful for.
Take an example: you're working on a piece of code (or maybe event a document [or a thesis!]) and you make some changes.
You then go away for a while, and a few weeks later you discover those changes have had some unintended consequence, and you wish you were able to just hit an undo button and go back to what happened before.
Well, this is what version control, at its most fundamental level, is designed to do.
When you register a file with a version control system it starts keeping track of the changes which you make to the file, and it lets you step back to previous points in the history of the file.
You can think about it like adding a time-dimension to your computer's file system.
This extra functionality also lets us do a number of other neat things, which we'll come to later in these notes.

There are two important concepts which are worth introducing at this point which will make understanding Git and similar VCSs easier: *repositories*, and *commits*.

repository
   This is just a directory on your file system where Git, or a similar VCS is keeping track of the history of some files.
   Not all directories on your machine will be held under version control, only ones inside directories which you turn into repositories.

commit
   This is a defined point in the history of a file; effectively a snapshot of its state at a specific time.
   VCSs like Git allow you to step between commits of the file in order to explore its history.


Getting started with your first repository
------------------------------------------

There are two ways that you might want to get started with a repository, either setting one up for the first time, or getting a copy of someone else's repository.
In this section I'll cover how you make your own repository, and discuss "cloning" someone else's repository later.

Before we can make a repository, however, we'll need some once-off preparation to set git up on your machine (and you'll need to do this on every machine which you use).

.. note::
   At the moment all of these notes assume that you'll be using Git on a unix-like system, such as MacOS X or some breed of Linux.
   I'll try and put together notes for using Git on Windows 10 at some point in the future.

To get started you'll need to open a terminal. We can check that you have Git installed by running

.. code-block:: console

		$ git --version
		git version 2.17.1

If you get an error, such as ``Command 'git' not found`` then you'll need to install git.
This will be different on various different systems, but again the Git book comes to our rescue with its `installation instructions`_ section.

If running ``git --version`` worked we can go ahead with setup, which involves telling Git who you are, and your email address.
This is important, as commits in the repository will be associated with you so that it's possible to tell who made changes to the code.

Run these two lines in your console (replacing the appropriate details) to finish setting this up:

.. code-block:: console

		$ git config --global user.name "John Doe"
		$ git config --global user.email johndoe@example.com

You can also find additional `git setup`_ options in the Git book, but this is all we need for now.

Now, say I keep all of my coding projects in a subdirectory called ``projects`` inside my home directory, and I want to start a new project called ``antelope``. Then I'd start by making a directory for it inside the ``projects`` directory, as so:

.. code-block:: console

		$ cd ~/projects
		$ mkdir antelope
		
To make the ``antelope`` directory into a repository all we need to do is ``cd`` into it, and run ``git init``:

.. code-block:: console

		$ cd antelope
		$ git init

And that's it! We have our first repository.


Keeping track of files
----------------------

Now that we have a repository it would be useful to start keeping track of files and their changes.
Let's start by making a new file inside our repository (which lives in ``~/projects/antelope``, remember).

.. code-block:: console

		$ echo "Hello world" > test.txt

We now have our text file which contains the words "Hello world".

Now, remember that I said Git works by effectively "adding a time dimension to the filesystem"? Well, that's true to some extent, but the timesteps are discrete, so we need to define what a single point in time will look like.
To do this Git looks at the repository the last time a commit was made, and then looks at all of the changes which have happened since then **to the files we tell it to look at**.
This last bit is important, because Git has a step called "staging" where all of the changes to be made to the repository are assembled before a new commit is made [staging-hg]_.
To tell Git to prepare to add a file, or updates to a file to the repository we run ``git add`` like so:

.. code-block:: console

		$ git add test.txt

This new file will now be in the stage, ready to be made into the commit.
We can verify that this has happened using the ``git status`` command:

.. code-block:: console

		$ git status
		
		On branch master

		No commits yet

		Changes to be committed:
		(use "git rm --cached <file>..." to unstage)

		new file:   test.txt

We can see that ``test.txt`` has been listed as a new file ready to be committed.

Let's make this change into a commit, so that we can always come back to this point.
The Git stage can be turned into a commit using the ``git commit`` command. It's *always* a good idea to write a little description of what the commit was for when we make a commit, which is done with the ``-m`` flag. So we can run

.. code-block:: console

		$ git commit -m "Added a test file."
		[master (root-commit) 1e9f762] Added a test file.
		1 file changed, 0 insertions(+), 0 deletions(-)
		create mode 100644 test.txt

And our changes (our new file) are now stored in the repository.
We can see the history of the repository by running ``git log`` which will show us the list of all commits.

.. code-block:: console

		$ git log
		commit 1e9f762c2b8cdb7315b21ad7fbb3a50999520ce1 (HEAD -> master)
		Author: Daniel Williams <daniel.williams@glasgow.ac.uk>
		Date:   Thu Oct 8 15:45:01 2020 +0100

		Added a test file.

As we make more changes the log will get more fleshed-out!

Suppose we want to change the contents of ``test.txt``, and then update the repository with the new contents of the file.
Well, we can do that exactly the same way as before!

.. code-block:: console

		$ echo "This is a second line." >> test.txt
		$ git add test.txt
		$ git commit -m "Added a second line."
		[master 7ae87f1] Added a second line.
		1 file changed, 2 insertions(+)
		$ git log
		commit 7ae87f1e78d213bedc0ad81b32588ee6496e1dfa (HEAD -> master)
		Author: Daniel Williams <mail@daniel-williams.co.uk>
		Date:   Thu Oct 8 16:18:26 2020 +0100

		Added a second line.

		commit 1e9f762c2b8cdb7315b21ad7fbb3a50999520ce1
		Author: Daniel Williams <mail@daniel-williams.co.uk>
		Date:   Thu Oct 8 15:45:01 2020 +0100

		Added a test file.


Cloning repositories
--------------------
(Amd getting other people's code)
		

.. _[staging-hg]: This is in fact a slightly peculiar feature of Git, and other version control systems, like Mercurial, don't do this, and they'll make the new commit from everything which exists in the working directory. This is simpler, but it can make it harder to make it easy to follow what's going on if there are changes to lots of files, where multiple commits might be helpful. Either way, this is how Git does things, and like it or not, it's what we need to work with.

.. _`installation instructions`: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _`git setup`: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup



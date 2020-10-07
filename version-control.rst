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




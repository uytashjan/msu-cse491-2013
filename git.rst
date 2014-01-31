=====================================
Basic Instructions for Git and Github
=====================================

Links:

* `An interactive git tutorial, 'try git' <http://try.github.io/levels/1/challenges/1>`__
* `Pro Git (the book) <http://git-scm.com/book>`__
* `A tutorial introduction to git <http://git-scm.com/docs/gittutorial>`__
* `Top 10 Git tutorials for beginners <http://sixrevisions.com/resources/git-tutorials-beginners/>`__

See also `this video that Titus made about merging <http://www.youtube.com/watch?v=5G9T_LXii98>`__ 

----

1. Cloning a repository.
========================

Cloning a repository (from github or anywhere else) makes a local copy
of the contents of that repository.

To clone a repository, locate your HTTPS repository URL; it should look
something like this::

   https://github.com/ctb/cse491-serverz.git

where 'ctb' is your username instead, and 'cse491-serverz' is whatever
repository you're trying to clone locally.

note: it *must* end in .git.

Then do 'git clone $URL', replacing $URL with the repository URL.
This will create a directory named after the repository.  You can
rename this directory to whatever you want, move it around, etc; it's
entirely self-contained.

You can now edit files and do whatever you want in this repo.

2. Committing changes
=====================

Do a 'git status' to see what git thinks has been changed.

'git diff' will show the differences between the last commit and
the current changes.

The command::

   git commit -am "my changes"

will commit all the changes to the repository.  A 'git status' immediately
afterwards should show no changes.

'git log' will show you a list of commits.

3. Pushing changes to github
============================

The command::

   git push origin master

will push all changes in the master branch (the default one) to the
remote location called 'origin', which, by default, is wherever you
cloned things from.

Here, 'master' is the branch.  So if you have a branch, say, 'other', you
can do::

   git push origin other:other

You can use 'git remote' to add, remove, edit, and otherwise mess with your
various location aliases (e.g. 'origin').

4. Creating new branches, and switching branches
================================================

To create a new branch called 'other', you can do::

   git checkout -b other

This will copy your *current* branch into a *new* branch called 'other'.

You can switch to an existing branch by doing::

   git checkout other

and you can see existing branches with::

   git branch

5. Pushing changes to github with different branch names.
=========================================================

There's no reason you *have* to use the same branch names in your
local repo as in your github repo.  For example, if you do::

   git push origin master:other

this will push the contents of your *local* master branch into the
*remote* branch named 'other'.

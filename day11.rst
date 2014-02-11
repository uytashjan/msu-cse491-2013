===============================
Day 11: Tuesday, Feb 11th, 2014
===============================

0. Read http://www.artima.com/scalazine/articles/twitter_on_scala.html

1. Quiz and brief discussion.

2. 'git stash' and 'git stash apply' demonstration

3. Code review of a specific chunk o' code.

Pull requests and doing code reviews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(In-class exercise.)

In brief, everyone should fetch this branch into their local repo,

   https://github.com/ctb/cse491-serverz/tree/day11

make at least one change, push the changed branch to their github
repo, and then set up a pull request back to me.

----

Instructions:

On arctic, in your existing repo OR in a newly cloned copy of YOUR
github repo (see :doc:`git`)::

   git fetch https://github.com/ctb/cse491-serverz.git day11:day11

If you have a bunch of changes in your repo for hw5, please commit them
or stash them ('git stash' -- you can retrieve with 'git stash apply').
Then check out the day 11 branch::

   git checkout day11

Now, edit ChangeLog and add in an entry saying "in-class exercise."

Then, push this branch back to your own github account::

   git commit -am "day 11 exercise"
   git push -u origin day11:day11

Go to to your own github account and set up a pull request between
YOUR repository/day11 and MY repository/master branch (ctb).  It
should look like `this <https://github.com/ctb/cse491-serverz/pull/40>`__.

Now, do a code review.  You can comment line by line
(go to the `files view <https://github.com/ctb/cse491-serverz/pull/40/files>`__ of the pull request) AND/OR make changes to your day11 branch and
push them to your repo. ::

   git push origin day11

----

General code review:

0. Does it run?
1. Do tests pass?
2. Spaces rather than tabs.
3. Spaces after #.
4. Properly spelled variable names .
5. Try writing tests to break something. For example, do you believe their POST logic?
6. 80 character line lengths.
7. Test with multiple browsers.
8. Use code coverage to find things that their tests don't test, and see
   if you can break their code.  (See :doc:`day8`)

And/or do a specific code review for :doc:`hw4`.

Reminder about features:

1. handle multipart/form-data.
2. arbitrary size requests.
3. implement templates.
4. implement "404 not found"


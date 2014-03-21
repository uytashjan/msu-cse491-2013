==========
Homework 9
==========

Due by noon on Thursday, Mar 27th.

0. Merge hw8 into your master.  Please don't delete the 'hw8' branch.

   Hand in this homework on branch 'hw9' on your github account, and
   set up a pull request between hw9 and your master branch.  Don't
   merge it, just set up the PR.

1. Integrate the quotes app into server.py, so that it can be run with
   '-A quotes'.  Instead of '/quotes-2.html' have the default ('/')
   be the page that displays the quotes.

2. Integrate the chats app into server.py, so that it can be run with
   '-A chat'.  Amend the chats app so that the time of each message is
   displayed in the chat window, too.

3. Pick 5 points worth of projects from :doc:`projects` and implement.

   Make sure to explain what you did in the ChangeLog, in detail.

   As per the syllabus, you are allowed to work collaboratively but
   everything you hand in must have your own name on the commits.  The
   only exception to this is if you are working with someone else's
   project, but the sum of the project points must be N*5 (if you work
   in a group with N=2 people, each person must implement 5 pts worth
   of projects).  Note that you are also responsible for making sure
   the other persons' code doesn't break your code.

After handing things in:
------------------------

Do a clean checkout of your repo and make sure that all the tests pass
and that all your functionality works on the clean checkout, on arctic.

Using ChangeLog, please explain your project choice and implementation
in sufficient detail to let someone else (me) who is _not_ psychic
understand what you've done and run it.  Test your code and any
instructions using a clean checkout.  I mean it.

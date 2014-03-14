==========
Homework 8
==========

Due by noon on Thursday, Mar 20th.

0. Merge hw7 into your master.  Please don't delete the 'hw7' branch.

   Hand in this homework on branch 'hw8' on your github account, and
   set up a pull request between hw8 and your master branch.  Don't merge
   it, just set up the PR.

1. Implement command line options in server.py to run the following WSGI apps:

      imageapp

      quixote.demo.altdemo

      your app from hw6.

   Specifically, 'server.py -A image -p 8000' should run imageapp on
   port 8000.  '-A altdemo' and '-A myapp' should do the obvious.  If
   '-p' is not specified then the port should be chosen randomly.

   Use `argparse <http://docs.python.org/2/library/argparse.html>`__ to
   accomplish this.

2. Run the twill tests for the image and altdemo apps.  The 'imageapp'
   and 'altdemo' tests (below) should run without modification.

   (Twill provides automated testing for Web apps; it's basically a
   command-line browser.)

   You can get the twill tests here:

      https://github.com/ctb/cse491-serverz/tree/hw8-twill-tests

   To run the twill tests for the imageapp, change into the directory
   containing your server.py, and run::

      twill-sh -u http://localhost:8000/ twill-tests/imageapp-1.twill

   (You will need to have server.py running in another terminal window
   already.)

   You should see output like this::

      >> EXECUTING FILE twill-tests/imageapp-1.twill
      ==> at http://localhost:8000
      AT LINE: twill-tests/imageapp-1.twill:0
      ==> at http://localhost:8000/upload
      AT LINE: twill-tests/imageapp-1.twill:1
      
      Added file "imageapp/dice.png" to file upload field "file"
      
      AT LINE: twill-tests/imageapp-1.twill:2
      Note: submit is using submit button: name="None", value=""
      
      AT LINE: twill-tests/imageapp-1.twill:3
      AT LINE: twill-tests/imageapp-1.twill:5
      ==> at http://localhost:8000/image
      AT LINE: twill-tests/imageapp-1.twill:6
      AT LINE: twill-tests/imageapp-1.twill:7
      --
      1 of 1 files SUCCEEDED.

   The 'run-qx' and 'run-imageapp' scripts should already work; your
   challenge is to make sure that your server.py implementation (which
   should use YOUR WSGI server) works.

   Twill documentation is `here <http://twill.idyll.org/>`__.  To install
   it in your virtualenv, do 'pip install -U twill'; see :doc:`virtualenv`
   for full instructions.

3. Write a twill test for your app that executes all of the URLs and
   checks the return code (200); put the test in twill-tests/ and name
   it myapp-1.twill.

4. Pick 5 points worth of projects from :doc:`projects` and implement.

   Make sure to explain what you did in the ChangeLog, in detail.

   As per the syllabus, you are allowed to work collaboratively but
   everything you hand in must have your own name on the commits.  The
   only exception to this is if you are working with someone else's
   hw8 project, but the sum of the project points must be N*5 (if you
   work in a group with N=2 people, each person must implement 5 pts
   worth of projects).  Note that you are also responsible for making
   sure the other persons' code doesn't break your code.

----

After handing things in:
------------------------

Do a clean checkout of your repo and make sure that all the tests pass
and that all your functionality works on the clean checkout, on arctic.

Using ChangeLog, please explain your project choice and implementation
in sufficient detail to let someone else (me) who is _not_ psychic
understand what you've done and run it.  Test these instructions using
a clean checkout.  I mean it.

.. make sure I can run their server; command line options!!
.. cookie tests!!
.. twill tests on their wsgi server
.. javascript add

.. changelog => changes

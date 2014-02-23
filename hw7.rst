==========
Homework 7
==========

Due by noon on Thursday, Feb 27th.

0. Merge hw6 into your master.  Please don't delete the 'hw6' branch.

   Hand in this homework on branch 'hw7' on your github account, and
   set up a pull request between hw7 and your master branch.  Don't merge
   it, just set up the PR.

1. Add cookie header handling into your WSGI server, and test it by
   making sure that the login link in ``quixote.demo.altdemo`` works.

   See https://github.com/ctb/cse491-serverz/blob/hw5-wsgi/run-qx.py for
   demo code that shows how to run altdemo; this code uses the WSGI reference
   server, but your HW 7.1 should use your own WSGI server.

2. Merge in or copy 'run-imageapp' and the 'imageapp/' directory
   hierarchy from my hw7-imageapp branch (see
   https://github.com/ctb/cse491-serverz/tree/hw7-imageapp).  As with HW 7.1,
   the 'run-imageapp' code uses the WSGI reference server, and you should
   make sure that 'imageapp' runs in your own WSGI server.

3. Modify the imageapp to display the latest image on the front (index) page,
   not just the '/image' page.

4. Do a clean checkout of your repo and make sure that all the tests pass
   and that all your hw7 functionality works on the clean checkout.

5. Have a good break!  There will be no HW over the break.

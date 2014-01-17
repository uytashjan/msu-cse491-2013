==========
Homework 2
==========

Due by noon on Thursday, Jan 23rd.  Reminder, per `the syllabus
<_static/cse491-spring2014-syllabus.pdf>`__ you may use The Google,
friends, family, etc. to complete the homework.

0. Do all of the below on a new branch, 'hw2'. (See :doc:`git` for info
   on how to create a new branch.)

1. Fix any HW1 problems; see my solution `here <https://github.com/ctb/cse491-serverz/tree/hw1-solution>`__

   a. All lines in the header must end in \r\n.
   b. ChangeLog must be updated.

2. Refactor 'server.py' to be testable, and run some tests.

   a. Change server.py to have two functions, main() and
   handle_connection(conn).  The 'main' function should have all of
   the current code (through the 'accept' statement in the loop) in
   it, while the actual connection handling (all the c.send stuff, and
   c.close) should be done in 'handle_connection(conn)'.

   At the end of server.py, then put::

      if __name__ == '__main__':
         main()

   'python server.py' should then still run the server, but 'python -c
   "import server"' should do nothing.

   b. Make sure your code passes the test in test_server.py.

   Merge in my 'hw2' code, to your hw2 branch::

      git pull https://github.com/ctb/cse491-serverz.git hw2

   This will give you a new file, 'test_server.py'.

   Next, make sure you're in an activated virtualenv, and run
   'pip install nose'.

   Finally, run 'nosetests'::

      nosetests -s

   and (when you are done fixing your code :) you should see no errors.

   For more information on nose, read `this introduction
   <http://ivory.idyll.org/articles/nose-intro.html>`__.

2. Update your server.py code to grab the request data (use
   'c.recv(1000)'), extract the 'path' component, and return different
   HTML content for the following request URLs::

      /
      /content
      /file
      /image

   Extend the tests to test each one of these; you should end up with
   at least four test functions in 'test_server', one for each of the
   request URLs.

3. Modify '/' to return HTML that contains links to /content, /file,
   and /image.  Make sure the tests still pass (i.e. fix 'em).

4. Mofify the handle_connection function to handle POST requests
   separately from GET; use the script 'send-post-request' to test
   this.  For now, just return 'hello world' or some such.

   Write a test for this behavior, too.

   Note, to use 'send-post-request', you'll need to run ::

      pip install requests

   inside your virtualenv.

5. Update ChangeLog with whatever it is you've changed; commit, push
   everything to your repository as part of the 'hw2' branch on your
   github repo.  See :doc:`git`; you should be doing something like::

      git push origin hw2:hw2

6. On github, set up a pull request between your two branches,
   'master' and 'hw2' (FROM hw2 INTO base master).  Make sure your
   diff in the pull request contains all of the changes you wanted
   to have.

Done!

---

Links:

* `Nose and testing tutorial <http://ivory.idyll.org/articles/nose-intro.html>`__

* `HTML reference <http://www.htmlgoodies.com/primers/html/article.php/3478131>`__ -- see through #4, linking pages.

* The `requests documentation <http://docs.python-requests.org/en/latest/>`__

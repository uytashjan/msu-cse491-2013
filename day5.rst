===================================
Day 5: Tuesday, January 21st, 2014
===================================

0. For class, read: http://ivory.idyll.org/blog/software-quality-death-spiral.html

1. `Quiz <https://docs.google.com/forms/d/1EAiacJq-5LdEKBH93rcqGj_Z7uMei20Z0VRcXGay-vg/viewform>`__ and discussion.

2. Roadmap for next few weeks.

   Week 4: forms - submitting basic user input data to the web server; HTML.
   
   Week 5: WSGI - building a fully functional Web server component; templating.
   
   Week 6: More interesting Web apps; header processing & cookies.

3. Structure of HTTP, revisited.  `See presentation <https://docs.google.com/presentation/d/1p3LWmm37c0n6zmyIczdMYXO07hIT-X6GS_hROHBo6zo/edit#slide=id.p16>`__.

   Payload of request, abstractly

   Payload of response, abstractly

4. String whacking.

   Read :doc:`strings` and try to solve these problems generically,
   using only those string manipulation commands:

     a. Pick out the 3rd value, e.g. ::

            f("a,b,c,d,e,f") == "c"

     b. Extract everything after the 4th comma in a string, e.g. ::

            f("a,b,c,d,e,f,g") == "e,f,g"

     c. Return the fourth and fifth lines of a multiline string, e.g. ::

            f("a\nb\nc\nd\ne\nf\n") = ["d", "e"]

     d. Pick out the third and fourth values, removing leading underscores, e.g.::

     	    f("_a,_b,_c,_d,_e,_f") = ["d", "e"]

   See also `String Methods <http://docs.python.org/2/library/stdtypes.html#string-methods>`__, and `Strings: Part I <http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/strings1.html>`__, `Part II <http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/strings2.html>`__, and `Part III <http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/strings3.html>`__.

8. Testing.

   Create a new directory & download two files to arctic by doing::

      mkdir cse491-day5
      cd cse491-day5
      wget https://github.com/ged-lab/msu-cse491-2013/raw/master/day5.py
      wget https://github.com/ged-lab/msu-cse491-2013/raw/master/tests_day5.py

   Activate your virtualenv::

      source ~/cse491.env/bin/activate.csh

   and then run nosetests::

      nosetests

   You should see 8 errors from the code in 'day5.py'.  Fix the code in
   'day5.py' so that the tests all pass!

   .. Solutions here: https://github.com/ged-lab/msu-cse491-2013/raw/master/day5-solved.py

.. video
.. blog post hosting

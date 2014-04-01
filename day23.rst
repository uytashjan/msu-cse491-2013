================================
Day 23: Thursday, Mar 27th, 2014
================================

0. Skim `DevOps for recruiters <http://www.slideshare.net/devopsguys/dev-opsguys-devops-101-for-recruiters>`__ and read `this article <http://arstechnica.com/information-technology/2012/07/netflix-attacks-own-network-with-chaos-monkey-and-now-you-can-too/>`__ and `this article <http://techblog.netflix.com/2012/07/chaos-monkey-released-into-wild.html>`__ on ChaosMonkey.


1. Fill out the `quiz <https://docs.google.com/a/msu.edu/forms/d/1_DiC1ECBtaYOpJ1UlVcayWVHaMWDKvY8VXYu9iHQvmo/viewform>`__

2. Discussion.

3. Introducing cookies, and "secure" cookies.

   http://en.wikipedia.org/wiki/HTTP_cookie

   See also 'cookieapp' in cse491-server.

   Check out the day23 branch (see bottom of page), then go into
   day23/ and run::

      python ref-server.py -A cookie

4. Introducing SQLite and SQL.

   https://docs.python.org/2/library/sqlite3.html

   http://sebastianraschka.com/Articles/sqlite3_database.html

   http://software-carpentry.org/v4/databases/

   See the sqlite/ subdirectory in cse491-server for some examples.
   To run the examples, check out the day23 branch (as below), and
   then go into day23/sqlite/, and run::

      python create.py
      python insert.py
      python retrieve.py out.png

   (Then verify that 'out.png' is a valid PNG file :)

.. 5. Python, namespaces, modules, and classes.

Reminder, to look at the day23 serverz repo, put a copy in the directory
'day23' by doing:::

   git clone https://github.com/ctb/cse491-serverz.git day23 -b day23

==========
Homework 3
==========

Due by noon on Thursday, Jan 30th.

0. Branches, etc.

   At your leisure, merge hw2 into your master. (This can be done by
   merging the pull request).  If this has been done correctly,
   visiting your default github page for cse491-serverz should show
   you the code from hw2. You may have trouble merging; I'll produce a
   video over the weekend on how to do this. Until then, just work on
   the hw2 branch.)

   Your master branch should now contain hw2.

   To hand in this homework, put everything on a new branch, hw3 ('git
   checkout -b hw3'), and push that to github.  Set up a pull request
   between hw3 and your master branch (again, matching to hw2) and
   *don't* merge the pull request -- just leave it there.

1. Form parsing/GET.

   Use the 'urlparse' library (included with Python 2.7) to parse
   the 'path' component of HTTP requests so that GET form data
   can be handled.  You should end up using both the 'urlparse' and
   'parse_qs' functions.

   See `the GET footnotes
   <http://www.jmarshall.com/easy/http/http_footnotes.html#getsubmit>`__
   for more information on the basics.

   Here is an HTML form that will generate an HTTP GET with form values::

      <form action='/submit' method='GET'>
      <input type='text' name='firstname'>
      <input type='text' name='lastname'>
      
      </form>

   Serve this form via your Web server (e.g. as '/form') and then
   implement code to take '/submit' requests and return a page
   containing the string, "Hello Mr. $firstname $lastname."  (You
   might look up Python string interpolation to figure out how to 
   substitute variables, although if you want to be a bad programmer
   you can just use '+' to concatenate strings.)
   
   In addition, create an automated test verifying the results of the
   form parsing.  (i.e. create a fake GET request with
   firstname/lastname set, and assert that the page contains the
   correct response containing that firstname/lastname).

2. Form parsing/POST/content-type.

   Edit or copy the form to also do this via a POST, for request
   content-type of application/x-www-form-urlencoded.  Note that
   for POST requests the content will be submitted as part of the
   content body, which for GET requests is empty; so you need to parse
   that.

   Also see: http://www.cs.tut.fi/~jkorpela/forms/methods.html

   You only need one form (so you can choose to do either a GET or a
   POST) but please make sure that both GET and POSTs *can work* in
   your HTTP server implementation.  The best way to do this is to get
   both GET and POST working, and then make sure that you have
   automated tests for both; I expect to see tests for both.

3. Refactor your main function.

   Split the different pages up into different functions, so that
   '/' goes to (for example) 'index(...)'.  Try to make the functions
   all take the same set of parameters, for future purposes.  You
   can still have a bunch of if/else statements in the main handle_connection
   function ;).

4. Reminder: submit as a pull request, unmerged, from branch 'hw3' to
   branch 'master' (which contains hw2) on your github repo.

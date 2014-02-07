==========
Homework 5
==========

Due by noon on Thursday, Feb 13th.

0. Merge hw4 into your master.  Please don't delete the 'hw3' branch :)

   Hand in this homework on branch 'hw5' on your github account, and
   set up a pull request between hw4 and your master branch.  Don't merge
   it, just set up the PR.

1. Move all of your content-delivery code (anything in server.py after
   reading in the request) into a new file, 'app.py', and refactor it
   to look like a WSGI application.
   
   More specifically, follow `the WSGI app specification
   <http://www.python.org/dev/peps/pep-3333/#the-application-framework-side>`__.

   Your app should work in the ref-server.py available `here
   <https://github.com/ctb/cse491-serverz/tree/hw5-wsgi>`__ -- you
   should be able to merge this into your repo by doing::

   	  git pull https://github.com/ctb/cse491-serverz.git hw5-wsgi

   This will give you a basic 'app' file and a demonstration of
   how to run it in ref-server.py.

   Once you've refactored your app.py code, you should get the same
   Web page results as from hw4, but through the WSGI server running
   in ref-server.py instead of with your own socket handling code.

2. Refactor the handle_connection function to run WSGI apps; see
   `the WSGI server info <http://www.python.org/dev/peps/pep-0333/#the-server-gateway-side>`__ for an example, although you'll need to ignore some of the
   CGI-specific details...

   Basically, what you need to do is separate out the actual HTTP
   request parsing from the code that generates a response (which, in
   any case, is now a WSGI app in app.py, right?).  A few tips:

    * 'environ' is a dictionary that you create from the HTTP request;
      see `environ variables <http://www.python.org/dev/peps/pep-3333/#environ-variables>`__.

    * you should fill in 'REQUEST_METHOD', 'PATH_INFO' (leave
      SCRIPT_NAME blank), 'QUERY_STRING', 'CONTENT_TYPE',
      'CONTENT_LENGTH', and 'wsgi.input' in the environ dictionary;

    * wsgi.input is that StringIO object you used in hw4 -- this contains
      the POST data, if any; empty otherwise.

    * 'start_response' should probably be defined *within* your handle
      connection_function (although there are other ways to do it).
      It is responsible for storing the status code and headers returned
      by the app, until the time comes to create the HTTP response.

   Your logic could look something like this:

     1. read in entire request
     2. parse request headers, build environ dictionary
     3. define start_response
     4. call WSGI app with start_response and environ
     5. build HTTP response from results of start_response and return
        value of WSGI app.

   The 'simple_app' in app.py on my hw5-wsgi branch (see `app.py
   <https://github.com/ctb/cse491-serverz/blob/hw5-wsgi/app.py>`__) is
   potentially a useful debugging tool; your server should work with it,
   as well as with the app in your app.py

3. Template inheritance and proper HTML.

   Create a file base.html and use it as a "base template" to return
   proper-ish HTML, as in `the jinja2 example from last year
   <https://github.com/ctb/cse491-webz/tree/master/jinja2>`__.

   (Each of your HTML files should inherit from this base.html and
   fill in only their specific content.)

   Please *do* specify an HTML title (<title> tag) for each page.

4. Your tests still pass, right?

.. Some sample servers, etc.

.. Do a code review?

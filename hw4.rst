==========
Homework 4
==========

Due by noon on Thursday, Feb 6th.

0. Merge hw3 into your master.  Please don't delete the 'hw3' branch :)

   Hand in this homework on branch 'hw4' on your github account, and
   set up a pull request between hw4 and your master branch.  Don't merge
   it, just set up the PR.

1. Modify your POST code handling code to properly handle requests that
   have a Content-Type of multipart/form-data.

   a. Modify send-post-request to send multipart/form-data; see
      `this StackOverflow post <http://stackoverflow.com/questions/12385179/how-to-send-a-multipart-form-data-with-requests-in-python>`__.

   b. Use the 'FieldStorage' class in the built-in 'cgi' module to
      parse the POST form data; see `these docs
      <http://epydoc.sourceforge.net/stdlib/cgi.FieldStorage-class.html>`__.
      Basically, you will want to encapsulate all of the POST request content
      into a StringIO.StringIO() object and pass that in as 'fp', and
      put all of the POST request headers into a dictionary, and pass that in
      as 'headers'.

   c. Retool your form response code to work with both
      application/x-www-form-urlencoded and multipart/form-data
      submission types; this will require writing tests that specify
      both! Test this manually by first setting the form 'enctype' and
      verifying that your code still does what you expect it to; then
      write this into your tests.  Your automated tests must test GET
      and POST, and must test both possible enctypes for POST.

   You might also look at `this discussion of GET and POST <http://www.cs.tut.fi/~jkorpela/forms/methods.html#tech>`__, and the formal W3C `forms documentation <http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4>`__.

2. Fix your code to work with arbitrary size requests.

   Right now, everyone is just using 'c.recv(1000)' to read the
   request in.  But requests can actually be of arbitrary size!  The
   size of the content payload is specified in the Content-Length
   header in the request.  For GET requests it's 0 - easy.  For POST
   requests, it's arbitrary.

   Make your code work with requests > 1000 (OR, change 1000 to be smaller,
   and make your code work with that).  You should *not* count on
   'c.recv(N)' returning N bytes, as this is not guaranteed; it will return
   *no more than* N bytes, and is guaranteed to return at least 1; so,
   plan to be calling c.recv multiple times.

   One trick here is that if you try to read one byte too many, your 'recv'
   will hang (see: blocking I/O).

   (The best way I've found to get this working is to change
   'c.recv(1000)' to 'c.recv(1)', and then make your code work with
   *that*.)

   And, remember to write tests... that test something...

3. HTML and templating.

   Take a look at https://github.com/ctb/cse491-webz/tree/master/jinja2, and
   implement basic templating with jinja2.

   Briefly, this means:

   * install jinja2 in your virtualenv ('pip install -U jinja2');

   * create a subdirectory called 'templates';

   * in that subdirectory, place files that correspond to your different
     pages, including your form handling; basically, anything that
     generates HTML;

   * call 'render' to generate HTML and return that HTML from your Web app;
     see 'render.py' in the cse491-webz repo, above, for example code.

   Please also feel free to modify your HTML tests to just check the
   response code (200) and some key words in your HTML response.

4. Modify your code to return a "404 Not Found" status, with an
   (in)appropriate error message, when a URL that you *don't* handle
   is requested.

5. Check your code coverage and make sure that everything in your
   handle_connection function is covered.  Everything.

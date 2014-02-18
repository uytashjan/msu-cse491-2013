==========
Homework 6
==========

Due by noon on Thursday, Feb 20th.  If you need an extension, ask.

0. Merge hw5 into your master.  Please don't delete the 'hw5' branch :)

   Hand in this homework on branch 'hw6' on your github account, and
   set up a pull request between hw6 and your master branch.  Don't merge
   it, just set up the PR.

1. Write a function that serves a file, together with the appropriate
   content-type.  You can stick with image/jpeg and text/plain for now,
   e.g. a .jpg file would have content-type image/jpeg and a .txt file
   would be text/plain.

   Make /image serve an image (JPG), and /file serve a text file of some
   sort.

   Hint: 'fp = open(filename, "rb"); data = fp.read(); fp.close()'

2. Make sure you WSGI server works with all three of the Quixote demo
   apps, as in :doc:`day13`.  Note that the 'login' functionality in
   altdemo will not work yet; that's OK.

3. Use the wsgiref validator to evaluate your WSGI app.  Apart from
   cookies, is anything else missing or broken?  Fix the obvious things.

4. Do a clean checkout of your repo and make sure that all the tests pass
   and that all your hw6 functionality works on the clean checkout.

   ("Clean checkout" means make a fresh clone of the repository somewhere
   else, so that you can be sure you've checked everything into the repo.)

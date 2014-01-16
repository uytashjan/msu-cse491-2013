===================================
Day 4: Thursday, January 16th, 2014
===================================

0. For class, read http://en.wikipedia.org/wiki/Deep_Web.  Maybe also check
   out http://arxiv.org/pdf/1312.6122v1.pdf.

1. `Quiz <https://docs.google.com/forms/d/15o8LNYMazJ3LL4nTB7WerbS_0-2JCt80euwOG6KuTf0/viewform>`__ and discussion.

2. Code review HOWTO:

   To do a code review, today:

    0. Check out and run/review; add comments and/or fix;
    1. Commit your comments.
    2. Push to branch 'hw1-review' on your own fork, and
       submit pull requests to original repository.

   To do all of this with git, let's do this in a new repo. ::

      git clone <repository under review> cse491-hw1-review
      cd cse491-hw-review
      # ... make changes ...
      git commit -am "review of hw1"
      git push <your home repository> master:hw1-review
      # now, go set up a pull request.

   The last 'git push' command is the only truly new one; you're just
   copying your default branch, 'master', to your home repository,
   with the new name 'hw1-review'.

   Your code review should focus on the following issues:

     0. Does it run
     1. Spaces rather than tabs
     2. Spaces after # in comments
     3. Properly spelled variable names 

   See http://www.python.org/dev/peps/pep-0008/ for general Python code
   thoughts ;).

3. Do code review!

.. How is the deep web even possible? What causes it?

   Login pages/password-protected pages
   Search engine limitations and blocks
   JavaScript
   Pages that no one links to
   
.. How might you find the deep web?

   Sign up for an account on an otherwise unindexed Web site
   Ask a friend
   Explore the Internet
   
.. How do we know the deep web exists?

   Network traffic
   Direct observation

.. Is Twitter an example of the deep web?

   Maybe
   Yes -- most tweets are not indexed or available
   No -- everything on Twitter is saved and indexed

.. Is Facebook an example of the deep web?

   Maybe
   Yes -- many FB pages are not indexed or available
   No -- everything on FB is saved and indexed
   
.. 4. :doc:`hw2` - review and discuss.

================================
Day 20: Thursday, Mar 20th, 2014
================================

0. Read `What is Web 2.0? <http://oreilly.com/web2/archive/what-is-web-20.html>`__ and, if you feel like it, the `Wikipedia page on Web 2.0 <http://en.wikipedia.org/wiki/Web_2.0>`__.

1. `Quiz. <https://docs.google.com/a/msu.edu/forms/d/1vVqbkV8lGjoz8xOeNpUt03M6h0Yi7zUgSR-5buFd9xc/viewform>`__  (May need to log out of your regular google.com account & log into your msu.edu account.)

2. Discussion

3. "AJAX"

   Why AJAX vs simply loading the page?

   Note: no content push options in HTTP!

   Various reasons for using AJAX:

    * Partial load of data.
    * More interactivity.
    * Less page rendering all at once on the client.

4. Quote app query diagram.  (See :doc:`day19`.)

5. Write a `query diagram <https://docs.google.com/presentation/d/1RIbnuczTYxYB5JLg0oCXz8VlxXpGoBFh4QRb7QI7zQ4/edit#slide=id.p13>`__ for the chat app.

   To get the chats app, do a clean checkout of my serverz repo into the directory 'day20' by doing::

     git clone https://github.com/ctb/cse491-serverz.git day20 -b day20

   and then::

     cd day20/chat/
     python2.7 chat-server <port number>

   You probably won't need to be in an activate virtualenv to do this.

   Finally, go to::

     arctic.cse.msu.edu:<port number>/

   and enter a few messages.

   Draw two query diagrams, the first for what happens when you submit
   a message and see it in your own browser chat window, and the
   second for what happens when someone else submits a message and you
   see it in your chat window.

   Then, write your NetID on the piece of paper and put 'em in a stack
   on Table 4.

Part of your HW will be to implement the chat and quotes apps in your
own server.py, i.e. as WSGI apps.  Feel free to get started with that
AFTER you do the query diagrams.

.. 5. Projects discussion.

========
Projects
========

1. Reimplement the imageapp functionality (minus the silly JavaScript)
   in your own app.py, or `Django <https://www.djangoproject.com/>`__
   or `flask <http://flask.pocoo.org/docs/>`__.  (5 pts each)

2. Write a WSGI middleware component that does recording and playback
   of all WSGI traffic between server and component.  (5 pts)

3. Swipe a template from oswd.org and put it in place on your imageapp
   server. (5 pts)

4. Change imageapp to support JPEG and TIFF. (5 pts)

5. Add a URL that provides a list of images, resized to thumbnails
   (you can just img size, not actual resizing -- that will be a
   separate project ;).  (5 pts.)

6. Add image "metadata" uploading, storage, and retrieval: image name,
   description, etc. (5 pts.)

7. Add image metadata search (find image by ...) (5 pts.)

8. Add the ability to comment on images. (5 pts.)

9. Add username login via cookies and tracking of image by "owner" (the
   person who uploaded it).  Allow the owner to delete it. (5 pts.)

10. Implement secure cookies (see #9).  (5 pts.)

11. Write something that prevents denial of services by uploading gigabyte
    files, or "forever" connections that upload things really slowly.
    Be sure to write a client-side test. (5 pts.)

12. Implement AJAX image upload with JQuery. (5 pts.)

13. Implement a Python client to upload images via a JSON-RPC interface. (5 pts)

14. Write down clear instructions for setting up a new Ubuntu machine
    on a cloud service of your choice (I have some documentation for Amazon)
    and installing the imageapp server on port 80. (5 pts.)

.. add account creation, login and authentication
.. add tests at all levels?
.. data persistence in sqlite or NoSQL.
.. thumbnail resizing dynamically
.. Add redirect latest iamge => number; access iages by numbers
.. Implement error handling for no file, etc.

.. consistent styles

.. Use jinja2 form stuff

.. provide detailed copy/paste instructions to run on cloud computer
.. create chef instructions to do same
.. implement auto startup of cloud computer
.. do domain name, IP, etc.

.. write Selenium tests

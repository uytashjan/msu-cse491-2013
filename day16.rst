================================
Day 16: Thursday, Feb 27th, 2014
================================

0. `Lecture notes <https://docs.google.com/presentation/d/1BH2DXvf2G_OwejU0TRbLnGfuJ3RAspWf9ptamKBQOvM/edit#slide=id.p13>`__

1. Walk through solution for :doc:`hw7`, problem 3.  (How are images served?)

2. Form submission and redirects:

   See https://github.com/ctb/cse491-serverz/blob/day16/imageapp/root.py, functions 'upload' and 'upload2'.

3. Read through the examples in :doc:`javascript` and integrate one
   JavaScript and one JQuery example each into one or more of your pages
   from HW 7.  (Don't worry too much about which page, and no, they don't
   have to be on any specific page.)  You should be editing your templates
   files to do this.

Note: you can either pull these files into your hw7 branch by doing ::

    git pull https://github.com/ctb/cse491-serverz.git day16

or by doing a clean checkout in some other directory and then copying
over the ones you care about::

    git clone https://github.com/ctb/cse491-serverz.git day16 -b day16

or you can just download and save the example files through github.  Whatever
suits.

Also note: if you're having trouble loading the jquery-1.3.2.min.js
file through your server, you can use this code snippet in your
RootDirectory class (in imageapp/root.py)::

    # make sure to import:
    #    from quixote.util import StaticFile
    #    import os.path

    # 'filename' must be in the _q_exports list
    _q_exports = [ ..., 'filename', ...]

    filename = StaticFile(os.path.abspath("./filename.txt"))

Here, 'filename.txt' will be served from whatever directory you're
running your WSGI server from.

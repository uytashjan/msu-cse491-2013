================
Using virtualenv
================

We're using `virtualenv <http://www.virtualenv.org/en/latest/>`__ to
manage software installs etc.  I'll keep this page up to date with
packages that need to be installed for HWs and in-class exercises.

.. note::

   There's no harm in deleting and recreating your virtualenv.  But
   you can't move them around; they contain hard-coded paths.

Creating a virtualenv
=====================

Pick a location (a directory that does not yet exist) and type::

   python2.7 -m virtualenv $location

This will create a new virtual environment in $location.  For example, ::

   rm -fr ~/cse491.env
   python2.7 -m virtualenv ~/cse491.env

will create a virtualenv in the directory 'cse491.env' in your home directory.

(You only need to create a virtualenv once.)

Activating your virtualenv
==========================

Every time you log in or open a new shell window, you need to activate the
virtualenv so your Python knows about it.  To do this in csh (the default
shell), type::

   source $location/bin/activate.csh

In bash, do::

   . $location/bin/activate

So, for example, in csh, you would do ::

   source ~/cse491.env/bin/activate.csh

Installing software in the virtualenv
=====================================

You will need nose, requests, and coverage; you only need to install these
once for each virtualenv. ::

   pip install -U nose
   pip install -U requests
   pip install -U coverage
   source ~/cse491.env/bin/activate.csh

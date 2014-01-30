===================================
Day 8: Thursday, January 30th, 2014
===================================

0. Read the links from :doc:`day7`: http://www.fastcompany.com/28121/they-write-right-stuff and http://www.infoworld.com/print/15243; skim http://calleam.com/WTPF/?page_id=2086

1. `Quiz <https://docs.google.com/forms/d/1jeObFWhhAhaKlRL6139hdiq_wRreMaERhEW5jrCCPjY/viewform>`__ and discussion.

2. Lecture on code coverage and code paths: `presentation <https://docs.google.com/presentation/d/1zxcMzbFUACmzo0zoYDt3IkHFp1QXPUw1r63LI91xU6w/edit#slide=id.g2a9c65f59_00>`__

3. Code review and code coverage of hw3

I'm happy to help with any git problems you have, also.

Computing and displaying code coverage stats
============================================

First, activate your virtualenv (see :doc:`virtualenv`).  Then install
`coverage <http://nedbatchelder.com/code/coverage/>`__::

   pip install -U coverage

(You may want to reactivate your virtualenv after installing this; I've had
some path problems.)

Next, grab some code to run it on -- let's use the 'hw2-solutions'
branch from https://github.com/ctb/cse491-serverz. ::

   mkdir ~/cse491
   cd ~/cse491
   git clone https://github.com/ctb/cse491-serverz.git -b hw2-solutions day8

Run the tests with code coverage enabled::

   cd day8
   nosetests --with-coverage

Generate HTML output of your code coverage::

   coverage html

which will put it in the directory 'htmlcov', and then post it to your
arctic Web site::

   mkdir ~/web/
   cp -r htmlcov ~/web/day8-htmlcov
   chmod -R a+rx ~/web/

Now go to http://www.cse.msu.edu/~$username/day8-htmlcov/ to look at
the code coverage report -- mine is here:

   http://www.cse.msu.edu/~ctb/day8-htmlcov/

If you look at 'server.py', you'll see some covered stuff (green) and
some uncovered stuff (red):

   http://www.cse.msu.edu/~ctb/day8-htmlcov/server.html

Why? Can you think of any way to "cover" the red stuff in the tests?
   
Things to try
-------------

Run code coverage on your own hw3.  What did you fail to test in server.py?

Deactivate some of your tests by putting a 'return' right after the
start of the function.  Does the code coverage change in the expected
way?

Do a review of someone else's hw3, and either make comments on their pull
request or on their code directly (by checking it out locally).  Note,
you can grab someone's code by doing something like this, in an existing
repo::

   git fetch https://github.com/ctb/cse491-serverz hw3 ctb-hw3
   git checkout ctb-hw3

If you make changes, comments, etc. then you can share them by first
committing them, and then doing::

   git push origin ctb-hw3:ctb-hw3

and setting up a pull request between YOUR copy of their branch (here,
ctb-hw3 in your github repo) and THEIR hw3 branch.

If you use coverage analysis during your review, you might be able
to find untested logic -- and there might be bugs in there, too. Try
writing a test that breaks their code (or at least covers it).

Code review checklist
~~~~~~~~~~~~~~~~~~~~~

Basic rules:

0. Does it run.
1. Do tests pass.
2. Spaces rather than tabs.
3. Spaces after #.
4. Properly spelled variable names .
5. Try writing tests to break something. For example, do you believe their POST logic?
6. 80 character line lengths.
7. Test with multiple browsers.
8. Use code coverage to find things that their tests don't test, and see
   if you can break their code.

List of repositories
====================

massiek: `github site <https://github.com/massiek/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/massiek/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/massiek/cse491-serverz.git>`__

eunbong: `github site <https://github.com/eunbong/cse491-serverz>`__ - `pulls <https://github.com/eunbong/cse491-serverz/pulls>`__ - `branches <https://github.com/eunbong/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/eunbong/cse491-serverz.git>`__

matheusldaraujo: `github site <https://github.com/matheusldaraujo/cse491-serverz>`__ - `pulls <https://github.com/matheusldaraujo/cse491-serverz/pulls>`__ - `branches <https://github.com/matheusldaraujo/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/matheusldaraujo/cse491-serverz.git>`__

ConnorAvery: `github site <https://github.com/ConnorAvery/cse491-serverz>`__ - `pulls <https://github.com/ConnorAvery/cse491-serverz/pulls>`__ - `branches <https://github.com/ConnorAvery/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/ConnorAvery/cse491-serverz.git>`__

jprickles: `github site <https://github.com/jprickles/cse491-serverz>`__ - `pulls <https://github.com/jprickles/cse491-serverz/pulls>`__ - `branches <https://github.com/jprickles/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jprickles/cse491-serverz.git>`__

jkteuber: `github site <https://github.com/jkteuber/cse491-serverz>`__ - `pulls <https://github.com/jkteuber/cse491-serverz/pulls>`__ - `branches <https://github.com/jkteuber/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jkteuber/cse491-serverz.git>`__

beckhamer: `github site <https://github.com/beckhamer/cse491-serverz>`__ - `pulls <https://github.com/beckhamer/cse491-serverz/pulls>`__ - `branches <https://github.com/beckhamer/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/beckhamer/cse491-serverz.git>`__

john3209: `github site <https://github.com/john3209/cse491-serverz>`__ - `pulls <https://github.com/john3209/cse491-serverz/pulls>`__ - `branches <https://github.com/john3209/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/john3209/cse491-serverz.git>`__

mill1256: `github site <https://github.com/mill1256/cse491-serverz>`__ - `pulls <https://github.com/mill1256/cse491-serverz/pulls>`__ - `branches <https://github.com/mill1256/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mill1256/cse491-serverz.git>`__

YourBestFriend: `github site <https://github.com/YourBestFriend/cse491-serverz>`__ - `pulls <https://github.com/YourBestFriend/cse491-serverz/pulls>`__ - `branches <https://github.com/YourBestFriend/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/YourBestFriend/cse491-serverz.git>`__

hoffm386: `github site <https://github.com/hoffm386/cse491-serverz>`__ - `pulls <https://github.com/hoffm386/cse491-serverz/pulls>`__ - `branches <https://github.com/hoffm386/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/hoffm386/cse491-serverz.git>`__

joshshadik: `github site <https://github.com/joshshadik/cse491-serverz>`__ - `pulls <https://github.com/joshshadik/cse491-serverz/pulls>`__ - `branches <https://github.com/joshshadik/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/joshshadik/cse491-serverz.git>`__

msweet18: `github site <https://github.com/msweet18/cse491-serverz>`__ - `pulls <https://github.com/msweet18/cse491-serverz/pulls>`__ - `branches <https://github.com/msweet18/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/msweet18/cse491-serverz.git>`__

juru13: `github site <https://github.com/juru13/cse491-serverz>`__ - `pulls <https://github.com/juru13/cse491-serverz/pulls>`__ - `branches <https://github.com/juru13/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/juru13/cse491-serverz.git>`__

mcdonaldca: `github site <https://github.com/mcdonaldca/cse491-serverz>`__ - `pulls <https://github.com/mcdonaldca/cse491-serverz/pulls>`__ - `branches <https://github.com/mcdonaldca/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mcdonaldca/cse491-serverz.git>`__

filajust: `github site <https://github.com/filajust/cse491-serverz>`__ - `pulls <https://github.com/filajust/cse491-serverz/pulls>`__ - `branches <https://github.com/filajust/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/filajust/cse491-serverz.git>`__

leflerja: `github site <https://github.com/leflerja/cse491-serverz>`__ - `pulls <https://github.com/leflerja/cse491-serverz/pulls>`__ - `branches <https://github.com/leflerja/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/leflerja/cse491-serverz.git>`__

FireSBurnsmuP: `github site <https://github.com/FireSBurnsmuP/cse491-serverz>`__ - `pulls <https://github.com/FireSBurnsmuP/cse491-serverz/pulls>`__ - `branches <https://github.com/FireSBurnsmuP/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/FireSBurnsmuP/cse491-serverz.git>`__

koppmana: `github site <https://github.com/koppmana/cse491-serverz>`__ - `pulls <https://github.com/koppmana/cse491-serverz/pulls>`__ - `branches <https://github.com/koppmana/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/koppmana/cse491-serverz.git>`__

Karmeow: `github site <https://github.com/Karmeow/cse491-serverz>`__ - `pulls <https://github.com/Karmeow/cse491-serverz/pulls>`__ - `branches <https://github.com/Karmeow/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/Karmeow/cse491-serverz.git>`__

curljosh: `github site <https://github.com/curljosh/cse491-serverz>`__ - `pulls <https://github.com/curljosh/cse491-serverz/pulls>`__ - `branches <https://github.com/curljosh/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/curljosh/cse491-serverz.git>`__

yispencer: `github site <https://github.com/yispencer/cse491-serverz>`__ - `pulls <https://github.com/yispencer/cse491-serverz/pulls>`__ - `branches <https://github.com/yispencer/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/yispencer/cse491-serverz.git>`__

glisto18: `github site <https://github.com/glisto18/cse491-serverz>`__ - `pulls <https://github.com/glisto18/cse491-serverz/pulls>`__ - `branches <https://github.com/glisto18/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/glisto18/cse491-serverz.git>`__

mannin92: `github site <https://github.com/mannin92/cse491-serverz>`__ - `pulls <https://github.com/mannin92/cse491-serverz/pulls>`__ - `branches <https://github.com/mannin92/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mannin92/cse491-serverz.git>`__

westjour: `github site <https://github.com/westjour/cse491-serverz>`__ - `pulls <https://github.com/westjour/cse491-serverz/pulls>`__ - `branches <https://github.com/westjour/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/westjour/cse491-serverz.git>`__

jbull477: `github site <https://github.com/jbull477/cse491-serverz>`__ - `pulls <https://github.com/jbull477/cse491-serverz/pulls>`__ - `branches <https://github.com/jbull477/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jbull477/cse491-serverz.git>`__

fakestuff: `github site <https://github.com/fakestuff/cse491-serverz>`__ - `pulls <https://github.com/fakestuff/cse491-serverz/pulls>`__ - `branches <https://github.com/fakestuff/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/fakestuff/cse491-serverz.git>`__

msu-web-dev: `github site <https://github.com/msu-web-dev/cse491-serverz>`__ - `pulls <https://github.com/msu-web-dev/cse491-serverz/pulls>`__ - `branches <https://github.com/msu-web-dev/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/msu-web-dev/cse491-serverz.git>`__

MaxwellGBrown: `github site <https://github.com/MaxwellGBrown/cse491-serverz>`__ - `pulls <https://github.com/MaxwellGBrown/cse491-serverz/pulls>`__ - `branches <https://github.com/MaxwellGBrown/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/MaxwellGBrown/cse491-serverz.git>`__

xavierdhjr: `github site <https://github.com/xavierdhjr/cse491-serverz>`__ - `pulls <https://github.com/xavierdhjr/cse491-serverz/pulls>`__ - `branches <https://github.com/xavierdhjr/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/xavierdhjr/cse491-serverz.git>`__

ettemaet: `github site <https://github.com/ettemaet/cse491-serverz>`__ - `pulls <https://github.com/ettemaet/cse491-serverz/pulls>`__ - `branches <https://github.com/ettemaet/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/ettemaet/cse491-serverz.git>`__

lieblic2: `github site <https://github.com/lieblic2/cse491-serverz>`__ - `pulls <https://github.com/lieblic2/cse491-serverz/pulls>`__ - `branches <https://github.com/lieblic2/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/lieblic2/cse491-serverz.git>`__

bjurgess1: `github site <https://github.com/bjurgess1/cse491-serverz>`__ - `pulls <https://github.com/bjurgess1/cse491-serverz/pulls>`__ - `branches <https://github.com/bjurgess1/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/bjurgess1/cse491-serverz.git>`__

suhkang: `github site <https://github.com/suhkang/cse491-serverz>`__ - `pulls <https://github.com/suhkang/cse491-serverz/pulls>`__ - `branches <https://github.com/suhkang/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/suhkang/cse491-serverz.git>`__

jonest31: `github site <https://github.com/jonest31/cse491-serverz>`__ - `pulls <https://github.com/jonest31/cse491-serverz/pulls>`__ - `branches <https://github.com/jonest31/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jonest31/cse491-serverz.git>`__

tsloncz: `github site <https://github.com/tsloncz/cse491-serverz>`__ - `pulls <https://github.com/tsloncz/cse491-serverz/pulls>`__ - `branches <https://github.com/tsloncz/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/tsloncz/cse491-serverz.git>`__

zhopping: `github site <https://github.com/zhopping/cse491-serverz>`__ - `pulls <https://github.com/zhopping/cse491-serverz/pulls>`__ - `branches <https://github.com/zhopping/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/zhopping/cse491-serverz.git>`__

MattyAyOh: `github site <https://github.com/MattyAyOh/cse491-serverz>`__ - `pulls <https://github.com/MattyAyOh/cse491-serverz/pulls>`__ - `branches <https://github.com/MattyAyOh/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/MattyAyOh/cse491-serverz.git>`__

o2themar: `github site <https://github.com/o2themar/cse491-serverz>`__ - `pulls <https://github.com/o2themar/cse491-serverz/pulls>`__ - `branches <https://github.com/o2themar/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/o2themar/cse491-serverz.git>`__

phammin1: `github site <https://github.com/phammin1/cse491-serverz>`__ - `pulls <https://github.com/phammin1/cse491-serverz/pulls>`__ - `branches <https://github.com/phammin1/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/phammin1/cse491-serverz.git>`__

Badsauce: `github site <https://github.com/Badsauce/cse491-serverz>`__ - `pulls <https://github.com/Badsauce/cse491-serverz/pulls>`__ - `branches <https://github.com/Badsauce/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/Badsauce/cse491-serverz.git>`__

DuncanCYoung: `github site <https://github.com/DuncanCYoung/cse491-serverz>`__ - `pulls <https://github.com/DuncanCYoung/cse491-serverz/pulls>`__ - `branches <https://github.com/DuncanCYoung/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/DuncanCYoung/cse491-serverz.git>`__

cameronkeif: `github site <https://github.com/cameronkeif/cse491-serverz>`__ - `pulls <https://github.com/cameronkeif/cse491-serverz/pulls>`__ - `branches <https://github.com/cameronkeif/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/cameronkeif/cse491-serverz.git>`__

majeedus: `github site <https://github.com/majeedus/cse491-serverz>`__ - `pulls <https://github.com/majeedus/cse491-serverz/pulls>`__ - `branches <https://github.com/majeedus/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/majeedus/cse491-serverz.git>`__

polavar3: `github site <https://github.com/polavar3/cse491-serverz>`__ - `pulls <https://github.com/polavar3/cse491-serverz/pulls>`__ - `branches <https://github.com/polavar3/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/polavar3/cse491-serverz.git>`__

brtaylor92: `github site <https://github.com/brtaylor92/cse491-serverz>`__ - `pulls <https://github.com/brtaylor92/cse491-serverz/pulls>`__ - `branches <https://github.com/brtaylor92/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/brtaylor92/cse491-serverz.git>`__

labrenzm: `github site <https://github.com/labrenzm/cse491-serverz>`__ - `pulls <https://github.com/labrenzm/cse491-serverz/pulls>`__ - `branches <https://github.com/labrenzm/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/labrenzm/cse491-serverz.git>`__

QSSS: `github site <https://github.com/QSSS/cse491-serverz>`__ - `pulls <https://github.com/QSSS/cse491-serverz/pulls>`__ - `branches <https://github.com/QSSS/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/QSSS/cse491-serverz.git>`__

sarteleb: `github site <https://github.com/sarteleb/cse491-serverz>`__ - `pulls <https://github.com/sarteleb/cse491-serverz/pulls>`__ - `branches <https://github.com/sarteleb/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/sarteleb/cse491-serverz.git>`__

JRucinski: `github site <https://github.com/JRucinski/cse491-serverz>`__ - `pulls <https://github.com/JRucinski/cse491-serverz/pulls>`__ - `branches <https://github.com/JRucinski/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/JRucinski/cse491-serverz.git>`__

fenderic: `github site <https://github.com/fenderic/cse491-serverz>`__ - `pulls <https://github.com/fenderic/cse491-serverz/pulls>`__ - `branches <https://github.com/fenderic/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/fenderic/cse491-serverz.git>`__

===================================
Day 6: Thursday, January 23rd, 2014
===================================

0. Read: https://www.thc.org/root/phun/unmaintain.html.   You might also like `BOFH <http://bofh.ntk.net/BOFH/0000/bastard01.php>`__.

1. `Quiz <https://docs.google.com/forms/d/1Aq84DUNI_UvjhY4Qlyz_aZqnmXylQuiS8UmkNHamGH8/viewform>`__ and discussion.

2. Presentation: HTTP, HTML, and links; ~/web/ on arctic.  `Presentation link <https://docs.google.com/presentation/d/1rXtdsm57hKzSCc3RW-WucqRZSuLQ_f1C2QgtNMT1nzw/edit#slide=id.p13>`__

3. Presentation: git and merging.

4. Options for today!

   a. Fix/ask for help with your hw2/pull request.  (Ask your neighbor(s) first; then ask Titus.)
   b. Code review! (See below.)
   c. Play with (static) HTML on arctic.
   d. Work through github tutorials: http://try.github.io/ and http://pcottle.github.io/learnGitBranching/

Code review HOWTO v2
====================

.. YourBestFriend
.. jonest31

1. Pick a name from the list of repositories below; go to the repository.

2. See if they have a pull request.  If they do, go to step 5.

3. If they don't have a pull request, see if they have a hw2 branch.  If they do, set up a pull request for them :)

4. If they don't have a hw2 branch, go to step 1.

5. Clone their repository (git clone https://github.com/USERNAME/cse491-servers.git) and then do a 'git checkout hw2'.

6. Perform your code review; place comments on the lines of code in the pull request.

7. Once done, go back and look at someone else's code, or do something else. (If you have questions on your code review, please feel free to e-mail me: ctb@msu.edu)

What to look at in code review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic rules:

0. Does it run.
1. Do tests pass.
2. Spaces rather than tabs.
3. Spaces after #.
4. Properly spelled variable names .
5. Try writing tests to break something. For example, do you believe their POST logic?
6. 80 character line lengths.
7. Test with multiple browsers.



.. video: merging?
.. blog hosting
.. reward for code reviewrs?
.. 

Play with static HTML on arctic
===============================

Reminder: `HTML reference <http://www.htmlgoodies.com/primers/html/article.php/3478131>`__ -- see through #4, linking pages.

On arctic, do::

   mkdir ~/web/
   mkdir ~/web/day6

   echo "<a href='hello.html'>Hello, world</a>" > ~/web/day6/index.html
   echo "Hello, world. <a href='./'>Go back</a>" > ~/web/day6/hello.html

   chmod -R a+rx ~/web/

Now, in a Web browser, go to::

   http://www.cse.msu.edu/~USERNAME/day6/

(make sure you have the '~' in there.)

This is how you create static pages on arctic.  It is also a simple way to
play with HTML to make sure that your basic HTML works right.

Tasks:

* create an absolute link to somewhere else on the index.html page
* create an absolute internal link to another page on CSE
* create a relative link to another page within your repository or elsewhere on CSE.

-------

List of repositories
====================

massiek: `github site <https://github.com/massiek/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/massiek/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/massiek/cse491-serverz.git>`__

eunbong: `github site <https://github.com/eunbong/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/eunbong/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/eunbong/cse491-serverz.git>`__

matheusldaraujo: `github site <https://github.com/matheusldaraujo/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/matheusldaraujo/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/matheusldaraujo/cse491-serverz.git>`__

ConnorAvery: `github site <https://github.com/ConnorAvery/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/ConnorAvery/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/ConnorAvery/cse491-serverz.git>`__

jprickles: `github site <https://github.com/jprickles/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/jprickles/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jprickles/cse491-serverz.git>`__

jkteuber: `github site <https://github.com/jkteuber/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/jkteuber/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jkteuber/cse491-serverz.git>`__

beckhamer: `github site <https://github.com/beckhamer/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/beckhamer/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/beckhamer/cse491-serverz.git>`__

john3209: `github site <https://github.com/john3209/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/john3209/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/john3209/cse491-serverz.git>`__

mill1256: `github site <https://github.com/mill1256/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/mill1256/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mill1256/cse491-serverz.git>`__

YourBestFriend: `github site <https://github.com/YourBestFriend/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/YourBestFriend/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/YourBestFriend/cse491-serverz.git>`__

hoffm386: `github site <https://github.com/hoffm386/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/hoffm386/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/hoffm386/cse491-serverz.git>`__

joshshadik: `github site <https://github.com/joshshadik/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/joshshadik/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/joshshadik/cse491-serverz.git>`__

msweet18: `github site <https://github.com/msweet18/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/msweet18/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/msweet18/cse491-serverz.git>`__

juru13: `github site <https://github.com/juru13/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/juru13/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/juru13/cse491-serverz.git>`__

mcdonaldca: `github site <https://github.com/mcdonaldca/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/mcdonaldca/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mcdonaldca/cse491-serverz.git>`__

filajust: `github site <https://github.com/filajust/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/filajust/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/filajust/cse491-serverz.git>`__

leflerja: `github site <https://github.com/leflerja/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/leflerja/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/leflerja/cse491-serverz.git>`__

FireSBurnsmuP: `github site <https://github.com/FireSBurnsmuP/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/FireSBurnsmuP/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/FireSBurnsmuP/cse491-serverz.git>`__

koppmana: `github site <https://github.com/koppmana/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/koppmana/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/koppmana/cse491-serverz.git>`__

Karmeow: `github site <https://github.com/Karmeow/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/Karmeow/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/Karmeow/cse491-serverz.git>`__

curljosh: `github site <https://github.com/curljosh/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/curljosh/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/curljosh/cse491-serverz.git>`__

yispencer: `github site <https://github.com/yispencer/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/yispencer/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/yispencer/cse491-serverz.git>`__

glisto18: `github site <https://github.com/glisto18/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/glisto18/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/glisto18/cse491-serverz.git>`__

mannin92: `github site <https://github.com/mannin92/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/mannin92/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/mannin92/cse491-serverz.git>`__

westjour: `github site <https://github.com/westjour/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/westjour/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/westjour/cse491-serverz.git>`__

jbull477: `github site <https://github.com/jbull477/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/jbull477/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jbull477/cse491-serverz.git>`__

fakestuff: `github site <https://github.com/fakestuff/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/fakestuff/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/fakestuff/cse491-serverz.git>`__

msu-web-dev: `github site <https://github.com/msu-web-dev/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/msu-web-dev/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/msu-web-dev/cse491-serverz.git>`__

MaxwellGBrown: `github site <https://github.com/MaxwellGBrown/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/MaxwellGBrown/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/MaxwellGBrown/cse491-serverz.git>`__

xavierdhjr: `github site <https://github.com/xavierdhjr/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/xavierdhjr/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/xavierdhjr/cse491-serverz.git>`__

ettemaet: `github site <https://github.com/ettemaet/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/ettemaet/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/ettemaet/cse491-serverz.git>`__

lieblic2: `github site <https://github.com/lieblic2/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/lieblic2/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/lieblic2/cse491-serverz.git>`__

bjurgess1: `github site <https://github.com/bjurgess1/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/bjurgess1/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/bjurgess1/cse491-serverz.git>`__

suhkang: `github site <https://github.com/suhkang/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/suhkang/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/suhkang/cse491-serverz.git>`__

jonest31: `github site <https://github.com/jonest31/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/jonest31/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/jonest31/cse491-serverz.git>`__

tsloncz: `github site <https://github.com/tsloncz/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/tsloncz/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/tsloncz/cse491-serverz.git>`__

zhopping: `github site <https://github.com/zhopping/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/zhopping/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/zhopping/cse491-serverz.git>`__

MattyAyOh: `github site <https://github.com/MattyAyOh/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/MattyAyOh/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/MattyAyOh/cse491-serverz.git>`__

o2themar: `github site <https://github.com/o2themar/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/o2themar/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/o2themar/cse491-serverz.git>`__

phammin1: `github site <https://github.com/phammin1/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/phammin1/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/phammin1/cse491-serverz.git>`__

Badsauce: `github site <https://github.com/Badsauce/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/Badsauce/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/Badsauce/cse491-serverz.git>`__

DuncanCYoung: `github site <https://github.com/DuncanCYoung/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/DuncanCYoung/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/DuncanCYoung/cse491-serverz.git>`__

cameronkeif: `github site <https://github.com/cameronkeif/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/cameronkeif/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/cameronkeif/cse491-serverz.git>`__

majeedus: `github site <https://github.com/majeedus/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/majeedus/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/majeedus/cse491-serverz.git>`__

polavar3: `github site <https://github.com/polavar3/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/polavar3/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/polavar3/cse491-serverz.git>`__

brtaylor92: `github site <https://github.com/brtaylor92/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/brtaylor92/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/brtaylor92/cse491-serverz.git>`__

labrenzm: `github site <https://github.com/labrenzm/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/labrenzm/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/labrenzm/cse491-serverz.git>`__

QSSS: `github site <https://github.com/QSSS/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/QSSS/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/QSSS/cse491-serverz.git>`__

sarteleb: `github site <https://github.com/sarteleb/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/sarteleb/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/sarteleb/cse491-serverz.git>`__

JRucinski: `github site <https://github.com/JRucinski/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/JRucinski/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/JRucinski/cse491-serverz.git>`__

fenderic: `github site <https://github.com/fenderic/cse491-serverz>`__ - `pulls <https://github.com/massiek/cse491-serverz/pulls>`__ - `branches <https://github.com/fenderic/cse491-serverz/branches>`__ - `repo URL for cloning <https://github.com/fenderic/cse491-serverz.git>`__

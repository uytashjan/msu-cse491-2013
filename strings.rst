Strings and Lists
=================

With Web programming, we often want to do lots of things to strings.  Luckily,
Python has some great string manipulation options.  However, to use them,
you need to know about not only strings but lists.  Here is a quick primer
on some useful string manipulations.

1. Turn a string of records separated by a ':' into a list of records::

     x = "a:b:c"              # define string containing records
     records = x.split(':')   # 'split' x into a list of strings based on ':'
     print records            # should see ['a', 'b', 'c']

   You can also use 'x.split(":", 1)' to split only the first record off;
   more generally, 'x.split(":", N)' will return a list of N+1 strings
   with the last string containing all of the records that weren't split.

2. Turn a multiline string into a list of lines::

      x = "a\nb\n"             # define a multiline string
      lines = x.splitlines()   # break the multiline string up into lines
      print lines[0]           # 'a'
      print len(lines)         # should be 2

3. Turning a list into a string with 'join'::

      x = ['a', 'b', 'c']      # define a list
      y = x.join(':')          # turn list into a string, elements joined by :
      print y                  # a:b:c

4. Indexing and slicing.  Both lists and strings can be indexed and sliced::

      x = [0, 1, 2, 3, 4]
      y = "abcde"

      print x[1:]		# [1,2,3,4]
      print x[1:3]		# [1,2]
      print x[1:-2]		# [1,2]

      print y[1:]		# bcde
      print y[1:3]		# bc
      print y[1:-2]		# bc

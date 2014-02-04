=============================
Day 9: Tuesday, Feb 4th, 2014
=============================

0. Read the following two links: `what is WSGI <http://ivory.idyll.org/articles/wsgi-intro/what-is-wsgi.html>`__, `Wikipedia on WSGI <http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface>`__; skim `a stack overflow question <http://stackoverflow.com/questions/4929626/what-are-wsgi-and-cgi-in-plain-english>`__ and `the WSGI PEP <http://www.python.org/dev/peps/pep-3333/>`__

1. `Quiz: answer some questions <https://docs.google.com/forms/d/1w87_5acvCLJeu88Tt3Qo2tnhWHI5fTnw5E0Lgc7YLgM/viewform>`__

2. What is StackOverflow anyway? Hey, and what's a PEP?

3. WSGI in practice; separation of concerns.

4. Thinkin' 'bout functions.

Fun with functions and callables
--------------------------------

try1: what does the following code print, if placed in a file and executed? ::

    def f(n):
        return 3 * n

    def g():
        return f

    value = g()
    print value(5)
    
try2: what does the following code print, if placed in a file and executed? ::
    
    def g(n):
        def f():
            return 8*n

        return f

    value = g(5)
    print value()

try3: what does the following code print, if placed in a file and executed? ::
    
    class Klassy(object):
        def __init__(self, n):
            self.n = n

        def val(self):
            return 4*self.n

    k = Klassy(5)
    print k.val()

try4: what does the following code print, if placed in a file and executed? ::
    
    class Klassy(object):
        def __init__(self, n):
            self.n = n

        def val(self):
            def g(m):
                return 3 * self.n + m

            return g

    k = Klassy(4)

    fn = k.val()
    print fn(3)

try5: what does the following code print, if placed in a file and executed? ::
    
    class Klassy(object):
        def __init__(self, n):
            self.n = n

        def val(self):
            def g(m):
                return 3 * self.n + m

            return g

    k = Klassy(4)

    fn = k.val()

    k.n = 8
    print fn(4)
    
try6: what does the following code print, if placed in a file and executed? ::
    
    class Klassy(object):
        def __init__(self, n):
            self.n = n

        def __call__(self):
            return 5*self.n

    k = Klassy(5)
    print k()

try7: what does the following code print, if placed in a file and executed? ::
    
    def some_function(other_fn, value):
        value = value*5

        value2 = other_fn(value)

        return value2

    def f(n):
        return n + 1

    def g(m):
        return m - 1

    print some_function(g, 5)
    print some_function(f, 4)

try8: what does the following code print, if placed in a file and executed? ::
    
    global_value = 6

    def some_function(other_fn, value):
        value = value*global_value

        value2 = other_fn(value)

        return value2

    def f(n):
        return n + 1

    def g(m):
        return m - 1

    print some_function(g, 5)
    print some_function(f, 4)

    global_value = 2

    print some_function(g, 5)
    print some_function(f, 4)

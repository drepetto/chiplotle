Coding Guidelines and Standards
===============================

These are some basic coding standards that programmers should follow when contributing to Chiplotle:


Indent with spaces, not with tabs. Use three spaces at a time::

   def foo(x, y):
      return x + y

Introduce comments with two pound signs and a single space::

   ## comment before foo
   def foo(x, y):
      return x + y

Limit lines to 80 characters and use ``\`` to break lines where necessary.

Favor early imports at the head of each module. Only one ``import`` per line::

      from foo import x
      from foo import y
      from foo import z

Include two blank lines after ``import`` statements before the rest of the module::

      from foo import x
      from foo import y
      from foo import z

   
      class Foo(object):
         ...
         ...

Always write an informative docstring when defining a new function or class::

   def foo(x, y):
      '''This is an informative docstring.'''

Use paired apostrophes to delimit strings::

   s = 'foo'

Use paired quotation marks to delimit strings within a string::

   s = 'foo and "bar"'

Eliminate trivial slice indices. Use ``s[:4]`` instead of ``s[0:4]``.

Name classes in upper camelcase::

   def FooBar(object):
      ...
      ...

Name bound methods in underscore-delimited lowercase::

   def Foo(object):

      def bar_blah(self):
         ...

      def bar_baz(self):
         ...

Name module-level functions in underscore-delimited lowercase::

   def foo_bar( ):
      ...

   def foo_blah( ):
      ...

Organize the definitions of core classes into the five following major sections plus initialization::

   class FooBar(object):

      def __init__(self, x, y):
         ...

      ## OVERLOADS ##

      def __repr__(self):
         ...

      def __str__(self):
         ...

      ## PRIVATE ATTRIBUTES ##

      @property
      def _foo(self):
         ...

      ## PUBLIC ATTRIBUTES ##

      @property
      def bar(self):
         ...

      ## PRIVATE METHODS ##

      def _blah(self, x, y):
         ...

      ## PUBLIC METHODS ##

      def baz(self, z):
         ...

Precede private class attributes with a single underscore::

   class FooBar(object):

      ## PRIVATE ATTRIBUTES ##

      @property
      def _foo(self):
         ...

      ## PRIVATE METHODS ##

      def _blah(self, x, y):
         ...

Include a single space in between empty parentheses::

   def foo( ):
      ...
      ...

Separate binary operators with space::

   (a // b) + c == d

not::

   (a//b)+c==d

Do not abbreviate variable names.

Name variables that represent a list or other collection of objects in the plural.

Author one ``py.test`` test file for every module-level function.

Author one ``py.test`` test file for every bound method in the public interface of a class.


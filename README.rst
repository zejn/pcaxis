PC Axis (.px) parser for Python
===============================

Requirements
------------

pyparsing>=1.5.2

Simple example
--------------

  import pcaxis
  data = pcaxis.parsePX(open('test.px').read(), encoding='utf-8')
  print data['TITLE']

The parsePX function returns a dictionary of containing keys such as TITLE or
DESCRIPTION and coresponding values. Under DATA you'll find the table data.

The API is practically nonexistant (I imagine values could be accessed by
indexing) and not all features are supported or implemented, only a subset,
which was needed for my use case.



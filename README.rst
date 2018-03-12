Demo report generator
=====================

This repository contains sample code for the SQL workshop that was held at the
University of Ljubljana, Faculty for Mathematics and Physics.


Installation
------------

.. code:: bash

   $ git clone https://github.com/xlab-si/demo-report-generator.git
   $ cd demo-report-generator
   $ python -m venv venv
   $ . venv/bin/activate  # GNU/Linux
   $ venv\Scripts\activate.bat  # Windows + cmd
   (venv) $ pip install -e .


Usage
-----

.. code:: bash

   $ report
   usage: report [-h] host port user dbname

   Demo report generator

   positional arguments:
     host        Database host IP address
     port        Database host port
     user        Database user
     dbname      Database name

   optional arguments:
     -h, --help  show this help message and exit
   error: the following arguments are required: host, port, user, dbname


Installing sample database
--------------------------

This report generator is meant to be used in conjunction with the PostgreSQL
port of the sakila sample database that is available from the
`PostgreSQL tutorial`_ site. This site also contains instructions on how to
install PostgreSQL on Windows.

.. _PostgreSQL tutorial: http://www.postgresqltutorial.com/

For installing PostgreSQL on GNU/Linux, one can use instructions that were
provided as part of the workshop (for CentOS 7, but they will also work on
Fedora and RHEL with slight modifications).

How to load sample database is described `load sample database`_ section of
the PostgreSQL tutorial.

.. _load sample database:
      http://www.postgresqltutorial.com/load-postgresql-sample-database/

For the people new to SQL, going through the first five sections of the
tutorial is recomended before trying to inspect the code in this sample
project.


Other relevant links
--------------------

Another source of laernig material is also w3schools_ page on SQL that
contains a lot of material to get started. Another benefit of this page is the
ability to run the SQL queries online in their try it editor. This way there
is no need to have database installed while getting our feet wet.

.. _w3schools: https://www.w3schools.com/sql/

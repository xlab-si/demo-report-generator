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

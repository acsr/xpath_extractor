===============
xpath_extractor
===============

Quick & Dirty Content Crawler for Jupyter Notebbook using httrack and xpath locator with Python

Prerequisites
=============

This was a one shot Python solution to grab and postprocess the actual content area inside an awful oldstyle table based website, consistent of around 25 pages. 

* We scraped the content of the website pages using httrack [1] into a filesystem based file/folder structure. The php URLs were transformed into html files.

Challenge
  We needed to extract the plain content core as formatted text - Fast!
  
Install
=======

* httrack [2] was installed on MacOSX using homebrew [3]
* Jupyter and Python 3 were installed on MacOSX using the Anaconda Package Manager [4]

The notebook
============

* a Jupyter Notebook with Python 3 was used to generate a script to process the httrack dump
* a textfile was generated containing all paths to the html files relatively to the notebook (one path per line).
* when opening a scraped html of httrack in a browser (here Chrome) and use the inspect feature (poniter in content, right-click "inspect", "untersuchen") to locate the html/xml node that encloses the content.
* right click on the open tag of the outer node and choose "Copy -> Copy xpath"
* paste the xpath into the scripts #config section where the variable "xpath_selector" is defined.
* test the selector until it works for you (beyond of the scope of this Readme)
* *(here is some further docs and example data missing, sorry)*
* the content is concatenated into one single html file with Headlines for every file and written to disk
* the webbrowser module is used to open the html in a browser.

How to start this notebook
==========================

This is for newbies, like from the PythonCamp where I demoed this as a coarse q&d solution.

* check out the *.ipynb file into the root of the httrack dump. (In this version, we only deal with files related to this directory)
* edit a textfile containing all paths to the html files relatively to the notebook (one path per line). You can do this by hand or using your favorite tools.
* adjust the filenames to the path list and the xpath selector pointing to the content as you like
* run the notebook

.. note:: If you know what you are doing you can alternatively copy the Python code in a new running notebook where you want or run it in another way.

ToDo (someday)
==============

* Add a code snippet to test the selector without the loop first.

Links
=====

[1] https://www.httrack.com
[2] command "brew install httrack"
[3] https://brew.sh
[4] https://www.anaconda.com/distribution/
[5] WEB SCRAPING Session by Jochen Wersdörfer,Armin Stross-Radschinski on PythonCamp Cologne 2018 https://barcamptools.eu/pycamp201804/

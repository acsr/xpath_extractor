===============
xpath_extractor
===============

Quick & Dirty Content Crawler suitable for Jupyter Notebook using httrack and xpath locator with Python

.. note:: This is not a bullet proof tutorial! The docs are work in progress. It was shown in the WEB SCRAPING Session by Jochen Wersdörfer, Armin Stross-Radschinski during the PythonCamp Cologne 2018. Visitors of the PythonCamp Session [5] will find some gems.

Prerequisites
=============

This was a one shot Python solution to grab and postprocess the actual content area inside an awful oldstyle table based website, consistent of around 25 pages. 

* We scraped the content of the website pages using httrack [1] into a filesystem based file/folder structure. The php URLs were transformed into html files.

Challenge
  We needed to extract the plain content core as formatted text - Fast!
  
Install
=======

* httrack [2] was installed on MacOSX using homebrew [3]
* Jupyter and Python 2 were installed on MacOSX using the Anaconda Package Manager [4]

The notebook
============

* a Jupyter Notebook with Python 2 was used to generate a script to process the httrack dump
* a textfile was generated containing all paths to the html files relatively to the notebook (one path per line).
* when opening a scraped html of httrack in a browser (here Chrome) and use the inspect feature (poniter in content, right-click "inspect", "untersuchen") to locate the html/xml node that encloses the content.
* right click on the open tag of the outer node and choose "Copy -> Copy xpath"
* paste the xpath into the scripts #config section where the variable "xpath_selector" is defined.
* test the selector until it works for you (beyond of the scope of this Readme)
* *(here is some further docs and example data missing, sorry)*
* the content is concatenated into one single html file with Headlines for every file and written to disk
* the webbrowser module is used to open the html in a browser.

How to start this in a notebook
===============================

This is for newbies, like from the PythonCamp where I demoed this as a coarse q&d solution.

* open a terminal and cd into the httrack dump root
* start the jupyter notebook with the command 'ipython notebook'
* create a ne notebook and paste the Python code from this repo in a cell
* edit a textfile containing all paths to the html files relatively to the notebook (one path per line)
* adjust the filename in the code to your path list file 
* adjust the xpath selector pointing to the content as you like
* run the notebook

et voila: The browser should show the resulting collected content.

.. note:: If you know what you are doing you can alternatively copy the Python code in a new running notebook where you want or run it in another way.

ToDo (someday)
==============

* add a sample httrach archive
* add a sample path list file
* add the notebook file (currently missing due to no time to clean up the history containing sensible data...)
* add a simpler code snippet in the notebook to test the selector without the loop first.

Links
=====

| [1] https://www.httrack.com
| [2] command "brew install httrack"
| [3] https://brew.sh
| [4] https://www.anaconda.com/distribution/
| [5] WEB SCRAPING Session by Jochen Wersdörfer,Armin Stross-Radschinski during PythonCamp Cologne 2018 https://barcamptools.eu/pycamp201804/

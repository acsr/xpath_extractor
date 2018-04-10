#!/usr/bin/python2
#
# xpath_extractor
# Python HTML Content Crawler
# © 2018 by acsr, developer@acsr.de

##########################
# Purpose
#
# iterate through a list of all html pages of a website dumped by httrack into the current folder
# read the list of file paths from a text file saved on disk in the current folder
# extract content nodes via XPATH selector and lxml
# concatenate well formatted html snippets into one document with headlines
# save the html as file on disk
# open the file in a webrowser
#
##########################

#### import Python modules ####

#basic imports
import sys
import os

#import lxml to process html as xml
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup as bs


#import webbrowser support to open html result
import webbrowser
try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x


# config
html_list_filename='html_list.txt'
html_styles="""body {font-family: Helvetica, arial, freesans, clean, sans-serif;}
p {margin-bottom: 0.5em;}
"""
html_table=""
html_tables=""

# xpath selector for the content block
# xpath originally copied from Chrome Inspector: '/html/body//table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]'
# xpath selector modified by acsr
xpath_selector='//*[@id="mainindex"]/table//tr/td[2]/table/tr[5]//table//tr[2]/td[2]'

# execution
##################

# read file list
with open(html_list_filename, 'r') as content_file:
    content = content_file.read()

lines = content.splitlines()

# process files
for line in lines:
    if (len(line) > 0):
        html_filename = str(line)
        html = lxml.html.parse(html_filename)
        content = html.xpath(xpath_selector)
        # prettify html
        html_chunk=etree.tostring(content[0], pretty_print=True, method='html')

        # enclose the <tr> in table with url filename as h2 headline
        
        table_prefix="""    <h2 class="filename">{}</h2>
    <table>
        <tr>
""".format(html_filename)
        
        table_suffix="""
        </tr>
    </table>

"""
        html_table= table_prefix + html_chunk + table_suffix
    
    html_tables+=html_table

html_result="""<html>
<head>
<title>xpath_extractor Content Crawler by acsr</title>
<meta charset="utf-8">
<meta name="Description" content="Content of all pages extracted using Python and lxml in one batch by acsr. Website URLs crawled by httrack on 21th March 2018">
<style>
{}
</style>
</head>
<body>

<!--
                                                                                                    
            OMNNNNDZ                7NNNNN8,               ODNNNNNN$                 ,?7?,          
       MMNNNNNNNNNNNNNN         MNNNNNNNNNNNNNNN       INNNNNNNNNNNNNNNNN     NNNNNNNNNNNNNNNNNMN   
     NNNNNDZ       DNNN       MNNNNN       IDMNNN     NNNNN         NNNNN     NNNNDN?     7MNNNNN   
   DNNNN           NNNN      NNNN                     DNNN                    NNNN                  
  NNNN             NNNN     NNNN                       NNNNN=                 NNNN                  
 :NNN              NNNN    NNNN                         $NNNNNNNNM$           NNNN                  
 NNNN              NNNN    NNNN                             NNNNNNNNNNN       NNNN                  
 8NNN              NNNN    NNNN                                   8NNNNNN     NNNN                  
  NNNN             NNNN     NNNN                                     :NNN~    NNNN                  
  =NNNN            NNNN      DNNNN           DNM      8NN            ~NNN,    NNNN                  
    NNNNNNNNNNNNN  NNNN       8NNNNNNO~ INNNNNNNN    DDNNNNNNN7:~ZMNNNNNN     NNNN                  
      DNNNNNNNNNNN NNNN          NNNNNNNNNNNNN          =NNNNNNNNNNNNNN       NNNN                  
                                                                                                 
-->

<h1>xpath_extractor Content Crawler</h1>
<h3>Content of all pages extracted using Python and lxml in one batch by acsr</h3>
<p>Website URLs crawled by httrack on 21th March 2018</p>
{}
</body>
</html>
""".format(html_styles, html_tables)

# prettify html
soup=bs(html_result, "lxml")                #make BeautifulSoup
prettyHTML=soup.prettify().encode('utf-8')

with open("combined_content.html", "w") as text_file:
    text_file.write(prettyHTML)

url = 'file:{}'.format(pathname2url(os.path.abspath('combined_content.html')))
webbrowser.open(url)

#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:         Datamining Tools: Row to Array
#
# Purpose:      This is a web based datamining tool that makes it easier to get rows of spreadsheet data into
#               your Python script as an array. Instead of having to parse spreadsheets from within your script,
#               all you have to do is copy and paste a row of data into the web form and this script will produce a
#               Pythonic list (array) that can be copied into your script. Created with Python 2.7.5
#
# Notes:        1. A word like Erup??o Vulc?nica may appear as 'Erup\xe7\xe3o Vulc\xe2nica' when added to the Pythonic list.
#               However, this is okay because when you print 'Erup\xe7\xe3o Vulc\xe2nica' in Python, you get back Erup??o Vulc?nica.
#               2. This script is designed to run as a web-based CGI script, so to use the script you will need to have a server
#               configured to run cgi scripts. For example:
#               http://5x59fs1a.ad.here.com/cgi-bin/column_to_array.py
#
# Author:       Chris Nielsen (chrisn@bluegalaxy.info)
# Created:      Feb. 12, 2015
#-------------------------------------------------------------------------------

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
row_list = form.getvalue('input')
array_data_type = form.getvalue('array_data_type')


# ---------------------------------------------
def ColumnInputForm():
    print "Content-type: text/html"

    landing_page = """
<html>
<head>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<style>

textarea {
    /*background-color: #b32d00;*/
    background-image:url(/images/fondo.jpg);
    overflow: hidden;
    border-style: solid;
    border-width: thin;
    border-color: #000000;
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
}
body {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
}
pre {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;

}

</style>
<title>Data Mining Tools: Row to Array</title>

</head>
    <body bgcolor='#d9d9d9' background="/images/802749-fantasy-fantasy-art-futuristic-guns-robots-science-fiction-vehicles-war-machine.jpg">
<h1>Data Mining Tools: Row to Array</h1>
<pre>This is a web based data mining tool that makes it easier to get rows of spreadsheet data into
your Python script as an array. Instead of having to parse spreadsheets from within your script,
all you have to do is copy and paste a row of data into the web form and this script will produce a
Pythonic list (array) that can be copied into your script. Created with Python 2.7.5</pre>
</body></html>

    <BR>
    <form name="list_form" action="http://bluegalaxy.info/cgi-bin/row_to_array.py" method='POST'>

    <table>
        <tr>
            <td>&nbsp;<b>Paste row of data here:</b><BR>
                <TEXTAREA NAME="input" COLS=108 ROWS=10"></TEXTAREA></td>
        </tr>
        <tr>
            <td>
            <br>What type of data does your list contain?<BR>
            <INPUT TYPE=RADIO NAME="array_data_type" VALUE="strings" CHECKED>strings<BR>
            <INPUT TYPE=RADIO NAME="array_data_type" VALUE="other">other (no quotes)<BR>
            </td>
        </tr>
    </table>
    <BR>
    <input type="Submit" value="Create Pythonic List">
    </form>
    </center>
    """
    print landing_page

# ---------------------------------------------
def ColumnOutput():
    """Take in a column of spreadsheet data and convert it to a pythonic list
    that can be copied and pasted into a script for quick use.
    """
    # Convert the data into a Pythonic list:
    s = row_list.rstrip("\n")
    s = s.rstrip("\r")
    s = s.rstrip("\r\n")
    s = s.rstrip(" ")
     # Convert the column into an array using split
    s = s.split("\t")

    # If not a list of strings, remove the single quotes
    if array_data_type != "strings":
        s = str(s).replace("'", "")

    output_box = """
    <BR>
    &nbsp;<b>Here is the array, ready to be copied into your script: (Ctrl + A) then (Ctrl + C) </b><BR>
    <table>
        <tr>
            <td><TEXTAREA NAME="Output" COLS=108 ROWS=10">%s</TEXTAREA></td>
        </tr>
    </table>
    <BR>
    </center>
    """
    print output_box % (s)

# ---------------------------------------------
def main():
    ColumnInputForm()
    if row_list:
        ColumnOutput()

# ---------------------------------------------
if __name__ == '__main__':
    main()

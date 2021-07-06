#!/usr/bin/env python3
# This script shows how to convert an HTML table to a python dictionary.

from bs4 import BeautifulSoup
import re

# Arbitrary HTML table 
html = """
<!doctype html>
<html>
<body>
  <table>
     <tr> 
      <th>Name:</th>
      <td>Johnny</td>
     </tr>
     <tr> 
      <th>Rank:</th>
      <td>Eagle</td>
     </tr>
     <tr> 
      <th>Age:</th>
      <td>26</td>
     </tr>
    <tr>
     <th>Gender:</th>
     <td>Male</td>
    </tr>
    <tr>
     <th>Height:</th>
     <td>5'10"</td>
    </tr>
    <tr>
     <th>Blood Type:</th>
     <td>A Neg.</td>
    </tr>
  </table>
</body>
</html>
"""

# Make soup object from html text
soup = BeautifulSoup(html, 'lxml')

# Initialize empty lists for table header and data <th> and <td> columns
header_list = []
data_list = []

# Find all table row <tr> tags
rows = soup.find_all('tr')

for row in rows:
	cleanr = re.compile('<.*?>')			# Regex to clean html chars

	col1 = str(row.th)				# Get <th> string
	clean_header = re.sub(cleanr, '', col1).strip()	# Strip it of html

	col2 = str(row.td)				# Same for table data column
	clean_data = re.sub(cleanr, '', col2).strip()

	header_list.append(clean_header)		# Slap those values into lists
	data_list.append(clean_data)

# Finally, I use zip() wrapped in dict() to turn the whole thing into a
# dictionary. 

table_dictionary = dict(zip(header_list, data_list))

print(table_dictionary)

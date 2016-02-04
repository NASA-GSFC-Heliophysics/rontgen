# the following scripts scraps the data from NIST
# and writes the data files
# This grabs the elements

import numpy as np
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import os
import json

url = "http://physics.nist.gov/PhysRefData/XrayMassCoef/tab4.html"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml", parse_only=SoupStrainer('a'))

link_list = []
name_list = []
file_dict = {}
savefile = True

for link in soup:
    if link.has_attr('href'):
        if link['href'].count('ComTab'):
            link_list.append('http://physics.nist.gov/PhysRefData/XrayMassCoef/' + link['href'])
            name_list.append(link.text)

for url, name in zip(link_list, name_list):
    print(url)
    r = urllib2.urlopen(url).read()
    f = os.path.basename(url).split('.')[0]
    print(f)
    lines = r.split('\n')
    element_name = name
    print(element_name)
    short_lines = [line[0:5] for line in lines]
    try:
        line_numbers = [short_lines.index('<PRE>')+6, short_lines.index('</PRE')]
    except:
        print('failed')
        continue
    data_str = lines[line_numbers[0]:line_numbers[1]]
    data_str = [datum.lstrip().rstrip().split() for datum in data_str]
    # remove edge strings
    #for datum in data_str:
        #if len(datum) > 3:
        #    print(datum[-3:])
    data = [datum[-3:] if len(datum) > 3 else datum for datum in data_str]
    # remove empty lines
    data = [datum for datum in data if len(datum) > 1]
    data = np.array(data, dtype=np.float)
    header = 'Data Source: NIST\n'
    header += 'For more information see \nhttp://physics.nist.gov/PhysRefData/XrayMassCoef/tab3.html\n'
    header += 'For definitions see http://physics.nist.gov/PhysRefData/XrayMassCoef/chap2.html\n'
    header += 'url: ' + url + '\n'
    header += '\n'
    header += element_name + '\n'
    header += '\n'
    header += 'energy, mu/rho, mu_en/rho\n'
    header += 'meV, cm2/g, cm2/g'

    file_dict.update({name: f + '.csv'})

    if savefile:
        np.savetxt(f + '.csv', data,                # array to save
            fmt='%.3e',
            delimiter=',',          # column delimiter
            newline='\n',           # new line character
            footer='end of file',   # file footer
            comments='# ',          # character to use for comments
            header=header)

# save the conversion dictionary
with open('data.json', 'w') as fp:
    json.dump(file_dict, fp)

'''
The MIT License (MIT)

Copyright (c) 2017 Vanessa Sochat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

__version__ = "0.1.0"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'node_dcm'
PACKAGE_URL = "http://www.github.com/vsoch/node-dcm"
KEYWORDS = 'dicom, receiver, node, Docker'
DESCRIPTION = "Dockerized node to implement basic Dicom receiver"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (

    ('pynetdicom3', {'min_version': '0.1.0'}),
    ('pydicom', {'min_version': "0.9.9"}),
    ('requests', {'min_version': '2.12.4'}),
    ('retrying', {'min_version': '1.3.3'}),
    ('google-api-python-client', {'min_version': None}),
    ('oauth2client', {'exact_version': '3.0'})
)

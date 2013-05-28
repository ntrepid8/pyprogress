__author__ = 'ntrepid8'

# -*- coding: utf-8 -*-

# Copyright (c) 2013 Josh Austin
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys


def write_progress(percent_complete, width=30):
    if isinstance(percent_complete, float):
        percent_complete = int(percent_complete)
    if (not isinstance(percent_complete, int)) or percent_complete < 0 or percent_complete > 100:
        raise ValueError('percent_complete must be an integer in the range 0-100')
    if (not isinstance(width, int)) or width < 10 or width > 100:
        raise ValueError('width must be an integer in the range 10-100')
    left = int((percent_complete / float(100)) * width)
    right = int((1 - (percent_complete / float(100))) * width)
    if not (left + right) == width:
        if (left + right) < width:
            diff = width - (left + right)
            left += diff
        else:
            diff = (left + right) - width
            left -= diff
    print '\r[' + ('=' * left) + (' ' * right) + '] ' + str(percent_complete) + '% ',
    if percent_complete == 100:
        print ' done!'
    sys.stdout.flush()
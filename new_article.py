#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import os
import sys


def main(name):
	meta_data = r"""Date: {}
Title: New Article Title
Tagline: Some snazzy tagline
Slug: the_slug
Category: Blog
Tags: tag1, tag2

Add the ``Status: draft`` metadata above to avoid publishing immediately!
	""".format(datetime.date.today())
	
	markdown_path = os.path.join('content', name)
	
	if os.path.exists(markdown_path):
		print 'ERROR: {} already exists! Aborting...'.format(markdown_path)
		return -1
	else:
		try:
			with open(markdown_path, 'w') as f:
				f.write(meta_data)
			print '{} succesfully created!'.format(markdown_path)
		except Exception as e:  # Eat all exceptions
			print e
			print 'ERROR: Unable to create article.'
			return -1

if __name__ == '__main__':
    main(sys.argv[1])


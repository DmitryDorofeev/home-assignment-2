#!/usr/bin/env python
import unittest
import os
import sys
from tests.test_post import PostTestCase
from tests.test_main import MainTestCase

source_dir = os.path.join(os.path.dirname(__file__), 'tests')

if __name__ == '__main__':

    if 'TTHA2PASSWORD' not in os.environ:
        sys.exit('No password set')

    if 'TTHA2BROWSER' not in os.environ:
        sys.exit('No browser set')

    suite = unittest.TestSuite((
        unittest.makeSuite(PostTestCase),
        unittest.makeSuite(MainTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""Module: barcode.upc

:Provided barcodes: UPC-A
"""
__docformat__ = 'restructuredtext en'

from barcode.ean import EuropeanArticleNumber13

# Python 3
try:
    reduce
except NameError:
    from functools import reduce


class UniversalProductCodeA(EuropeanArticleNumber13):
    """Initializes new UPC-A barcode. Can be rendered as EAN-13 by passing
    `True` to the `make_ean` argument.

    :parameters:
        upc : String
            The upc number as string.
        writer : barcode.writer Instance
            The writer to render the barcode (default: SVGWriter).
        make_ean : Boolean
            Render barcode as EAN-13 with leading 0 (default: False).
    """

    name = 'UPC-A'

    digits = 11

    def __init__(self, upc, writer=None, make_ean=False):
        if make_ean:
            UniversalProductCodeA.digits = 12
            upc = '0' + upc
        self.upc = upc
        EuropeanArticleNumber13.__init__(self, upc, writer)

    def __unicode__(self):
        return self.upc

    def calculate_checksum(self):
        """Calculates the checksum for UPCA-Code.

        :returns: The checksum for `self.ean`.
        :rtype: Integer
        """
        def sum_(x, y):
            return int(x) + int(y)

        evensum = reduce(sum_, self.ean[::2])
        oddsum = reduce(sum_, self.ean[1::2])
        return (10 - ((evensum * 3 + oddsum) % 10)) % 10

    __str__ = __unicode__


UPCA = UniversalProductCodeA

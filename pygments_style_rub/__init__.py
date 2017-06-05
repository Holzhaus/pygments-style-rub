# -*- coding: utf-8 -*-
"""
    rub
    ~~~

    A style based on the Corporate Design of the Ruhr-University Bochum.

    Color definition were taken from the Corporate Design Manual:
        https://www.ruhr-uni-bochum.de/cd/cd-2016/download/cd_manual_beta.pdf

    :copyright: Copyright 2017 by Jan Holthuis.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class RubStyle(Style):
    """
    A style based on the Corporate Design of the Ruhr-University Bochum.
    """

    default_style = 'autumn'

    styles = {
        Whitespace:                 '#bbbbbb',

        Comment:                    'italic #818181',
        Comment.Preproc:            'noitalic #4c8317',
        Comment.Special:            'italic #003560',

        Keyword:                    'bold #003560',
        Keyword.Type:               '#8dae10',

        Operator.Word:              '#003560',

        Name.Builtin:               '#8dae10',
        Name.Function:              '#274800',
        Name.Class:                 'underline #274800',
        Name.Namespace:             'underline #8dae10',
        Name.Variable:              '#aa0000',
        Name.Constant:              '#aa0000',
        Name.Entity:                'bold #800',
        Name.Attribute:             '#8dae10',
        Name.Tag:                   'bold #1e90ff',
        Name.Decorator:             '#888888',

        String:                     '#336893',
        String.Symbol:              '#003560',
        String.Regex:               '#8dae10',

        Number:                     'italic #8dae10',

        Generic.Heading:            'bold #000080',
        Generic.Subheading:         'bold #800080',
        Generic.Deleted:            '#aa0000',
        Generic.Inserted:           '#274800',
        Generic.Error:              '#aa0000',
        Generic.Emph:               'italic',
        Generic.Strong:             'bold',
        Generic.Prompt:             '#555555',
        Generic.Output:             '#888888',
        Generic.Traceback:          '#aa0000',

        Error:                      '#F00 bg:#FAA'
    }

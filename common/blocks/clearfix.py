# -*- coding: utf-8 -*-
"""Clearfix Block

A block to provide a clearfix element for Wagtail's StreamField.
"""


from wagtail.core.blocks import IntegerBlock
from wagtail.core.blocks import StructBlock
from django.db.models import IntegerField
from wagtail.core import blocks
from common.blocks.jobs import JobsWholeBlock
from .StructBlockWithStyle import StructBlockWithStyle

class ClearfixBlock(StructBlockWithStyle):

    class Meta:
        template = 'common/blocks/clearfix_block.html'
        icon = 'placeholder'
        label = 'Clearfix Block'
        help_text = ('When you need to make sure that your next element(s) is on a new line from '
                     'the previous elements, use this little helper block.')

class WhitespaceBlock(StructBlockWithStyle):

    height = IntegerBlock()



    class Meta:
        template = 'common/blocks/whitespace_block.html'
        icon = 'placeholder'
        label = 'Whitespace Block'
        help_text = ('When you need to make sure that your next element(s) is on a new line from '
                     'the previous elements, use this little helper block.')


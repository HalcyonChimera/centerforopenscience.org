from .StructBlockWithStyle import StructBlockWithStyle
from wagtail.core import blocks
from common.blocks import LANGUAGE_CHOICES

class CodeBlock(StructBlockWithStyle):

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES, default="python")
    codes = blocks.TextBlock()

    class Meta:
        # form_template = 'common/block_forms/code_block.html'
        template = 'common/blocks/code_block.html'
        icon = 'edit'
        label = 'Codes'

from .StructBlockWithStyle import StructBlockWithStyle
from wagtail.core import blocks


class CenteredTextBlock(StructBlockWithStyle):
    text = blocks.RichTextBlock()

    class Meta:
        template = 'common/blocks/centered_text.html'
        icon = 'fa-align-center'
        label = 'Centered Text Block'

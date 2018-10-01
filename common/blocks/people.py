from wagtail.core import blocks
from .StructBlockWithStyle import StructBlockWithStyle

PEOPLE_DISPLAY_CHOICES = [
    ('concise-team', 'concise-team'),
    ('concise-ambassador', 'concise-ambassador'),
    ('detailed', 'detailed'),
]

class PeopleBlock(StructBlockWithStyle):
    displayStyle = blocks.ChoiceBlock(choices=PEOPLE_DISPLAY_CHOICES,default="concise-team")
    tag = blocks.CharBlock(max_length=20)

    class Meta:
        template = 'common/blocks/people_block.html'
        icon = 'group'
        label = "PeopleBlock"

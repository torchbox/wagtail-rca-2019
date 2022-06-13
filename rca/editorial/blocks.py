from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock

from rca.utils import blocks as utils_blocks


class EditorialPageBlock(blocks.StreamBlock):
    image = utils_blocks.ImageChooserBlock()
    heading = blocks.CharBlock(
        form_classname="full title",
        icon="title",
        template="patterns/molecules/streamfield/blocks/heading_block.html",
    )
    paragraph = blocks.RichTextBlock()
    embed = EmbedBlock()
    quote = utils_blocks.QuoteBlock()
    jw_video = utils_blocks.JWPLayerBlock()

    class Meta:
        template = "patterns/molecules/streamfield/stream_block.html"

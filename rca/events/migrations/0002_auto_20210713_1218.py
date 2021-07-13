# Generated by Django 3.1.10 on 2021-07-13 11:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetailpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(form_classname='full title', icon='title', template='patterns/molecules/streamfield/blocks/heading_block.html')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(form_classname='title', help_text='Enter quote text only, there is no need to add quotation marks')), ('author', wagtail.core.blocks.CharBlock(required=False)), ('job_title', wagtail.core.blocks.CharBlock(required=False))]))], default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdetailpage',
            name='call_to_action',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='A large heading diplayed at the top of block', required=False)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False))], help_text='An optional link to display below the expanded content', required=False))]))], blank=True),
        ),
    ]

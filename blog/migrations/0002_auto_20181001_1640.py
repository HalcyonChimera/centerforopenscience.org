# Generated by Django 2.0.9 on 2018-10-01 16:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0001_initial'),
        ('wagtailimages', '0021_image_file_hash'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpageperson',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.Person'),
        ),
        migrations.AddField(
            model_name='blogpageperson',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='blog.BlogPage'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_authors',
            field=models.ManyToManyField(blank=True, through='blog.BlogPagePerson', to='common.Person'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_categories',
            field=models.ManyToManyField(blank=True, through='blog.BlogCategoryBlogPage', to='blog.BlogCategory'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='footer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.Footer'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Header image'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='footer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.Footer'),
        ),
        migrations.AddField(
            model_name='blogcategoryblogpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.BlogCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='blogcategoryblogpage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.BlogPage'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have children categories for Bebop and Big Band. Totally optional.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blog.BlogCategory'),
        ),
    ]

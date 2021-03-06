# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("api_v2", "0004_auto_20180821_2221")]

    operations = [
        migrations.CreateModel(
            name="TopicRelationship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_timestamp",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("update_timestamp", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={"db_table": "topic_relationship"},
        ),
        migrations.RemoveField(model_name="credential", name="topics"),
        migrations.AddField(
            model_name="credential",
            name="topics",
            field=models.ManyToManyField(
                related_name="credentials",
                through="api_v2.TopicRelationship",
                to="api_v2.Topic",
            ),
        ),
        migrations.AddField(
            model_name="topic",
            name="related_topics",
            field=models.ManyToManyField(
                related_name="_topic_related_topics_+",
                through="api_v2.TopicRelationship",
                to="api_v2.Topic",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="topic", unique_together=set([("source_id", "type")])
        ),
        migrations.AddField(
            model_name="topicrelationship",
            name="credential",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topic_relationships",
                to="api_v2.Credential",
            ),
        ),
        migrations.AddField(
            model_name="topicrelationship",
            name="related_topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="api_v2.Topic",
            ),
        ),
        migrations.AddField(
            model_name="topicrelationship",
            name="topic",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="api_v2.Topic",
            ),
        ),
    ]

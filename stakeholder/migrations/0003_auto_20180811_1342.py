# Generated by Django 2.0.8 on 2018-08-11 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0002_auto_20180220_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billposition',
            name='bill',
            field=models.ForeignKey(help_text='The bill this position is on.', on_delete=django.db.models.deletion.PROTECT, related_name='stakeholder_positions', to='bill.Bill'),
        ),
        migrations.AlterField(
            model_name='billposition',
            name='position',
            field=models.IntegerField(blank=True, choices=[(1, 'Support'), (0, 'Neutral'), (-1, 'Oppose')], help_text="The stakeholder's position on the bill: against (-1), neutral/it's complicated (0), 1 (support), or null if the stakeholder is merely providing a summary and has no position.", null=True),
        ),
        migrations.AlterField(
            model_name='billposition',
            name='post',
            field=models.ForeignKey(help_text='The post that this position is related to.', on_delete=django.db.models.deletion.CASCADE, related_name='bill_positions', to='stakeholder.Post'),
        ),
        migrations.AlterField(
            model_name='voteposition',
            name='position',
            field=models.IntegerField(blank=True, choices=[(1, 'Aye/Yea'), (0, 'Neutral'), (-1, 'No/Nay')], help_text="The stakeholder's position on the vote: against (-1), neutral/it's complicated (0), 1 (support), or null if the stakeholder is merely providing a summary and has no position.", null=True),
        ),
        migrations.AlterField(
            model_name='voteposition',
            name='post',
            field=models.ForeignKey(help_text='The post that this position is related to.', on_delete=django.db.models.deletion.CASCADE, related_name='vote_positions', to='stakeholder.Post'),
        ),
        migrations.AlterField(
            model_name='voteposition',
            name='vote',
            field=models.ForeignKey(help_text='The vote this position is on.', on_delete=django.db.models.deletion.PROTECT, related_name='stakeholder_positions', to='vote.Vote'),
        ),
    ]
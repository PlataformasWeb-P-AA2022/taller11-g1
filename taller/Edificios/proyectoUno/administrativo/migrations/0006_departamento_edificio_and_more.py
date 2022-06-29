# Generated by Django 4.0.5 on 2022-06-29 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_estudiante_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('costo_depa', models.DecimalField(decimal_places=2, max_digits=100)),
                ('num_cuartos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30, unique=True)),
                ('tipo', models.CharField(choices=[('residencial', 'Edificio Residencial'), ('comercial', 'Edificio comercial')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='numerotelefonico',
            name='estudiante',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='NumeroTelefonico',
        ),
        migrations.AddField(
            model_name='departamento',
            name='edificio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edificio_depa', to='administrativo.edificio'),
        ),
    ]
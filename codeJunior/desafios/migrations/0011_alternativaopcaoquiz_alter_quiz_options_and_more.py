# Generated by Django 4.2.4 on 2023-10-08 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_perfil'),
        ('desafios', '0010_opcaoquiz_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativaOpcaoQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição da opção do quiz')),
                ('correta', models.BooleanField(default=True, help_text='Indica se a alternativa está correta', verbose_name='Correta?')),
                ('ativo', models.BooleanField(default=True, help_text='Indica se a alternativa está ativo', verbose_name='Está ativo?')),
                ('ordem', models.IntegerField(default=1, verbose_name='Ordenação')),
            ],
            options={
                'verbose_name': 'Alternativa opção do quiz',
                'verbose_name_plural': 'Alternativas das opções do quiz',
            },
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Quiz', 'verbose_name_plural': 'Quiz'},
        ),
        migrations.RemoveField(
            model_name='opcaoquiz',
            name='correta',
        ),
        migrations.RemoveField(
            model_name='opcaoquiz',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='opcaoquiz',
            name='titulo',
            field=models.TextField(max_length=200, verbose_name='Descrição da opção do quiz'),
        ),
        migrations.CreateModel(
            name='RespostaQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('alternativaSelecionada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desafios.alternativaopcaoquiz', verbose_name='Alternativa da opcao do Quiz')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desafios.opcaoquiz', verbose_name='Opção do Quiz')),
                ('quemRespondeu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastro.pessoa', verbose_name='Quem Respondeu')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desafios.quiz', verbose_name='Quiz')),
            ],
            options={
                'verbose_name': 'Resposta da opção do quiz',
                'verbose_name_plural': 'Respostas da opções do quiz',
            },
        ),
        migrations.AddField(
            model_name='opcaoquiz',
            name='alternativas',
            field=models.ManyToManyField(to='desafios.alternativaopcaoquiz', verbose_name='Opções do Quiz'),
        ),
    ]

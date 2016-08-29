#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import sm_lib

setup(
    name='writter.py',
    version=sm_lib.__version__,

    # Liste les packages à insérer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),

    author="Rousseau Alexandre",
    author_email="rousseaualexandre.lyon@gmail.com",

    description="a simply class used to normalize all input/output in console",

    long_description=open('README.md').read(),

    # Vous pouvez rajouter une liste de dépendances pour votre lib
    # et même préciser une version. A l'installation, Python essayera de
    # les télécharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,

    # Une url qui pointe vers la page officielle de votre lib
    url='http://github.com/sametmax/sm_lib',

    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue, alors je vous
    # l'ai mise sur 0bin: http://is.gd/AajTjj
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: Windows 7 Entreprise",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],


    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme django-admin.
    # Par exemple, si on veut créer la fabuleuse commande proclame-sm, on
    # va faire pointer ce nom vers la fonction proclame. La commande sera
    # créé automatiquement. La syntaxe package.module.fonction.
    entry_points = {
        'console_scripts': [
            'proclame-sm = sm_lib.core:proclamer',
        ],
    },

    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="WTFPL",

)

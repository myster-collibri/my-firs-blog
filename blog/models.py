from django.db import models

# Create your models here.
#les classe d'ici represente le table de la base de donnees

class Categorie(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    #on_delete cad si on suprime une categorie tout les article associer seront supprimer
    #la cle etrangere vers la table Category
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



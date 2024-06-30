from django import models

class information(models.Model):
    name =models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    age = models.IntegerField()
    

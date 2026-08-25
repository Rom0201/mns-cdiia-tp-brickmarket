from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("nom", max_length=100, unique=True)
    description = models.TextField("description", blank=True, null=False)
    slug = models.SlugField("identifiant url", max_length=100, unique=True)
    
    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField("nom", max_length=200)
    short_description = models.TextField("description courte", blank=True)
    price = models.PositiveIntegerField("Prix")
    #image_path = models.CharField("Chemin de l'image", max_length=150)
    image_url = models.URLField("adresse complète", max_length=500)
    age = models.CharField("âge consiellé", max_length=50, blank=True)
    parts_count = models.PositiveIntegerField("nombre de pièces", blank=True)

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Disponible"
        OUT_OF_STOCK = "OUT_OF_STOCK", "Rupture de stock"
        PREORDER = "PREORDER", "Pré-commande"
        OUTOFSTOCK = "OUTOFSTOCK", "hors stock"

    status = models.CharField("disponibilité", max_length=20, choices=Status, default=Status.AVAILABLE)
    rewards_point = models.PositiveIntegerField("points de récompense", default=0)
    slug = models.SlugField("identifiant url", max_length=200, unique=True)
    category = models.ForeignKey(Category, verbose_name="catégorie", on_delete=models.PROTECT, related_name="products")
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    
    @property
    def price_display(self):
        return f"{self.price / 100:.2f}"

    class Meta:
        verbose_name = "set lego"
        verbose_name_plural = "sets lego"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

from uuid import uuid4

from django.db import models
from common.models import CommonModel
from django.utils.timezone import now
from common.manager import GeneralManager, AllObjectsManager

# Create your models here.
class Listing(CommonModel):   
    class SaleType(models.TextChoices):
        FOR_SALE = "For Sale"
        FOR_RENT = "For Rent"
    class HomeType(models.TextChoices):
        HOUSE = "House"
        CONDO = "Condo"
        TOWNHOUSE = "Townhouse"
        MULTI_FAMILY = "Multi-Family"
        LAND = "Land"    
    realtor = models.CharField(max_length=255)
    title = models.CharField(max_length=255,db_index=True) 
    slug = models.SlugField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255,db_index=True)
    state = models.CharField(max_length=255,db_index=True)
    zipcode = models.CharField(max_length=255,db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(db_index=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sale_type = models.CharField(max_length=255, choices=SaleType.choices,default=SaleType.FOR_SALE )
    home_type = models.CharField(max_length=255, choices=HomeType.choices,default=HomeType.HOUSE )
    main_photo = models.ImageField(upload_to="listing_photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="listing_photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="listing_photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="listing_photos/%Y/%m/%d/", blank=True)
    status = models.CharField(max_length=255,choices=[("drafts", "Drafts"), ("published", "Published")], default="drafts", db_index=True)
  
    #---------------Objects manager-----------------
    objects = GeneralManager()
    #---------------------------All objects manager to include soft deleted objects-----------------
    all_objects = AllObjectsManager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = "Listings"
        verbose_name = "Listing"
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_slug")
        ]
    #Composite index for city, state, and zipcode to optimize search queries
        indexes = [
            models.Index(fields=["city", "state", "zipcode"]),
        ]    
    
    def save(self, *args, **kwargs):
        if not self.uniqueId:
            self.uniqueId = uuid4().hex[:12]
        super().save(*args, **kwargs)
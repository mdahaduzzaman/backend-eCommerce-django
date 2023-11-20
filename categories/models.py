import uuid
from django.db import models
from django.utils.text import slugify

class MainCategory(models.Model):
    id = models.CharField(max_length=100, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_category_images/', blank=True, null=True)
    icon = models.CharField(max_length=100, null=True)
    icon_from = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If ID is not set
            base_id = slugify(self.name)
            new_id = base_id
            while MainCategory.objects.filter(id=new_id).exists():
                random_chars = str(uuid.uuid4())[:4]  # Get 4 random characters from UUID
                new_id = f"{base_id}-{random_chars}"
            self.id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.CharField(max_length=100, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sub_category_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If ID is not set
            base_id = slugify(self.name)
            new_id = base_id
            while SubCategory.objects.filter(id=new_id).exists():
                random_chars = str(uuid.uuid4())[:4]  # Get 4 random characters from UUID
                new_id = f"{base_id}-{random_chars}"
            self.id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubSubCategory(models.Model):
    id = models.CharField(max_length=100, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sub_sub_category_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If ID is not set
            base_id = slugify(self.name)
            new_id = base_id
            while SubSubCategory.objects.filter(id=new_id).exists():
                random_chars = str(uuid.uuid4())[:4]  # Get 4 random characters from UUID
                new_id = f"{base_id}-{random_chars}"
            self.id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

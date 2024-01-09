from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    video = models.FileField(upload_to='news/videos/', null=True, blank=True)
    photo1 = models.ImageField(upload_to='news/photos/', blank=True)
    photo2 = models.ImageField(upload_to='news/photos/', blank=True)
    photo3 = models.ImageField(upload_to='news/photos/', blank=True)
    photo4 = models.ImageField(upload_to='news/photos/', blank=True)
    photo5 = models.ImageField(upload_to='news/photos/', blank=True)
    photo6 = models.ImageField(upload_to='news/photos/', blank=True)
    photo7 = models.ImageField(upload_to='news/photos/', blank=True)
    photo8 = models.ImageField(upload_to='news/photos/', blank=True)
    photo9 = models.ImageField(upload_to='news/photos/', blank=True)
    photo10 = models.ImageField(upload_to='news/photos/', blank=True)


def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='trainers/')
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.ManyToManyField('MerchandisePhoto', blank=True, related_name='merchandise_photos')
    sizes = models.ManyToManyField('Size', blank=True)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class MerchandisePhoto(models.Model):
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='merchandise/')


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.name


class TrainingRegistration(models.Model):
    LEVEL_CHOICES = [
        ('advanced', 'Advanced'),
        ('beginner', 'Beginner'),
        ('child', 'Child'),
    ]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    parent_name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    account_number = models.CharField(max_length=20)
    email = models.EmailField()
    registration_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.address


class AboutUs(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
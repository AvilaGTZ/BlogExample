from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('State', default=True)
    creationDate = models.DateField('Creation date', auto_now=False, auto_now_add= True)
    modDate = models.DateField('Modification date', auto_now=True, auto_now_add=False)
    delDate = models.DateField('Modification date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True  #Will not add this to the database 

class Category(BaseModel):
    name = models.CharField('Category name', max_length=100, unique=True)
    imageRef = models.ImageField('Reference image', upload_to='category/')

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField('Name', max_length=100)
    lastName = models.CharField('Last name', max_length=120)
    email = models.EmailField('Email', max_length=200)
    desc  = models.TextField('Description', max_length=500)
    refImage = models.ImageField('Ref image', upload_to='authors/', max_length=255, null=True, blank=True)
    web   = models.URLField('Web', null = True, blank = True)
    facebook   = models.URLField('Facebook', null = True, blank = True)
    twitter   = models.URLField('Twitter', null = True, blank = True)
    instagram   = models.URLField('Instagra,', null = True, blank = True)

    class Meta:
        verbose_name= 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return '{0},{1}'.format(self.lastName, self.name)

class Post(BaseModel):
    title = models.CharField('Title', max_length=150, unique=True)
    slug  = models.CharField('Slug', max_length=150, unique=True)
    desc = models.TextField('Description')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField()
    refImage = models.ImageField('Ref image', upload_to='images/', max_length=255)
    published = models.BooleanField('Published', default=False)
    publishDate = models.DateField('Publish date')


    class Meta:
        verbose_name= 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Web(BaseModel):
    aboutUs = models.TextField('About us')
    phone = models.CharField('Phone', max_length=10)
    email = models.EmailField('Email', max_length=200)
    address = models.CharField('Address', max_length=200)

    class Meta:
        verbose_name= 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.aboutUs


class SocialNetworks(BaseModel):
    facebook = models.URLField('Facebook')
    twitter  = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name= 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return self.facebook


class Contact(BaseModel):
    name = models.CharField('Name', max_length=100)
    lastName = models.CharField('Last name', max_length=150)
    email    = models.EmailField('Email', max_length=200)
    topic    = models.CharField('Topic', max_length=100)
    message = models.TextField('Message')

    class Meta:
        verbose_name= 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.topic

class Suscription(BaseModel):
    email = models.EmailField('Email', max_length=200)

    class Meta:
        verbose_name= 'Suscription'
        verbose_name_plural = 'Suscriptions'

    def __str__(self):
        return self.email
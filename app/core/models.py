from django.db import models


# HOME
class Home(models.Model):
    #Sidevar
    name = models.CharField(max_length=20, verbose_name='Name of Page')    
    acronym = models.CharField(max_length=2, verbose_name='Acronym of Name')
    title = models.CharField(max_length=20, verbose_name='Title of Page')
    instagram_url = models.URLField(verbose_name='Your instagram url')
    github_url = models.URLField(verbose_name='Your Git-Hub url')
    #Page Section
    greetings_1 = models.CharField(max_length=5, verbose_name='Greetings in page 1st')
    greetings_2 = models.CharField(max_length=5, verbose_name='Greetings in page 2nd')
    picture = models.ImageField(upload_to='img/home/' , verbose_name='Your Photo')
    # Save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# ABOUT
class About(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Heading or greetings')
    career = models.CharField(max_length=50, verbose_name='Career')
    description = models.TextField(blank=False, verbose_name='Description')
    profile_img = models.ImageField(upload_to='img/home/', verbose_name='Your profile photo')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

    # remember include icons skills


# SKILLS
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Profession')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)
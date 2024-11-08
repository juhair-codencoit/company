from django.db import models
#from django.utils.text import slugify

class Industry(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Projects(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()
    industry_id = models.ForeignKey(Industry,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
   
class ProjectImage(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_pic/")  
    
    
class Services(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceProduct(models.Model):
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

   
class Technologies(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="tech_icon/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechnologiesProduct(models.Model):
    tech_id = models.ForeignKey(Technologies,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    
    
class TeamMember(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team_member/")


class ClientStatement(models.Model): 
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    client_statement = models.TextField()
    client_picture = models.ImageField(upload_to='client_pic/')
    company_logo = models.ImageField(upload_to='company_logo/')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

   
class FAQ(models.Model):

    LANDING_PAGE = 'LP'
    INDUSTRY_PAGE = 'IP'
    SERVICE_PAGE = 'SP'
    TECHNOLOGY_PAGE = 'TP'

    PAGE_CHOICES =[
        (LANDING_PAGE, 'Landing'),
        (INDUSTRY_PAGE, 'Industry'),
        (SERVICE_PAGE, 'Service'),
        (TECHNOLOGY_PAGE, 'Technology'),
    ]

    name = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answear = models.CharField(max_length=255)
    page_name = models.CharField(max_length=3, choices=PAGE_CHOICES, default=LANDING_PAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField()
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Request_estimation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField()
    company_name = models.CharField(max_length=255)
    project_description = models.TextField()
    budget = models.IntegerField()
    project_document = models.FileField(upload_to='project_documents/')
    meeting_schedule = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
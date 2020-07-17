from django.db import models

# Create your models here.


JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


def img_upload(instance, filename):
    imgname, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)


class Job(models.Model):    # table
    title = models.CharField(max_length=100)   # column
    # location
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)   # jobs numbers
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=img_upload)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

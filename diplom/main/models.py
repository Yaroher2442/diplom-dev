from django.db import models


class Funnels(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    descr = models.CharField(max_length=200)


class Clients(models.Model):
    funnel = models.ForeignKey(Funnels, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    descr = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    change_time = models.DateTimeField()


class Cases(models.Model):
    funnel = models.ForeignKey(Funnels, on_delete=models.CASCADE)
    f_position = models.IntegerField(default=0)
    stage = models.CharField(max_length=200, default='')
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    descr = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    change_time = models.DateTimeField()
    executor = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)


class Tasks(models.Model):
    case = models.ForeignKey(Cases, on_delete=models.CASCADE)
    descr = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    change_time = models.DateTimeField()
    status = models.CharField(max_length=200, default='')

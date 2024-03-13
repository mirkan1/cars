from django.db import models
from django.contrib.auth.models import Group, User as _User

class Group(Group):
    users = models.ManyToManyField(_User, blank=True)
    moderators = models.ManyToManyField(_User, related_name='moderators', blank=True) # some groups have 3 moderators
    # orned group
        # edremit araba toplulugu
        # jetta turkiye from facebook, ayriyetten jetta turkiye whatsapp grubu var
    cars_on_sale = models.ManyToManyField('Car', blank=True)
    picture = models.ImageField(upload_to='groups', null=True, blank=True)
    join_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    # biyos app example 5$ per month
    # generally monthly
    # some groups wants monthly payment for being a member on whatsapp or facebook groups
    sponsors = models.ManyToManyField(_User, related_name='sponsors', blank=True)
    # when a user aks questions useing "!" the output should be seen by the users
        # for example a user asks "!expertise" and the output should be seen by the users like from twitch.com
    # he need to have chat in every group that floods
    history = models.TextField(null=True, blank=True) # many text fields about chat history
    # 24 hours clearing might be good
    # we can do it like telegram so that only got the first 50 messages, get the rest only wehen user swipe up
    notifications = models.TextField(null=True, blank=True) # many text fields about notifications
    group_point = models.IntegerField(default=0) # good group, bad group
    # group reputation
    rules = models.TextField(null=True, blank=True) # many text fields about rules
    # it will be like a forum, rules can be seen by everyone and will be like description

    def __str__(self):
        return self.name

class Chat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(_User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # we can do it like telegram so that only got the first 50 messages, get the rest only wehen user swipe up

    def __str__(self):
        return self.group.name + ' - ' + self.user.username + ': ' + self.message


class User(_User):
    blood_type = models.CharField(max_length=3, null=True, blank=True)
    owned_car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True, blank=True)
    national_number = models.CharField(max_length=11, null=True, blank=True)
    where_did_user_come_from = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='users', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    # need email proof from the user so that we know the user is real
    job = models.CharField(max_length=100, null=True, blank=True)
    socials = models.TextField(null=True, blank=True) # many text fields about socials
    user_type = models.CharField(max_length=100, null=True, blank=True) # premium user etc.
    user_point = models.IntegerField(default=0)
    city = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.username


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    owner = models.ForeignKey(_User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cars', null=True, blank=True)
    pivture_3d = models.FileField(upload_to='cars', null=True, blank=True) # at the end it will be an url that shows the 3d model as blender object or sth like this
    is_car_on_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    car_history = models.TextField(null=True, blank=True) # many text fields about car history
    changed_car_parts = models.TextField(null=True, blank=True) # many text fields about changed car parts
    

    def __str__(self):
        return self.make + ' ' + self.model + ' (' + str(self.year) + ')'


class Radar(models.Model):
    # radar is a device that detects the speed of the cars
    # we wantt o show users known radar locations
    # we can get it form our users or admins
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    when_radar_found = models.DateTimeField(auto_now_add=True)
    # dogrulandi mi?
    confirmed = models.BooleanField(default=False)


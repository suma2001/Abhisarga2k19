from django.conf import settings
from django.db import models

# Create your models here.

def get_event_photo_path(instance, filename):
	return "Event/{0}/{1}".format(instance.name, filename)

def get_event_category_photo_path(instance, filename):
	return "EventCategory/{0}/{1}".format(instance.category, filename)

class EventCategory(models.Model):
	category = models.CharField(max_length=100, null=True, blank=True)
	image = models.ImageField(upload_to=get_event_category_photo_path, null=True, blank=True)
	description = models.TextField()
	web_priority = models.IntegerField(default=0)
	app_priority = models.IntegerField(default=0)

	def __str__(self):
		return self.category

class Event(models.Model):
	event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name="event_category")
	name = models.CharField(max_length=200, null=True, blank=True)
	logo = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	registration_from = models.DateTimeField(null=True, blank=True)
	registration_to = models.DateTimeField(null=True, blank=True)
	event_from = models.DateTimeField(null=True, blank=True)
	event_to = models.DateTimeField(null=True, blank=True)
	participant_limit = models.IntegerField(default=0)
	participant_count = models.IntegerField(default=0)
	description = models.TextField()
	rules = models.TextField()
	prize = models.TextField()
	brochure = models.FileField(upload_to=get_event_photo_path, null=True, blank=True)
	organisers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="organising_events")
	#volunteers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="volunteering_events")
	web_priority = models.IntegerField(default=0)
	app_priority = models.IntegerField(default=0)
	registration_closed = models.BooleanField(default=False)
	team_event = models.BooleanField(default=False)

	img_1 = models.FileField(upload_to=get_event_photo_path, null=True, blank=True)
	img_2 = models.FileField(upload_to=get_event_photo_path, null=True, blank=True)
	img_3 = models.FileField(upload_to=get_event_photo_path, null=True, blank=True)
	img_4 = models.FileField(upload_to=get_event_photo_path, null=True, blank=True)

	qr_code_string = models.CharField(max_length=100, null=True, blank=True)

	@property
	def registration_full(self):
		teams = Team.objects.filter(event__id=self.id)
		return False if len(teams) < self.participant_limit else True

	def __str__(self):
		teams=list()
		if self.id:
			teams = Team.objects.filter(event__id=self.id)
		return str(self.name) + ' - ' + str(len(teams))


class Team(models.Model):
	team_name = models.CharField(max_length=50, null=True, blank=True)
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participating_events")
	leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="team_leader_of")
	
	present_for_event = models.BooleanField(default=False)

	def __str__(self):
		return str(self.team_name) + ' - ' + str(self.event.name)


class Member(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="belong_to_team")
	name = models.CharField(max_length=100, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	mobile_no = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return str(self.name) + ' - ' + str(self.email)


class EventCatalogue(models.Model):
	event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="catalogue_of")
	image1 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	image2 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	image3 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	image4 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	image5 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)
	image6 = models.ImageField(upload_to=get_event_photo_path, null=True, blank=True)

	def __str__(self):
		return str(self.event.name) + "Catalogue"
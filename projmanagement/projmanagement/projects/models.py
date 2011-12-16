from django.db import models

# Create your models here.
class Project(models.Model):
	STATUS_CHOICES = (
		('N' , 'Not Started'),
		('S' , 'Started'),
		('F' , 'Finished'),
	)	
	codeName = models.CharField(max_length = 50)
	name = models.CharField(max_length = 200)
	status = models.CharField(max_length = 1, choices=STATUS_CHOICES, default='N')
	initDate = models.DateField(null=True, blank=True)
	dateToFinish = models.DateField(null=True, blank=True)
	comments = models.CharField(max_length = 300, blank=True)
	
	def __unicode__(self):
		return self.codeName + ' - ' + self.name

class Phase(models.Model):
	STATUS_CHOICES = (
		('N' , 'Not Started'),
		('S' , 'Started'),
		('F' , 'Finished'),
	)	
	phaseNumber = models.IntegerField()
	name = models.CharField(max_length = 200)
	project = models.ForeignKey(Project)
	isUnique = models.BooleanField()
	initDate = models.DateField(null=True, blank=True)
	status = models.CharField(max_length = 1, choices=STATUS_CHOICES, default='N')
	comments = models.CharField(max_length = 300, blank=True)

	def __unicode__(self):
		return str(self.phaseNumber) + ' - ' + self.name	
	
class Task(models.Model):
	STATUS_CHOICES = (
		('N' , 'Not Started'),
		('S' , 'Started'),
		('F' , 'Finished'),
		('ST', 'Stalled'),
	)	
	TASK_TYPES = (
		('PS', 'Proposal'),
		('PL', 'Planning'),
		('MG', 'Management'),
		('A', 'Analysis'),
		('TD', 'Technic Design'),
		('PG', 'Programming'),
		('T', 'Testing'),
		('PP', 'Preparing for production'),
		('IO', 'IOP'),
	)
	name = models.CharField(max_length=200)
	taskType = models.CharField(max_length=2, choices=TASK_TYPES, blank=True)
	phase = models.ForeignKey(Phase) 
	order = models.IntegerField(null=True, blank=True)
	level = models.IntegerField(default=1)
	superTask = models.ForeignKey('self',null=True, blank=True)
	predecessor = models.ManyToManyField('self', null=True, blank=True)
	successor = models.ManyToManyField('self', null=True, blank=True)
	estimateCost = models.IntegerField(null=True, blank=True)
	estimateInitDate = models.DateField(null=True, blank=True)
	EstimateEndDate = models.DateField(null=True, blank=True)
	realInitDate = models.DateField(null=True, blank=True)
	realEndDate = models.DateField(null=True, blank=True)
	realCost = models.IntegerField(null=True, blank=True)
	status = models.CharField(max_length = 2, choices=STATUS_CHOICES, default='N')
	comments = models.CharField(max_length = 300, blank=True)	

	def __unicode__(self):
		return self.name	

class Team(models.Model):
	name = models.CharField(max_length=200)
	surname1 = models.CharField(max_length=200, null=True, blank=True)
	surname2 = models.CharField(max_length=200, null=True, blank=True)
	TSOUsername = models.CharField(max_length=10, null=True, blank=True)
	IMSusername = models.CharField(max_length=10, null=True, blank=True)
	tasks = models.ManyToManyField(Task, through='Assignment', null=True, blank=True)

	def __unicode__(self):
		return self.name + ' ' + self.surname1	
	
class Assignment(models.Model):
	responsible = models.ForeignKey(Team)
	task = models.ForeignKey(Task)
	assignedCost = models.IntegerField(null=True, blank=True)
	compromiseDate = models.DateField(null=True, blank=True)
	comments = models.CharField(max_length = 300, blank=True)		

	def __unicode__(self):
		return self.esponsible.name + ' - ' + self.task.name	
	
class WorkReport(models.Model):
	assignment = models.ForeignKey(Assignment)
	dayReport = models.DateField()
	timeReport = models.IntegerField()
	
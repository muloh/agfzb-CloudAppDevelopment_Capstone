from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User



# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
	name 		= models.CharField(max_length=150)
	Description = models.TextField()

	created_by = models.ForeignKey(User, related_name = 'CarMake_created_by', null = True, editable=False, on_delete=models.CASCADE)
	modified_by = models.ForeignKey(User, related_name = 'CarMake_modified_by', null = True, editable=False, on_delete=models.CASCADE)
	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
	auto_date_only = models.DateField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
# class CarDealer(models.Model):
# 	name = models.ForeignKey(User, on_delete = models.CASCADE)
# 	phone = models.CharField(max_length = 100)
# 	address = models.CharField(max_length = 250)

# 	created_by = models.ForeignKey(User, related_name = 'CarDealer_created_by', null = True, editable=False, on_delete=models.CASCADE)
# 	modified_by = models.ForeignKey(User, related_name = 'CarDealer_modified_by', null = True, editable=False, on_delete=models.CASCADE)
# 	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
# 	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
# 	auto_date_only = models.DateField(auto_now_add = True, null = True)
# # 
class CarDealer:

	def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
		# Dealer address
		self.address = address
		# Dealer city
		self.city = city
		# Dealer Full Name
		self.full_name = full_name
		# Dealer id
		self.id = id
		# Location lat
		self.lat = lat
		# Location long
		self.long = long
		# Dealer short name
		self.short_name = short_name
		# Dealer state
		self.st = st
		# Dealer zip
		self.zip = zip

	def __str__(self):
		return "Dealer name: " + self.full_name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
	MODEL_TYPE = (
		('Sedan', 'Sedan'),
		('SUV', 'SUV'),
		('WAGON', 'WAGON'),
	)
	make 		= models.ForeignKey(CarMake, on_delete = models.CASCADE)
	dealer_id 	= models.IntegerField() # dealer id created in cloudant database
	name 		= models.CharField(max_length=150)
	model_type 	= models.CharField(max_length = 200, choices=MODEL_TYPE)
	year 		= models.DateField()

	created_by = models.ForeignKey(User, related_name = 'CarModel_created_by', null = True, editable=False, on_delete=models.CASCADE)
	modified_by = models.ForeignKey(User, related_name = 'CarModel_modified_by', null = True, editable=False, on_delete=models.CASCADE)
	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
	auto_date_only = models.DateField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name



# # <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

	def __init__(self, dealership, name, purchase, review):
		# Required attributes
		self.dealership = dealership
		self.name = name
		self.purchase = purchase
		self.review = review
		# Optional attributes
		self.purchase_date = ""
		self.purchase_make = ""
		self.purchase_model = ""
		self.purchase_year = ""
		self.sentiment = ""
		self.id = ""

	def __str__(self):
		return "Review: " + self.review

	def to_json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
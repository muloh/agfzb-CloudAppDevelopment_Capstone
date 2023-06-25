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
class CarDealer(models.Model):
	name = models.ForeignKey(User, on_delete = models.CASCADE)
	phone = models.CharField(max_length = 100)
	address = models.CharField(max_length = 250)

	created_by = models.ForeignKey(User, related_name = 'CarDealer_created_by', null = True, editable=False, on_delete=models.CASCADE)
	modified_by = models.ForeignKey(User, related_name = 'CarDealer_modified_by', null = True, editable=False, on_delete=models.CASCADE)
	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
	auto_date_only = models.DateField(auto_now_add = True, null = True)

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
	make = models.ForeignKey(CarMake, on_delete = models.CASCADE)
	dealer = models.ForeignKey(CarDealer, on_delete = models.CASCADE)
	name 		= models.CharField(max_length=150)
	model_type = models.CharField(max_length = 200)
	year = models.DateField()

	created_by = models.ForeignKey(User, related_name = 'CarModel_created_by', null = True, editable=False, on_delete=models.CASCADE)
	modified_by = models.ForeignKey(User, related_name = 'CarModel_modified_by', null = True, editable=False, on_delete=models.CASCADE)
	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
	auto_date_only = models.DateField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name



# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
	car_model = models.ForeignKey(CarModel, on_delete = models.CASCADE)
	review = models.CharField(max_length = 250)

	created_by = models.ForeignKey(User, related_name = 'DealerReview_created_by', null = True, editable=False, on_delete=models.CASCADE)
	modified_by = models.ForeignKey(User, related_name = 'DealerReview_modified_by', null = True, editable=False, on_delete=models.CASCADE)
	auto_date_created = models.DateTimeField(auto_now_add=True, null = True)
	auto_date_time_updated = models.DateTimeField(auto_now = True, null = True)
	auto_date_only = models.DateField(auto_now_add = True, null = True)
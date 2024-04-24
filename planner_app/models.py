from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    username = models.CharField(max_length=45, unique=True, null=False)
    password = models.CharField(max_length=45, null=False)
    birthdate = models.DateField()
    phone = models.CharField(max_length=11, unique=True, null=False)
    email = models.CharField(max_length=45, unique=True, null=False)
    profile_photo = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return str(self.user_id)
    
    
class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    count = models.CharField(max_length=45, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foods', null=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    
    def __str__(self):
        return str(self.food_id)


class Project(models.Model):    
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', null=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.project_id)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    
    def __str__(self):
        return str(self.task_id)
    
class Sport(models.Model):    
    sport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sports', null=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    
    def __str__(self):
        return str(self.sport_id)

class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routines', null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    
    def __str__(self):
        return str(self.routine_id)
    

class Event_project(models.Model):
    id_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    @property
    def start_datetime(self):
        return datetime.combine(self.start_date, self.start_time)

    @property
    def end_datetime(self):
        return datetime.combine(self.end_date, self.end_time)     
    



class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    # class Meta:  
    #     db_table = "tblevents"    




# ------------------------------------------------------- Bridge tables -------------------------------------------------------------
    
# class food_plan(models.Model):
#     id_number = models.AutoField(primary_key=True)
#     date_time = models.DateTimeField()
#     food_id = models.CharField(max_length=45, null=False)
#     user_id = models.CharField(max_length=45, null=False)
    
#     def __str__(self):
#         return str(self.id_number)
    
    
# class project_plan(models.Model):
#     id_number = models.AutoField(primary_key=True)
#     date_time = models.DateTimeField()
#     project_id = models.CharField(max_length=45, null=False)
#     user_id = models.CharField(max_length=45, null=False)
    
#     def __str__(self):
#         return str(self.id_number)
    
    
# class task_plan(models.Model):
#     id_number = models.AutoField(primary_key=True)
#     date_time = models.DateTimeField()
#     task_id = models.CharField(max_length=45, null=False)
#     user_id = models.CharField(max_length=45, null=False)
    
#     def __str__(self):
#         return str(self.id_number)        


# class sport_plan(models.Model):
#     id_number = models.AutoField(primary_key=True)
#     date_time = models.DateTimeField()
#     sport_id = models.CharField(max_length=45, null=False)
#     user_id = models.CharField(max_length=45, null=False)
    
#     def __str__(self):
#         return str(self.id_number)        



# class routine_plan(models.Model):
#     id_number = models.AutoField(primary_key=True)
#     date_time = models.DateTimeField()
#     routine_id = models.CharField(max_length=45, null=False)
#     user_id = models.CharField(max_length=45, null=False)
    
#     def __str__(self):
#         return str(self.id_number)        


   
        
        
        
        
# example for making the database : ---------------------------------------------------------------------------
# 
# my_field = models.AutoField(primary_key=True)

# my_field = models.CharField(unique=True, max_length=100)
# 
# my_field = models.CharField(max_length=100, null=False)
# 
# my_field = models.CharField(max_length=100, default='default_value')
# 
# author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# authors = models.ManyToManyField(Author)   :   many to many relationship

# ------------------------------------------------------------------------------------------------------------


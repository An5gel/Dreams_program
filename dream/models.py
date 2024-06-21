from django.db import models

class Participant(models.Model):
    child_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    
    AGE_GROUP_CHOICES = [
        (10, '10-14 yrs.'),
        (15, '15-19 yrs.'),
    ]
    age_group = models.IntegerField(choices=AGE_GROUP_CHOICES)
    
    HIV_STATUS_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]
    hiv_status = models.CharField(max_length=10, choices=HIV_STATUS_CHOICES)
    
    date_of_birth = models.DateField()
    
    SCHOOLING_STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('not_enrolled', 'Not Enrolled'),
    ]
    schooling_status = models.CharField(max_length=20, choices=SCHOOLING_STATUS_CHOICES)

    def __str__(self):
        return self.child_name

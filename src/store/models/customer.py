from django.db import models
from django.contrib.auth import get_user_model


from django.db.models.signals import post_save
from django.dispatch import receiver


User =  get_user_model()
class Customer(models.Model):
    username= models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
    
@receiver(post_save, sender=Customer)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(email=instance.email,
                            first_name=instance.first_name,
                            last_name=instance.last_name,
                            username=instance.username,
                            password =instance.password 
                               #service=instance.add_count_e_s
                               ) 

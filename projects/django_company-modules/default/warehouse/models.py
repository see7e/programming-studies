from django.db import models

from core.models import Event, Task
from register_login.models import CustomUser

# To simplify the process, in this application was desconsidered the Inbound and Putaway steps, this
# way the system will care only about the Itens that are already in the Inventory and the Outbound
# process. It will also care about the Labor Management and Reporting the operations.

REPORT_CHOICES = [("approved", "Approved"), ("rejected", "Rejected")]

# ## 1. Inbound
# class PurchaseOrder(models.Model):
#     number = models.CharField(max_length=100)
#     barcode = models.CharField(max_length=100)
#     # Add other relevant fields

# class QualityIssue(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     description = models.TextField()
#     photo = models.ImageField(upload_to='quality_issues/')
#     # Add other relevant fields

# ## 2. Putaway
# class Location(models.Model):
#     code = models.CharField(max_length=100)
#     # Add other relevant fields

# class Putaway(models.Model):
#     code = models.ForeignKey(Item, on_delete=models.CASCADE)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     # Add other relevant fields

## 3. Inventory Management
class Shed(models.Model):
    shed = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()


class Rack(models.Model):
    code = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()
    in_shed = models.ForeignKey(Shed, on_delete=models.CASCADE)


class Item(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    quantity = models.IntegerField()
    in_rack = models.ForeignKey(Rack, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     created = not self.pk
    #     super().save(*args, **kwargs)
    #     if created:
    #         # Emit event when a new item is created
    #         Event.objects.create(name='ItemCreated', description=f'Item {self.code} created')

    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {self.quantity}"


## 4. Outbound
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.license_plate


class OutboundRequest(models.Model):
    license_plate = models.CharField(max_length=100)
    products = models.ManyToManyField(Item, through="OutboundProduct")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # for the destination, will be created a tocken that will be used to identify the destination
    # this code will be a hash of the information of the destination (city, state, country)
    destination_code = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     created = not self.pk
    #     super().save(*args, **kwargs)
    #     if created:
    #         # Emit event when a new outbound request is created
    #         Event.objects.create(name='OutboundRequestCreated', description=f'Outbound request {self.id} created')


class OutboundProduct(models.Model):
    outbound_request = models.ForeignKey(OutboundRequest, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()


## 5. Labor Management
# inherits from core.Task


# class Report(models.Model):
#     date = models.DateField()
#     user = models.ForeignKey(CustomUser, related_name='user_reports', on_delete=models.CASCADE)
#     manager = models.ForeignKey(CustomUser, related_name='manager_reports', on_delete=models.CASCADE)
#     description = models.TextField(max_length=150)
#     status = models.CharField(max_length=20, choices=REPORT_CHOICES)

#     def save(self, *args, **kwargs):
#         created = not self.pk
#         super().save(*args, **kwargs)
#         if created:
#             # Emit event when a new report is created
#             Event.objects.create(name='ReportCreated', description=f'Report {self.id} created')
#         else:
#             # Emit event when a report is updated
#             Event.objects.create(name='ReportUpdated', description=f'Report {self.id} updated')

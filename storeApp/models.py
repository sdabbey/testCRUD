from mongoengine import Document, fields
from db_connection import db
# Create your models here.



class Product(Document):
    productId = fields.SequenceField()
    productName = fields.StringField(max_length=200)
    productPrice = fields.IntField()

    def __str__(self):
        return self.productName


class Customer(Document):
    customerName = fields.StringField(max_length=200)

    def __str__(self):
        return self.customerName
    
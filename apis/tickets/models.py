# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename

from products.models import (
    Product
)

from users.models import (
    CustomUser
)

class TicketTopic(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')

    TOPIC_CATEGORY = [
        ('GN', 'General'),
        ('EG', 'eGovernment')
    ]
    topic_category = models.CharField(
        choices=TOPIC_CATEGORY,
        max_length=2,
        default='GN'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class TicketSubject(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='NA')

    SUBJECT_CATEGORY = [
        ('GN', 'General'),
        ('EG', 'eGovernment')
    ]
    subject_category = models.CharField(
        choices=SUBJECT_CATEGORY,
        max_length=2,
        default='GN'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Ticket(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default='NA')
    description = models.TextField(default='NA')

    TICKET_TYPE = [
        ('GN', 'General'),
        ('EG', 'eGovernment')
    ]
    ticket_type = models.CharField(
        choices=TICKET_TYPE,
        max_length=2,
        default='GN'
    )
    
    TICKET_STATUS = [
        ('RS', 'Resolved'),
        ('US', 'Unresolved')
    ]
    ticket_status = models.CharField(
        choices=TICKET_STATUS,
        max_length=2,
        default='US'
    )
    
    topic = models.ForeignKey(TicketTopic, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(TicketSubject, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


    receipt_number = models.CharField(max_length=100, default='NA')
    attached_document = models.FileField(null=True, upload_to=PathAndRename('enquiry-attached-document'))
    error_screenshot = models.ImageField(null=True, upload_to=PathAndRename('enquiry-error-screenshot'))
    error_supporting_document = models.FileField(null=True, upload_to=PathAndRename('enquiry-supporting-document'))
    error_product = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class TicketCBID(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requestor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    remarks = models.TextField(default='NA')
    
    ENTITY_TYPE = [
        ('ROB', 'Registration of Business'),
        ('ROC', 'Registration of Company')
    ]
    entity_type = models.CharField(choices=ENTITY_TYPE, max_length=3, default='ROB')

    PRODUCT_TYPE = [
        ('BT', 'Both'),
        ('LT', 'Listing'),
        ('PD', 'Product')
    ]
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=2, default='BT')

    STATUS_TYPE = [
        ('PG', 'Pending'),
        ('PD', 'Paid'),
        ('CP', 'Completed')
    ]
    status = models.CharField(choices=STATUS_TYPE, max_length=2, default='PG')
    
    pending_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['requestor']
    
    def __str__(self):
        return self.entity_type


class TicketInvestigation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    officer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reference_letter_number = models.CharField(max_length=100, default='NA')
    ip_no = models.CharField(max_length=100, default='NA')
    court_case_number = models.CharField(max_length=100, default='NA')
    official_attachment = models.FileField(null=True, upload_to=PathAndRename('investigation-attachment-official'))
    offense = models.CharField(max_length=100, default='NA')
    document_request = models.FileField(null=True, upload_to=PathAndRename('investigation-document-request'))
    submit_request = models.FileField(null=True, upload_to=PathAndRename('investigation-submit-request'))

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['requestor']
    
    def __str__(self):
        return self.entity_type



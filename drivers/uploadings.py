from dataclasses import fields
from email import header
import os
import sys

os.environ['DJANGO_SETTING_MODULE'] = 'my_crm.settings'

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import django
django.setup()

from .models import Driver
import xlrd
import datetime

class UploadingFiles(object):
    foreign_key_fields = ["client", "owner"]
    model = Driver
    
    def __init__(self, data):
        data = data
        self.uploaded_file = data.get("file")
        self.parsing()
        
    def getting_related_model(self, field_name):
        model = self.model
        related_model = model._meta.get_field(field_name).rel.to
        return related_model
    
    def getting_headers(self):
        s = self.s
        headers = dict()
        for column in range(s.ncols):
            value = s.cell(0, column).value
            headers[column] = value
        return headers
    
    def parsing(self):
        uploaded_file = self.uploaded_file
        wb = xlrd.open_workbook(file_contents=uploaded_file.read())
        s = wb.sheet_by_index(0)
        self.s = s
        
        headers = self.getting_headers()
        
        bulk_list = list()
        for row in range(1, s.nrows):
            row_dict = {}
            for column in range(s.ncols):
                value = s.cell(row, column).value
                field_name = headers[column]
                
                if field_name == 'id' and not value:
                    continue
                
                if field_name in self.foreign_key_fields:
                    related_model = self.getting_related_model(field_name)
                    instance, created = related_model.objects.get_or_created(name=value)
                    value = instance
                    
                if 'date' in field_name or field_name=='birthday':
                    cell = s.cell(row, column).value
                    year, month, day, hour, minute, second = xlrd.xldate.xldate_as_tuple(cell, wb.datemode)
                    value = datetime.datetime(year, month, day, hour, minute, second)
                    
                if 'bool' in field_name:
                    if value=='+':
                        value = True
                    else:
                        value = False
                    
                row_dict[field_name] = value
                
            bulk_list.append(Driver(**row_dict))
        
        Driver.objects.bulk_create(bulk_list)
        return True
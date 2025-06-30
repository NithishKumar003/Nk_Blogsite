from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help ='This commands inserts post data'
    
    def handle(self, *args:Any, **options:Any):

        # Deleting exixting data
        
            Category.objects.all().delete()
            
            categories =[
                'Sports', 'Technologies', 'Science', 'Art', 'Food']

            for category_name in categories:
                Category.objects.create(name = category_name)
    
            self.stdout.write(self.style.SUCCESS("Completrd inserting Data!"))
    
    
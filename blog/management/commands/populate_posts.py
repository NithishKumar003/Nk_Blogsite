from blog.models import post, Category
from typing import Any
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help ='This commands inserts post data'
    
    def handle(self, *args:Any, **options:Any):

        # Deleting exixting data
        
            post.objects.all().delete()
            
            
            titles = [  
    "Post 1", 
    "Post 2", 
    "Post 3", 
    "Post 4", 
    "Post 5", 
    "Post 6", 
    "Post 7", 
    "Post 8", 
    "Post 9", 
    "Post 10", 
    "Post 11", 
    "Post 12", 
]

            content =[
    "Content of Post 1",
    "Content of Post 2",
    "Content of Post 3",
    "Content of Post 4",
    "Content of Post 5",
    "Content of Post 6",
    "Content of Post 7",
    "Content of Post 8",
    "Content of Post 9",
    "Content of Post 10",
    "Content of Post 11",
    "Content of Post 12",
]

            img_urls =[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
]

            categories = Category.objects.all()

            for title, content, img_url in zip(titles, content, img_urls):
                category = random.choice(categories)
                post.objects.create(title=title, content=content, img_url=img_url, category = category)
    
            self.stdout.write(self.style.SUCCESS("Completrd inserting Data!"))
    
    
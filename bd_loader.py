from renderer.models import Blog

file_name = "" # some file

f=open(file_name,'r')


s=input() # some data

while s:
    b=Blog(name='first_entity',tagline='second_entity')
    b.save()
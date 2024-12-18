from django.shortcuts import render
from .models import About

# Create your views here.
    
"""
Renders the About Page
"""
def about_me(request):

   """
   selects a single about entry (if multiple entries have been
   added in the admin portal).
   The objects.all selects all the information within that entry
   so the title, body etc.
   orders it in reverse and then selects the first entry
   stores it in a variable called about
   """
   about = About.objects.all().order_by('-updated_on').first()
   
   return render(
       request,
       "about/about.html",
       {"about": about},
    )

"""
returns when requested (from the brackets above) the about 
template (the location of the about template)
followed by setting the context
"""
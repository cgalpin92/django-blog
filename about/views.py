from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
    
"""
Renders the About Page
"""
def about_me(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data==request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            message.add_message(request, messages.SUCCESS, 
            "Collaboration request received! I endeavor to respond within 2 working days.")
    """
    selects a single about entry (if multiple entries have been
    added in the admin portal).
    The objects.all selects all the information within that entry
    so the title, body etc.
    orders it in reverse and then selects the first entry
    stores it in a variable called about
    """

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
   
    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form
    },
    )

"""
returns when requested (from the brackets above) the about 
template (the location of the about template)
followed by setting the context
"""
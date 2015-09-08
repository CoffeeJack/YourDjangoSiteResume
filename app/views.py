"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Coffee Cat',
    'bio' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id interdum tellus. Morbi ac lacus pellentesque, iaculis arcu quis, condimentum ipsum. Proin a ex ipsum. Aliquam accumsan cursus est, eu vulputate risus iaculis at. Quisque mollis rutrum sagittis. Nam cursus imperdiet lobortis. Sed dapibus cursus elit, ut gravida dui scelerisque non. Nulla eu velit mauris.',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'DorkMix', # No @ symbol, just the handle.
    'github_username' : "CoffeeJack", 
    'headshot_url' : 'https://c1.staticflickr.com/9/8119/8639028259_65436dfb4f_b.jpg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )
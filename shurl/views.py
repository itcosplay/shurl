from django.shortcuts import render

from shurl.forms import LinkForm

def render_main_page(request):
    form = LinkForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
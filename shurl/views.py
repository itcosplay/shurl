from django.shortcuts import render
from django.shortcuts import redirect

from shurl.forms import LinkForm

def render_main_page(request):
    error = ''

    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('main')
            
        else:
            error = 'Form was incorrect!!!'

    form = LinkForm()

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'index.html', context)
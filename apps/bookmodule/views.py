from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, 'bookmodule/index.html', {"name": name})

def index2(request, val1):
    try:
        val1 = int(val1)  # Try to convert val1 to an integer
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("error, expected val1 to be integer")


def viewbook(request, bookId):
    # Define two example books
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    # Initialize targetBook as None
    targetBook = None
    
    # Check if the bookId matches one of the books
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2
    
    # Prepare context with the found book
    context = {'book': targetBook}
    
    # Render the bookmodule/show.html template with the context
    return render(request, 'bookmodule/show.html', context)

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)


def link_page(request):
    return render(request, 'bookmodule/links.html')


def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')
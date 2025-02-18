from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    genre_counts = {
        "children": Genre.objects.filter(name__icontains='children').count(),
        "fiction": Genre.objects.filter(name__icontains='fiction').count(),
        "science": Genre.objects.filter(name__icontains='science').count(),
    }

    # chained filters are "AND"ed together, resulting in the "intersection" or "conjunction", but I wanted
    # the "OR"ed result (or "disjunction" or "union") so I used the Q object (note the added import above)
    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#complex-lookups-with-q-objects
    scien_books_count = Book.objects.filter(Q(title__icontains='scien') | Q(summary__icontains='scien')).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre_counts': genre_counts,
        'scien_books_count': scien_books_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

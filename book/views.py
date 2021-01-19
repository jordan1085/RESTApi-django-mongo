from django.shortcuts import render, redirect

from django.core.paginator import Paginator

from .models import Book
# Create your views here.

# Obtener todos los libros
def index(request):
    books = Book.objects.all()
    books_page = Paginator(books,2) #agregando paginacion 

    print(books_page)
    return render(request, 'book/index.html',{'books':books_page}) #reques, pagina, template


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    redirect('book:index')
from django.shortcuts import render, redirect
from .forms import BookForm


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


from django.shortcuts import render
from .models import book

def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})


from django.shortcuts import get_object_or_404, redirect
from .models import book

def delete_book(request, pk):
    book = get_object_or_404(book, pk=pk)
    book.delete()
    return redirect('book_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import book
from .forms import BookForm

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


from django.shortcuts import render
from .models import book

def search_books(request):
    book_type = book.book_type
    ages = book.age

    books = book.objects.all()

    keyword = request.GET.get('keyword')
    age = request.GET.get('age')
    book_types_selected = request.GET.getlist('book_type')

    if keyword:
        books = books.filter(name__icontains=keyword)

    if age:
        books = books.filter(age=age)

    if book_types_selected:
        books = books.filter(book_type__in=book_types_selected)

    context = {
        'books': books,
        'ages': ages,
        'book_type': book_type,
        'keyword': keyword,
        'age_selected': age,
        'book_types_selected': book_types_selected,
    }

    return render(request, 'search_books.html', context)


from django.shortcuts import render
from .models import book

def index(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})
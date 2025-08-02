from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm

@permission_required('core.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

@permission_required('core.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'core/book_form.html', {'form': form})

@permission_required('core.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'core/book_form.html', {'form': form})

@permission_required('core.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'core/book_confirm_delete.html', {'book': book})

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            return render(request, 'core/example_success.html', {'data': form.cleaned_data})
    else:
        form = ExampleForm()
    return render(request, 'core/example_form.html', {'form': form})
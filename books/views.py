from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from books.utils import get_book, search_books
from books.forms import FavouriteBookForm
from books.models import FavouriteBook
# Create your views here.




def search_page(request):
      books:list = []
      message:str = ""
      # if user search something - get this books, using search_books function
      if searchQuery := request.GET.get("q"):
            books:list[dict] = search_books( searchQuery )
      
            # if we don`t get books we display message
            if len(books) == 0:
                  message = "No books was found."
      
      return render(request, "books/index.html", {
            "books": books,
            "message":message
      })


@login_required(login_url="../users/login")
def favourite_page(request):
      message:str = ""
      queryset = request.user.books.all()
      if len(queryset) == 0:
            message = "You don`t have favourite books yet"
      return render(request, "books/favourite.html", {"books":queryset, "message":message})



@login_required(login_url="../users/login")
def add_to_favourite_books(request):
      if request.method == "POST":
            data = dict(request.POST)
            data['user'] = request.user
            form = FavouriteBookForm(data)
            if form.is_valid():
                  form.save()
            else:
                  print(form.errors)
            
            return redirect(reverse("books:favourite"))
      
      return redirect(reverse("books:search"))

def detail_page(request, id):
      book = get_book(id)
      if image_url := request.GET.get("img"):
            book['image'] = image_url
      return render(request, "books/detail.html", {
            "book":book
      })


@login_required(login_url="../users/login")
def delete_favourite(request, id):
      try:
            FavouriteBook.objects.get(user = request.user, key = id).delete()
      except FavouriteBook.DoesNotExist:
            pass
      
      return redirect("books:favourite")
            
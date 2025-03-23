from ninja import NinjaAPI, Schema, ModelSchema
from typing import List
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from catalog.models import Author, Genre, Language, Book, BookInstance
from ninja.security import django_auth

api = NinjaAPI()

# Schemas

class AuthorSchema(ModelSchema):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']

class GenreSchema(ModelSchema):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class LanguageSchema(ModelSchema):
    class Meta:
        model = Language
        fields = ['id', 'name']

class BookSchema(ModelSchema):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'isbn', 'genre', 'language']

class BookInstanceSchema(ModelSchema):
    class Meta:
        model = BookInstance
        fields = ['id', 'book', 'imprint', 'due_back', 'status']

# CRUD Endpoints: Author
@api.get("/author/", response=List[AuthorSchema])
def list_authors(request):
    return Author.objects.all()

@api.get("/author/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    return get_object_or_404(Author, pk=author_id)

@api.post("/author/", auth=django_auth, response=AuthorSchema)
def create_author(request, data: AuthorSchema):
    return Author.objects.create(**data.dict())

@api.put("/author/{author_id}", auth=django_auth, response=AuthorSchema)
def update_author(request, author_id: int, data: AuthorSchema):
    author = get_object_or_404(Author, pk=author_id)
    for attr, value in data.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/author/{author_id}", auth=django_auth)
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return {"success": True}

# CRUD: Genre
@api.get("/genre/", response=List[GenreSchema])
def list_genres(request):
    return Genre.objects.all()

@api.get("/genre/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    return get_object_or_404(Genre, pk=genre_id)

@api.post("/genre/", auth=django_auth, response=GenreSchema)
def create_genre(request, data: GenreSchema):
    return Genre.objects.create(**data.dict())

@api.put("/genre/{genre_id}", auth=django_auth, response=GenreSchema)
def update_genre(request, genre_id: int, data: GenreSchema):
    genre = get_object_or_404(Genre, pk=genre_id)
    genre.name = data.name
    genre.save()
    return genre

@api.delete("/genre/{genre_id}", auth=django_auth)
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, pk=genre_id)
    genre.delete()
    return {"success": True}

# CRUD: Language
@api.get("/language/", response=List[LanguageSchema])
def list_languages(request):
    return Language.objects.all()

@api.get("/language/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    return get_object_or_404(Language, pk=language_id)

@api.post("/language/", auth=django_auth, response=LanguageSchema)
def create_language(request, data: LanguageSchema):
    return Language.objects.create(**data.dict())

@api.put("/language/{language_id}", auth=django_auth, response=LanguageSchema)
def update_language(request, language_id: int, data: LanguageSchema):
    language = get_object_or_404(Language, pk=language_id)
    language.name = data.name
    language.save()
    return language

@api.delete("/language/{language_id}", auth=django_auth)
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, pk=language_id)
    language.delete()
    return {"success": True}

# CRUD: Book
@api.get("/book/", response=List[BookSchema])
def list_books(request):
    return Book.objects.all()

@api.get("/book/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    return get_object_or_404(Book, pk=book_id)

@api.post("/book/", auth=django_auth, response=BookSchema)
def create_book(request, data: BookSchema):
    return Book.objects.create(**data.dict())

@api.put("/book/{book_id}", auth=django_auth, response=BookSchema)
def update_book(request, book_id: int, data: BookSchema):
    book = get_object_or_404(Book, pk=book_id)
    for attr, value in data.dict().items():
        setattr(book, attr, value)
    book.save()
    return book

@api.delete("/book/{book_id}", auth=django_auth)
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return {"success": True}

# CRUD: BookInstance
@api.get("/bookinstance/", response=List[BookInstanceSchema])
def list_bookinstances(request):
    return BookInstance.objects.all()

@api.get("/bookinstance/{instance_id}", response=BookInstanceSchema)
def get_bookinstance(request, instance_id: int):
    return get_object_or_404(BookInstance, pk=instance_id)

@api.post("/bookinstance/", auth=django_auth, response=BookInstanceSchema)
def create_bookinstance(request, data: BookInstanceSchema):
    return BookInstance.objects.create(**data.dict())

@api.put("/bookinstance/{instance_id}", auth=django_auth, response=BookInstanceSchema)
def update_bookinstance(request, instance_id: int, data: BookInstanceSchema):
    instance = get_object_or_404(BookInstance, pk=instance_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance

@api.delete("/bookinstance/{instance_id}", auth=django_auth)
def delete_bookinstance(request, instance_id: int):
    instance = get_object_or_404(BookInstance, pk=instance_id)
    instance.delete()
    return {"success": True}

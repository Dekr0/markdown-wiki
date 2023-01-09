from django.urls import path

from . import views


urlpatterns = [
    path("",
         views.index,
         name="index"),

    path("create_new_entry",
         views.show_entry_editor,
         name="create_new_entry"),

    path("edit_entry/<str:entry_title>",
         views.show_entry_editor,
         name="edit_entry",
         kwargs={"new": False}),

    path("search?<str:entry_title>",
         views.search,
         name="search"),

    path("search",
         views.search,
         name="search"),

    path("wiki/<str:entry_title>",
         views.show_entry_page,
         name="show_entry_page"),
]

from django.shortcuts import render
from django.views.decorators.http import require_GET

from . import util
from .form.entry_editor import EntryEditor


def index(request):
    """
    Render the index page of the encyclopedia
    :param request:
    :return:
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show_entry_editor(request, new=True, entry_title=None):
    """
    Render the page for creating a new entry / editing an existent entry,
    and handle the submission of the form

    :param entry_title:
    :param new:
    :param request:
    :return:
    """

    return render(request, "encyclopedia/entry_editor.html", {
        "title": "Create New Entry" if new else f"Editing {entry_title}",
        "form": EntryEditor()
    })


@require_GET
def search(request):
    query = request.GET.get('query', '')

    entries = util.list_entries()

    if query in entries:
        return show_entry_page(request, query)

    results = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/list_entry.html", {
        "entries": results,
    })


def show_entry_page(request, entry_title):
    markdown = util.get_entry(entry_title)

    if markdown is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "Page not found"
        })

    base_url = request.build_absolute_uri().replace(request.path, '') + '/encyclopedia'

    html = util.resolve_all_link(util.convert_markdown_to_html(markdown), base_url)

    return render(request, "encyclopedia/entry_page.html", {
        "entry_title": entry_title,
        "html": html,
    })

import re
import bs4

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from markdown2 import Markdown


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def resolve_all_link(html, base_url):
    """
    Resolve all links in html
    """
    soup = bs4.BeautifulSoup(html, "html.parser")

    for link in soup.find_all('a'):
        if link['href'].startswith('/wiki/'):
            link['href'] = base_url + link['href']

    return str(soup)


def convert_markdown_to_html(markdown):
    """
    Converts Markdown to HTML.
    """
    return Markdown().convert(markdown)

from django import template

register = template.Library()

def is_preview():
    """
    Returns True if the current object is not in, or different to, the
    respective object in the database and False if otherwise.
    """
    pass
from django.contrib.auth import get_user_model
user_model = get_user_model()
from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter
def author_details(username):
    if not isinstance(username, user_model):
        # return empty string as safe default
        return ""
    """ Returns Authr' details (first and/or last name)
        As clickable href link if email is present """
    if username.email:
        prefix = format_html('<a href="mailto:{}">', username.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""
    if username.first_name and username.last_name:
        name = f"{username.first_name} {username.last_name}"
    elif username.first_name:
        name = f"{username.first_name}"
    elif username.last_name:
        name = f"{username.last_name}"
    else:
        name = f"{username}"
    return format_html('{}{}{}', prefix, name, suffix)

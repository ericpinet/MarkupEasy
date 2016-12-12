from django import template

register = template.Library()


@register.filter
def human_readable_size(size):
    if size <= (1024 * 1024):
        return "%s kb" % (size / 1024)
    else:
        return "%s mo" % (size / 1024 / 1024)

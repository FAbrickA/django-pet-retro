from django.template import Library

register = Library()


@register.inclusion_tag('_messages.html', takes_context=True)
def display_messages(context):
    return context

from django import template

register = template.Library()

@register.filter
def has_attribute(value, arg):
  
    return hasattr(value, arg)
    
@register.simple_tag(takes_context=True)
def active(context,t,  pattern):
    import re
    path = context.request.path
    if re.search(pattern, path):
        return 'is-active'
    return ''
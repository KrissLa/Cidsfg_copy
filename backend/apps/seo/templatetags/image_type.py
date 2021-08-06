from django import template

register = template.Library()


@register.filter(name='image_type')
def image_type(value):
    """ Считаем количество только активных """
    if not value:
        return 'JPEG'
    img_type = value.split('.')[-1]
    if img_type == 'png':
        return 'PNG'
    elif img_type == 'webp':
        return 'WebP'
    else:
        return 'JPEG'

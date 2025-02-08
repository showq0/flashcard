# from django import template
# register = template.Library() #create instance of library 

# @register.simple_tag
# def greet(name):
#     return f"Hello, {name}!"

from django import template
from cards.models import BOXES, Card

register = template.Library() #create instance of library 


@register.inclusion_tag("cards/box_link.html")# as a decorator. This tells Django that boxes_as_links is an inclusion tag.
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()# may be boxes length may be less 
        boxes.append({ 
            "number":  box_num, 
            "card_count": card_count
            })
        
    return {"boxes": boxes}
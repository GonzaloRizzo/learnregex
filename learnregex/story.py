from story.story import BaseStory

from . import character_classes, introduction, special_characters
from .data import _


class Story(BaseStory):

    name = 'learnregex'
    title = _('Learn regular expressions with Python')
    adventures = [
        introduction,
        special_characters,
        character_classes,
    ]

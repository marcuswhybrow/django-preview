
def previewable(cls):
    """
    Adds helper methods to a previewable class allowing the creation
    and previewing of an unsaved state
    """
    class decorator(cls):
        def create_preview(self):
            print 'Creating preview'
        
        def get_preview_url(self):
            print 'Getting URL'
    
    decorator.__name__ = cls.__name__
    return decorator
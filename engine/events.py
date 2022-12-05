class Event:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description
        
    def event(self, function):
        self.function = function

class Events:
    def __init__(self):
        self.events = []
    
    def append(self, event: Event):
        self.events.append(event)
   
    def checkEvent(self):
        if not self.events:
            event = Event(None, None)
        else:
            event = self.events.pop()
            event.function(event.name, event.description)
        return event
           
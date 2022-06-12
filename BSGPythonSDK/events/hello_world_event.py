import BSGPythonSDK.events.base_event as base_event


class HelloWorldEvent(base_event.BaseEvent):
    def execute(self, *args, **kwargs):
        print("Hello, World!")

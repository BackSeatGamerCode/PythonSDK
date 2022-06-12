# PythonSDK
 The generic SDK for games written in Python

## Setup
This SDK requires [BackSeatGamer Reverse Proxy](https://github.com/BackSeatGamerCode/ReverseProxy) to be running in `TCP/IP Broadcast` Mode using `JSON` format. By default, port 29175 will be used.

This SDK was designed to be as generic as possible, for any game with modding in Python, however, more specific SDKs for various games may be released soon. When they are complete, they will be listed here. 
Feel free to fork the repository to create a more specific Python SDK.

## Usage
Due to the generic nature of this SDK, instructions on how to install mods, set up the working environment, and resources for more information can not be included.
All you need is the `BSGPythonSDK` package. Be sure to copy everything, and that the destination package is `BSGPythonSDK` so there are no compatibility issues. 
We will be adding this library to PIP in the near future to make installation easier.

### Setup
Once everything is set up, development can begin! To start, simply create a new class which extends `BSGPythonSDK`. It will require `get_event` to be implemented. 
You can optionally override `on_redemption_received` for more control:
```python
from BSGPythonSDK import *


class MyBSGClass(BSGPythonSDK):
    def get_event(self, redemption):
        return HelloWorldEvent()
```

or if you wish to use the `on_redemption_received` method:
```python
from BSGPythonSDK import *


class MyBSGClass(BSGPythonSDK):
    def get_event(self, redemption):
        return HelloWorldEvent()

    def on_redemption_received(self, redemption, *args, **kwargs):
        print(redemption.to_message())
```

`on_redemption_received` is called whenever a person redeems a reward. The default functionality is for nothing to happen. This event is generally used to announce the reward and who redeemed it. 
This method is called BEFORE the event is executed. The method also takes `*args` and `**kwargs`. This will be explained soon.
In the above example, the `to_message` method of the reward is called, which returns a string in the format `{guest} has redeemed the reward {name}`. This method is also executed in the main thread of the application.

The next method `get_event` is responsible for converting a redemption to an event. You could use a dictionary table to look up the reward if you wish, but there is nothing too fancy in the example code.
This section uses the Gang of Four's Command pattern. The method should return the object, and so the signature of the constructor can be whatever you want it to be. Feel free to call as many methods of the object as you wish.
All you need to do is return the object when it is ready. This method is called in the main thread of the application.

### Implementation
To run the mod functionality, simply instantiate your class which extends the `BSGPythonSDK` class. On each game loop/tick, simply call the `poll` method of the object. Easy. 
The `poll` method does not perform any networking or other laborious activities, so it is safe to call every game loop without performance taking a hit.

The `poll` method can take a variable number of arguments. These arguments are passed to all methods which have the parameters `*args` and `**kwargs` (`on_redemption_received` in your mod class which extends `BSGPythonSDK`, and `execute` in the custom `Event` class).

### Custom Events
To create a custom event, simply create a class which extends `BaseEvent`. This abstract class requires the implementation of the `execute` method, which takes `*args` and `**kwargs` as its only argument (see above for explanation).

Feel free to add a constructor and other supporting methods. You will be responsible for instantiating the object in the `get_event` method of your class which extends the `BSGPythonSDK` class.

The actual execution of the event should be implemented in the `execute` method.

The following is the source code of the built-in `HelloWorldEvent`, which prints `Hello, World!` to the console when executed:
```python
from BSGPythonSDK import *


class HelloWorldEvent(BaseEvent):
    def execute(self, *args, **kwargs):
        print("Hello, World!")

```

### The `Redemption` Object
The `Redemption` Object has three getters, `get_command()` which returns the command of the reward, `get_name()` returns the display name of the reward, and `get_guest()` returns the name of the guest who redeemed the reward.

The `Redemption` Object also has a method called `to_message` which returns a string in the format `{guest} has redeemed the reward {name}`. 

## Issues/Feedback
If you encounter any problems, or have suggestions for future updates, feel free to leave them over in the [Issue Tracker](https://github.com/BackSeatGamerCode/PythonSDK/issues). Alternatively, if you have questions or want to discuss something with your fellow Java modders, then check out our [Discussions](https://github.com/BackSeatGamerCode/PythonSDK/discussions). Thank you for using Java modding SDK, and good luck with your mod!

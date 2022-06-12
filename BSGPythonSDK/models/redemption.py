import typing
import json


class Redemption:
    def __init__(self, command: str, name: str, guest: str):
        self._command = command
        self._name = name
        self._guest = guest

    @classmethod
    def from_json(cls, data: typing.Union[str, dict]):
        if isinstance(data, str):
            data = json.loads(data)

        return cls(data["command"], data["name"], data["guest"])

    def get_command(self) -> str:
        return self._command

    def get_name(self) -> str:
        return self._name

    def get_reward_name(self) -> str:
        return self._name

    def get_guest(self) -> str:
        return self._guest

    def __repr__(self):
        return "<Redemption command='{}' name='{}' guest='{}'>".format(self._command, self._name, self._guest)

    def to_message(self) -> str:
        return '{} has redeemed the reward {}'.format(self._guest, self._name)

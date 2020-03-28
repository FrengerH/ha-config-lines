
"""Platform for sensor integration."""
from homeassistant.helpers.entity import Entity
from homeassistant.const import (
    STATE_UNKNOWN,
)

import math

MOTIVATION = "motivation"

MOTIVATIONS = [
    "Great work, your config is looking sweeeeeeeeet!!!!",
    "Almost there just a few more lines to clean.",
    "You're on the right path, your config is getting better every day.",
    "And again a bit cleaner config nice work.",
    "And less than 500 lines of config. Almost there.",
    "Your config is looking great today.",
    "Getting closer and closer to a nice and clean config.",
    "Slowly getting there keep up the good work.",
    "And again your config is a bit cleaner great work.",
    "Less than 1000 lines of config, just a few more to go.",
    "A clean config is a happy config.",
    "You're more than half way there, you can do it.",
    "Keep on going, your config is looking better and better.",
    "Oh look that sweet config getting cleaner every time.",
    "Looking better and better that config of yours.",
    "Config cleaning, config cleaning oh what do I love config cleaning.",
    "On your way to a perfect clean config.",
    "Your config is looking better by the day.",
    "And another 100 lines of config cleaned. Good job!!",
    "Keep up the good work, you're getting there.",
    "You can do it, only 2000 more lines of config to clean.",
    "And again cleaned up some config you're getting there.",
    "Slowly moving to a nice and clean config.",
    "That's a start keep up the good work.",
    "There is still a lot of config to split.",
]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([ConfigLines()])


class ConfigLines(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {
            MOTIVATION: STATE_UNKNOWN,
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Config lines'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def state_attributes(self):
        """Return state attributes."""
        return self._attributes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "lines"

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        with open("./config/configuration.yaml") as f:
            lines = len(f.readlines())
            self._attributes[MOTIVATION] = self.getMotivation(lines)
            self._state = lines

    def getMotivation(self, lines):
        motivation = math.ceil(lines / 100)
        if motivation > 25:
            motivation = 25
        return MOTIVATIONS[motivation -1]

import pyblish.api
import pype.api


class ValidateShots(pyblish.api.ContextPlugin):
    """Validate there is a "mov" next to the editorial file."""

    label = "Validate Shots"
    hosts = ["standalonepublisher"]
    order = pype.api.ValidateContentsOrder

    def process(self, context):
        shot_names = []
        duplicate_names = []
        for instance in context:
            name = instance.data["name"]
            if name in shot_names:
                duplicate_names.append(name)
            else:
                shot_names.append(name)

        msg = "There are duplicate shot names:\n{}".format(duplicate_names)
        assert not duplicate_names, msg

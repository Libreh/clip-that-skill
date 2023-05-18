from mycroft import MycroftSkill, intent_file_handler


class ClipThat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('that.clip.intent')
    def handle_that_clip(self, message):
        self.speak_dialog('that.clip')


def create_skill():
    return ClipThat()


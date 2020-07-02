from mycroft import MycroftSkill, intent_file_handler


class HaloProtocol(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('protocol.halo.intent')
    def handle_protocol_halo(self, message):
        self.speak_dialog('protocol.halo')


def create_skill():
    return HaloProtocol()


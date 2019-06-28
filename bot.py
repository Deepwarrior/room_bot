import telebot
from player import Player
from bot_utils import create_link

class Bot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.bot_init()

    def give_link(self, chat, player):
        pass

    def inform_admins(self, text):
        pass

    def register(self, message):
        try:
            self.inform_admins(create_link(message.from_user, "Игрок") + " зарегаться пытается.")
            self.bot.reply_to(message, "Заявка принята! Ожидайте.")
        except telebot.apihelper.ApiException:
            pass

    def kusb(self, chat, player):
        pass

    def parse_text(self, chat):
        pass

    def check_answer(self, message):
        pass

    def end_turn(self):
        pass

    def change_info(self):
        pass

    def bot_init(self):
        @self.bot.message_handler(commands=["reg"])
        def reg(message):
            player = Player(message.from_user.id)
            if player.registration():
                self.register(message)
            else:
                try:
                    self.bot.reply_to(message, "Регистрироваться дважды? Ну неее.")
                except telebot.apihelper.ApiException:
                    pass
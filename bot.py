import telebot
from player import Player
from bot_utils import create_link
import io

class Bot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.bot_init()

    def give_link(self, chat, player):
        try:
            # check is there way from current position?
            if chat.id in player.get_map():
                self.bot.send_message(player.id, chat.get_link())
        except telebot.apihelper.ApiException:
            pass

    def inform_admins(self, text):
        chat_id = io.get_chat_id("admin")
        try:
            self.bot.send_message(chat_id, text)
        except telebot.apihelper.ApiException:
            pass

    def register(self, message):
        try:
            self.inform_admins(create_link(message.from_user, "Игрок") + " зарегаться пытается.")
            self.bot.reply_to(message, "Заявка принята! Ожидайте.")
        except telebot.apihelper.ApiException:
            pass

    def kusb(self, chat, player):
        try:
            self.bot.kick_chat_member(chat.id, player.id, 0)
            self.bot.unban_chat_member(chat.id, player.id)
        except telebot.apihelper.ApiException:
            self.inform_admins("НЕ " + create_link(player.id, "КУСБНУЛОСЬ") + "\n" +
                               "ОТСЕДОВА: " + chat.get_link())

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
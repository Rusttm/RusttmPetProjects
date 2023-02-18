
""" третья версия -доработан калькулятор до полноценного вычисления функций
"""

import logging
import configparser
import os
import candygame
import tictacgame_v2
import expr_resolver_4bot
try:
    # get data from in file
    conf = configparser.ConfigParser()
    #conf.read('config.ini')
    conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    TOKEN = conf['TOKENS']['telegram']

except IndexError:
    print('Error, cant read .ini file')

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    filename='bot.log', filemode='a'
)
logger = logging.getLogger(__name__)

class JohnBotGB():
    def __init__(self):
        self.project = False
        self.current_gamer = dict() # 'user_id' : 'tictac', calc or false
        self.current_user_game = dict()
        self.delete_msg_id = 0
        self.current_user_id = '1'
        self.msg_update = ()
        self.msg_context = ()
        self.game_dict = dict({'nogame': {'function': self.start, 'help': 'Игра не выбрана', 'command': '/start'},
                               'tictaс': {'function': self.GameTicTac, 'help': 'Введите координату', 'command': '/tictac'},
                               'candy': {'function': self.GameCandy, 'help': 'Сколько конфет возьмете?', 'command': '/candy'},
                               'calc': {'function': self.GameCalcStart, 'help': 'Введите выражение', 'command': '/calc'}
                               })

        self.commands_dict = dict({'/start': '-перезапуск бота',
                                   '/help': '- помощь',
                                   '/tictac': '-игра в крестики-нолики',
                                   '/candy': '-игра в конфетки',
                                   '/calc': 'решение математического выражения'})
        self.tictac_start_keyboard = [[
                InlineKeyboardButton("\U0000274C", callback_data="tictac cross"), # крестик
                InlineKeyboardButton("\U00002B55", callback_data="tictac zero"), # нолик
            ]]
        self.tictac_field_keyboard = [[
            InlineKeyboardButton("\U00002796", callback_data="tictac a1"),  # тире
            InlineKeyboardButton("\U00002796", callback_data="tictac b1"),  # тире
            InlineKeyboardButton("\U00002796", callback_data="tictac c1"),  # тире
            ],
            [
                InlineKeyboardButton("\U00002796", callback_data="tictac a2"),  # тире
                InlineKeyboardButton("\U00002796", callback_data="tictac b2"),  # тире
                InlineKeyboardButton("\U00002796", callback_data="tictac c2"),  # тире
            ],
            [
                InlineKeyboardButton("\U00002796", callback_data="tictac a3"),  # тире
                InlineKeyboardButton("\U00002796", callback_data="tictac b3"),  # тире
                InlineKeyboardButton("\U00002796", callback_data="tictac c3"),  # тире
            ]]

        self.start_keyboard = [
            [
                InlineKeyboardButton("Start", callback_data="command /start"),
                InlineKeyboardButton("Help", callback_data="command /help"),
            ],
            [InlineKeyboardButton("КрестикиНолики", callback_data="command /tictac")],
            [InlineKeyboardButton("Конфетки", callback_data="command /candy")],
            [InlineKeyboardButton("Калькулятор", callback_data="command /calc")],
        ]
        self.NewBot()


    # работа с клавиатурой
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Sends a message with three inline buttons attached."""

        self.msg_update = update
        self.msg_context = context
        self.current_user_id = update.message.from_user.id
        keyboard = self.start_keyboard
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Меню:", reply_markup=reply_markup)


    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """обработчик нажатий всех кнопок - перенаправляет на соответствующий обработчик"""

        query = update.callback_query
        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        await query.answer()
        query_game, query_data = query.data.split()
        print(f"{query_game}, {query_data}")

        if query_game == 'command':
            if query_data == '/start':
                await self.start_button(query_data=query_data)
            elif query_data == '/tictac':
                await self.GameTicTac(query_data=query_data)
            elif query_data == '/candy':
                await self.GameCandy(self.msg_update, self.msg_context)
            elif query_data == '/calc':
                await self.GameCalcStart(self.msg_update, self.msg_context)
        elif query_game == 'tictac':
            await self.GameTicTac(query_data=query_data)

        else:
            await query.edit_message_text(text=f"Selected option: {query.data}")
        # await self.help_command( Update, ContextTypes.DEFAULT_TYPE)
        # self.application.add_handler(CommandHandler("start", self.start))
        # await query.edit_message_text(text=f"Selected option: {query.data}")
        # self.msg_update.message.text = query.edit_message_text(text=f"Selected option: {query.data}")

    async def start_button(self, query_data='/start') -> None:
        """обработчик нажатий кнопок на стартовом меню"""
        if query_data == '/start':
            await self.start(self.msg_update, self.msg_context)
        elif query_data == '/help':
            await self.help_command(self.msg_update, self.msg_context)
        elif query_data == '/tictac':
            await self.GameTicTac(query_data=query_data)
        elif query_data == '/candy':
            await self.GameCandy(self.msg_update, self.msg_context)
        elif query_data == '/calc':
            await self.GameCalcStart(self.msg_update, self.msg_context)
        else:
            await self.start(self.msg_update, self.msg_context)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""

        temp_msg = self.game_dict.get(self.current_gamer[update.message.from_user.id], self.game_dict['nogame'])['help']
        await update.message.delete()
        await update.message.reply_text(f"{temp_msg}")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        logging.info(msg=f"message from: {update.message.chat.first_name}, text: {update.message.text} ")
        self.msg_update = update
        self.msg_context = context
        self.current_user_id = update.message.from_user.id
        current_user_game = self.current_gamer[update.message.from_user.id]
        if current_user_game == 'nogame':
            await update.message.reply_text(f"Hi {update.message.from_user.first_name}({update.message.from_user.id}) "
                                            f"and you wrote {update.message.text}")
        elif current_user_game == 'tictac':
            await self.GameTicTac(command=update.message.text)

        # elif current_user_game == 'calc':
        #     await self.GameCalc()


        else:
            print(update.message.text)
            result = self.current_user_game[update.message.from_user.id].UserTurn(update.message.text)
            await update.message.reply_text(result[1])
            if result[0] == 'end':
                # высылаем картинку если калькулятор сработал
                if current_user_game == 'calc':
                    try:
                        chat_id = update.message['chat']['id']
                        # graph = self.current_user_game[update.message.from_user.id].draw_expression()
                        # await context.bot.send_photo(chat_id=chat_id, photo=graph)
                        await context.bot.send_photo(chat_id=chat_id,
                                                     photo=open(f'{update.message.from_user.id}.png', 'rb'),
                                                     filename=f'{update.message.from_user.id}.png')
                        await context.bot.send_photo(chat_id=chat_id,
                                                     photo=open(f'{update.message.from_user.id}_diff.png', 'rb'),
                                                     filename=f'{update.message.from_user.id}_diff.png')
                    except:
                        chat_id = update.message['chat']['id']
                        await context.bot.send_photo(chat_id=chat_id,
                                                     photo=open('acute.jpeg', 'rb'),
                                                     filename='acute.jpeg')
                else:
                    await update.message.reply_text("Игра закончена!")

                self.current_gamer[update.message.from_user.id] = 'nogame'
                await self.start(update, context)

    async def TicTacField(self, field_data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        accord = {0: "\U00002796", 1: "\U0000274C", -1: "\U00002B55"}
        # field = list(map(lambda x: list(map(lambda y: accord[y], x)), field_data))
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for ii in range(3):
                if field_data[i][ii] == 1:
                    field[i][ii] = "\U0000274C"
                elif field_data[i][ii] == -1:
                    field[i][ii] = "\U00002B55"
                else:
                    field[i][ii] = "\U00002796"

        self.tictac_field_keyboard = [[
            InlineKeyboardButton(field[0][0], callback_data="tictac a1"),
            InlineKeyboardButton(field[0][1], callback_data="tictac b1"),
            InlineKeyboardButton(field[0][2], callback_data="tictac c1"),
            ],
            [
                InlineKeyboardButton(field[1][0], callback_data="tictac a2"),
                InlineKeyboardButton(field[1][1], callback_data="tictac b2"),
                InlineKeyboardButton(field[1][2], callback_data="tictac c2"),
            ],
            [
                InlineKeyboardButton(field[2][0], callback_data="tictac a3"),
                InlineKeyboardButton(field[2][1], callback_data="tictac b3"),
                InlineKeyboardButton(field[2][2], callback_data="tictac c3"),
            ]]
        keyboard = self.tictac_field_keyboard
        reply_markup = InlineKeyboardMarkup(keyboard)
        await self.msg_update.message.reply_text("Поле:", reply_markup=reply_markup)
        self.application.add_handler(CallbackQueryHandler(self.button))

    async def GameTicTac(self, query_data='cross'):
        """start tictak game"""
        result = ['halt', 'Unknow command']

        if query_data == '/tictac':  # при первом запуске
        # if self.current_gamer[self.msg_update.message.from_user.id] != 'tictaс':
            # создаем экземпляр
            self.current_gamer[self.msg_update.message.from_user.id] = 'tictaс'
            self.current_user_game[self.msg_update.message.from_user.id] = tictacgame_v2.XOgame(
                user_name=self.msg_update.message.from_user.id)
            # рисуем выбор крестика-нолика
            keyboard = self.tictac_start_keyboard
            reply_markup = InlineKeyboardMarkup(keyboard)
            await self.msg_update.message.reply_text("Чем будете играть?:", reply_markup=reply_markup)
            self.application.add_handler(CallbackQueryHandler(self.button))

        elif query_data == 'cross':
            result = self.current_user_game[self.msg_update.message.from_user.id].UserTurn('x')

        elif query_data == 'zero':
            result = self.current_user_game[self.msg_update.message.from_user.id].UserTurn('o')

        elif query_data in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
            result = self.current_user_game[self.msg_update.message.from_user.id].UserTurn(query_data)


        else:
            await self.msg_update.message.reply_text("Не правильный шаг")
        if result[0] == 'continue':
            # await self.msg_update.message.reply_text(result[1])
            field = self.current_user_game[self.msg_update.message.from_user.id].PrintField()
            await self.TicTacField(field)
        if result[0] == 'end':
            self.current_gamer[self.msg_update.message.from_user.id] = 'nogame'
            print(result[1])
            await self.TicTacField(result[1])
            end_msg = self.current_user_game[self.msg_update.message.from_user.id].winner
            await self.msg_update.message.reply_text(end_msg)
            await self.start(self.msg_update, self.msg_context)




        # # рисуем поле
        # keyboard = self.tictac_field_keyboard
        # reply_markup = InlineKeyboardMarkup(keyboard)
        # await update.message.reply_text("Поле:", reply_markup=reply_markup)
        # field = self.current_user_game[update.message.from_user.id].PrintField()
        # await update.message.reply_text(field)
        # await update.message.reply_text("Чем Вы будете играть? 'O' или 'X'")

    async def GameCandy(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictak game"""
        self.current_gamer[update.message.from_user.id] = 'candy'
        self.current_user_game[update.message.from_user.id] = candygame.CandyGame(user_name=update.message.from_user.id)
        start_msg = self.current_user_game[update.message.from_user.id].StartMessage()
        await update.message.reply_text(start_msg[1])
        await update.message.reply_text("Сколько \U0001F36C возьмете?")

    async def GameCalcStart(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start gamecalc game"""
        self.current_gamer[update.message.from_user.id] = 'calc'
        self.current_user_game[update.message.from_user.id] = expr_resolver_4bot.ExpressionResolver(user_name=update.message.from_user.id)
        await update.message.reply_text("Введите выражение для вычисления")

    # async def GameCalc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    #     """ expression resolver """
    #     self.current_gamer[update.message.from_user.id] = 'calc'
    #     self.current_user_game[update.message.from_user.id] = expr_resolver_bot.ExpressionResolver(user_name=update.message.from_user.id,
    #                                                                                                expression_str=update.message.text)
    #     await update.message.reply_text("Введите выражение для вычисления")





    def NewBot(self) -> None:
        """Start the bot."""

        # Create the Application and pass it your bot's token.
        self.application = Application.builder().token(TOKEN).build()

        # on different commands - answer in Telegram
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("tictac", self.GameTicTac))
        self.application.add_handler(CommandHandler("calc", self.GameCalcStart))
        self.application.add_handler(CommandHandler("candy", self.GameCandy))
        self.application.add_handler(CommandHandler("stop", self.start))

        self.application.add_handler(CallbackQueryHandler(self.button))
        # on non command i.e message - echo the message on Telegram
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        # Run the bot until the user presses Ctrl-C
        self.application.run_polling()




if __name__ == "__main__":
    bot_run = JohnBotGB()
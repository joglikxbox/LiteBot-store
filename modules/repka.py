from core.utils import utils
import traceback

class Main:
	
	version="1.0.0"
	info="""
	Исправление русских слов написанных англ раскладкой.
	Использовать ответом на сообщение.
	"""
	group="Work"
	
	async def init(app, m):
		text=m.reply_to_message.text

		layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                           "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
		t_out = text.translate(layout)

		await m.edit(t_out)

from deep_translator import GoogleTranslator
'''
to_translate = 'Я тупой'
translated = GoogleTranslator(source='auto', target='en').translate(to_translate)

print(translated)
'''

class Main:
    version = "0.2.0"
    info = "Переводчик"
    group = "Search"

    async def init(app, m):
    	input_t=m.text[7:]
    	atribut=input_t.split(' ')[0]

    	if len(atribut) == 2:
    		to_translate=input_t.replace(atribut, '')
    		atrib_out=atribut
    	else:
        	atrib_out='ru'
        	if m.reply_to_message:
        		to_translate = m.reply_to_message.text
        	else:
        		to_translate = input_t

    	await m.edit(f'**Translater:**```{to_translate}```**перевод на ** {atrib_out} \n'+GoogleTranslator(source='auto', target=atrib_out).translate(to_translate))
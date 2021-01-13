
import wikipedia as wiki

class Main:
    version = "0.2.0"
    info = "Переводчик"
    group = "Search"

    async def init(app, m):

        input_t=m.text[6:]
        atribut=input_t.split(' ')[0]
        
        if atribut.isdigit() == True:
            search=input_t.replace(atribut, '')
            atrib_out=atribut
        else:
            search=input_t
            atrib_out=2

        wiki.set_lang("ru")
        try:
            output=wiki.summary(search, sentences=atrib_out)
        except:
            output="Не найдено"

        await m.edit(f"**Wiki {search} \n**"+output)
from pyowm.owm import OWM
from core.utils import utils
from pyowm.utils.config import get_default_config

class Main:
	
	version="1.0.0"
	info="Модуль для погоды"
	group="Search"
	data=["token"]

	async def init(app, m):

		try: token=utils.db.select("weather", "token")[0]
		except: token=False

		if token:

			loc=m.text[9:]

			config_dict = get_default_config()
			config_dict['language'] = 'ru'
			owm = OWM(token, config_dict)
			mgr = owm.weather_manager()
			try:
				weather = mgr.weather_at_place(loc).weather
				temp = round(weather.temperature('celsius')['temp'])
				status = weather.detailed_status
				wind = weather.wind()['speed']
				humidity = weather.humidity
			except: await m.edit(f'**Погода в **{loc.capitalize()}:\n**Не найденa.**')

			if ',' in loc:
				loc = loc.split(',')[0]

			await m.edit(f'**Погода в **{loc.capitalize()}:\n**Cтатус: **{status.capitalize()}.\n**Cкорость ветра: **{wind} м/сек\n**Влажность: **{humidity}%\n**Температура: **{temp}°')

		else: await m.edit("Для работы требуется токен, получить его можно тут(https://openweathermap.org/), настроить его можно в веб панели бота.")

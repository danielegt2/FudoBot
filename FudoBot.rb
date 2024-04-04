#
#	Fudo Telegram Bot
#	Author: danielegt2
#

require 'telegram/bot'

token = ''

Telegram::Bot::Client.run(token, logger: Logger.new($stdout)) do |bot|
	bot.listen do |message|
		case message.text
		when '/start'
			bot.api.send_message(chat_id: message.chat.id, text: "A regazzì, e mo vo buco sto pallone")
		when '/milan'
			bot.api.send_photo(chat_id: message.chat.id, photo: Faraday::UploadIO.new('/immagini/silva1.jpg', 'image/jpeg'))
		when '/pogba'
			bot.api.send_message(chat_id: message.chat.id, text: "30!")
		else
			bot.api.send_message(chat_id: message.chat.id, text: "Cos'hai detto?!")
		end
	rescue Telegram::Bot::Exceptions::ResponseError => e
		retry
	end
end

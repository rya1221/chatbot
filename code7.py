import telebot
import requests
import json

# Create a new bot with your API token
bot = telebot.TeleBot('6240234914:AAEcwOuj0RtLHI8ODLgFf8oyibCyz_XWCjA')

# Define a function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'hello' or message.text.lower() == 'hi':
        # Call the GPT-3 API to generate a greeting message in Hindi
        response = requests.post(
            'https://api.openai.com/v1/engines/davinci-codex/completions',
            headers={'Authorization': 'Bearer YOUR_API_KEY_HERE'},
            json={
                'prompt': 'नमस्ते! क्या मैं आपकी मदद कर सकता हूँ?',
                'temperature': 0.5,
                'max_tokens': 50,
                'top_p': 1,
                'frequency_penalty': 0,
                'presence_penalty': 0
            }
        )
        # Parse the response and send the generated message to the user
        output = json.loads(response.text)['choices'][0]['text']
        bot.reply_to(message, output)
    else:
        bot.reply_to(message, 'मुझे यह समझ में नहीं आया। कृपया फिर से कोशिश करें।')

# Start the bot
bot.polling()

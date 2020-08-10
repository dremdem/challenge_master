# Tech spec for a Telegram Bot interfacing

## Documentation

[Telegram API](https://core.telegram.org/bots/api)


## Description

First of all I planned to use [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
It's ok, but the situation is: We need separate process/thread for this.
This thread will don't know anything about our main Django applications.
So we need find a way how to interact between two peaces of code.

Then I found another solution. Speak with TeleBot [by WebHook](https://medium.com/@voronov007/part-2-django-webhook-for-the-telegram-bot-a5bc7e179c75):

It's more convenient way, but we have to process raw data to/from 
TeleServer without any additional libraries.

## Diagram 

## Steps

### Research

* Find out what info we will get when user join to channel 

We need to make authorization by token.
I received a token when create my bot by BotFather.
Let's hide it to a env variable.
For reading from .env file will use [python-dotenv](https://pypi.org/project/python-dotenv/)

For setting webhook we have to send [setWebhook message](https://core.telegram.org/bots/api#setwebhook) to TeleServer.

I'm going to use it for production, I should provide a reusable solution, so let's make it as [a django command](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/)
In order it we have to define our first application: telegram. 

One more thing relating to webhook: I have to have a domain name! 
Huh... Seems like I should rent a VPS before even researching :) 

Fortunately I have one, so I can use it for this project. 

Wow! I have to use **certificates**!

Here in the [guide](https://core.telegram.org/bots/webhooks)
[How to](https://core.telegram.org/bots/self-signed) generate it.

Ouch.. Let's do it. 

Well done.

Put my ip-address to a env var: MY_DOMAIN_NAME

As teleapi suggests, let's make a route for a web hook like: 
/tg/<settings.BOT_TOKEN>/

WHOAAAAAA!!!
Holy crap...

https://core.telegram.org/bots/webhooks
>Setting a webhook needs a URL for us to post to. For that you'll need a server with a domain name. 
>If you don't have one, you'll need to obtain one first.  

Shoot me please.
One day of tests and all that for nothing.

Ok, I have to gather my thoughts.

1. I have to redirect one of my domain names to my VPS.
2. Make cert with certbot as many of developers done.
3. Profit!! 





* If we can get some unique chat_id associated with user, we can identify user next time
* What if a user join to channel and then leave it and then join it again. Will it be the same chat_id ? 

### Application

* Do we need different app for the models and for a Telebot interactions ? 







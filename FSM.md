# FSM

## Description

We will process commands from an user.
Every user will have a unique chat_id
We have to remember on what step we are right now.

For example the user just joined to chat-bot and hit /start command.
After that a bot asks the user to add an personal info.

* nick
* sex
* age 

How we can do it? 

We have to store a command and a state inside of this command.

We can use Django-FSM for this.

But there an issue. All logic will be placed in the models file, namely in a particular model.
This is antipattern IMHO.  I have to decouple a business-logic and a model. 



## DOCS

https://tproger.ru/translations/finite-state-machines-theory-and-implementation/
https://habr.com/ru/post/160105/
[Django FSM github](https://github.com/viewflow/django-fsm)
[Django-FSM tutorial in russain](https://webdevblog.ru/upravlenie-konechnym-avtomatom-s-ispolzovaniem-django-fsm/)
[transitions](https://github.com/pytransitions/transitions)
https://github.com/pytransitions/transitions/blob/master/examples/Frequently%20asked%20questions.ipynb
[Business Process implementation - not a FSM!] (https://github.com/viewflow/viewflow)

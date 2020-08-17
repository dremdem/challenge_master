# MVP

## Description 

So originally I was going to start with database design.
When I open lucidchart I realized that I don't know what my 
application should do exactly. 

Seems like I have to start with simple user cases, 
like workflow for my application.

Let's start with list of business-processes.

## Database

This is MVP, isn't it? The fancy approach... Dash it! Let's leave SQLLite by default.

## Models

### Profile

To extend users info I'm going to use a [*Profile* approach](https://tproger.ru/translations/extending-django-user-model/#var2).

I shave to add :
* sex
* age 
fields to a standard users model.

## Django Applications

### Telegram 

Will server all API for telegram bot interactions

## Flowcharts

### Business processes 

#### User registration

[BP flowchart](https://app.lucidchart.com/documents/view/ad08bb93-20a2-4966-ba10-1773f859e266)

This MVP will be used with telegram-bot. 
So when we would like to register, we have to specify:
* username
* email, optional
* age, optional
* sex, optional

#### Make challenge

Challenge options: 

* Name
* Description
* Deadline
* Steps frequency
  * Daily 
  * Weekly 
  * Monthly 
* Set notification type
  * by bot
  * by email
  * none
* Time of notification
* Amount of time for every step completion

#### Pause challenge

The pausing of a challenge is a painful process, but sometime it should be.

Options: 

* description
* auto continue datetime, optional

#### Cancel challenge

When a user is trying to cancel a challenge, we should to talk her/him out of it.
If user still contends, the app asks to fill next fields: 

* the reason
* do you plan to restart it sometimes later
  * notification, yes/no, datetime
* a suggestion to your followers

#### Get a notification

Some worker should be started by default and when notification 
datetime comes it should be send a notification.

We have two types of notifications: 

* For starting a step 
* when step is should be done

In the last case the app asks an user to mark this step done or not.

#### Mark step done

Anytime an user can mark a current (last notified) step as done/cancelled 
The user can add optional comment on it.

#### Track the implementation

Commands for tracking: 

* list my challenges
* get a challenge detailed info

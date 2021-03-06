========
Twitcher
========

Twitcher is a little read-only twitter client made for messing around with **AngularJS + Django + Sass + Twitter API**.

You can see how to consume an API with ngResource.
These might not be the best practices, so if you have anything in mind don't hesitate to create a pull request.

## Cloning

    git clone git@github.com:bit2pixel/twitcher.git

## Installing

Run the install script and follow the instructions. This script provides you with step-by-step instructions for getting API access on Twitter. It will create your config.ini file for you with your credentials.

    cd twitcher
    ./install.sh
    
    Enter your API key -> ******
    Enter your API secret -> ******
    Enter your PIN CODE -> ******

    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes

Don't forget your password. It will be required to play with Twitcher

## Running

    ./run.sh

## Playing

- Open your latest Google Chrome and go to http://localhost:8000

- At first run enter your admin username and password you've created while installing.

- When you login, type a twitter username. Thats all!

## Screenshot

![twitcher](https://raw.githubusercontent.com/bit2pixel/twitcher/master/screenshot.jpg)

## License

The MIT License (MIT)

Copyright (c) 2014 Renan Cakirerk (bit2pixel)

**Massachusetts Institute of Technology license (MIT):** You are allowed to use, modify and distribute copies of the software as long as you allow the same rights to the person to whom you distribute the software

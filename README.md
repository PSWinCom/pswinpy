PSWinCom Python Package
=======================

A Python interface to the [PSWinCom SMS Gateway](http://pswin.com/english/products/gateway).

Installation
------------

The pswinpy package is distributed through PyPI as both egg, Windows installer and source. [Download here](http://pypi.python.org/pypi/pswinpy/).

Basic Usage
-----------
To use this package, you will need sign up for a Gateway account with PSWinCom. Demo account are available.

This piece of code demonstrates how to send a simple SMS message:

    from pswinpy import API
    api = API("myUsername", "myPassword")
    api.sendSms(4712345678, "Strange women lying in ponds distributing swords is no basis for a system of government!")

Properties
----------
Receiver and message text are the two mandatory properties when sending a message. You may specify additional properties by using named arguments.

For instance this is how you would specify a sender:

    api.sendSms(4712345678, "It's just a flesh wound.", sender="BlackKnight")

Properties currently supported are:

* sender
* TTL - time to live in minutes
* tariff - the amount (in local currency as cents/"&oslash;rer") to charge the receiver
* serviceCode - service code for sending GAS messages. Requires that tariff is set. See [wiki](http://wiki.pswin.com/CPA-Goods-and-Services.ashx) for details.
* deliveryTime - a datetime object specifying when to send the message

Specifying Host
---------------
*Details in flux at the moment*

Modes
-----
For testing purposes the API provides a couple of modes you can set globally to control how the library works.

    Mode.test = True

.. will make you use the API without actually sending any messages.

    Mode.debug = True

.. will make the API output debug information to standard out.

License
-------
This code is free to use under the terms of the MIT license.


nereid-demo
===========

A little APP to test and get some source code about Nereid, a webdevelopment framework for Python based on Tryton.

In this repo you can get source code to:

 * Login
 * Registration
 * Reset password (and send emails)
 * Get info account user
 * Create or edit new cutomer addresses


Installation
------------

How to install Nereid and Tryton Nereid in Nereid doc: http://nereid.openlabs.co.in/docs/

 * Install Nereid in your system or virtualenv
 * Create new database and install Nereid module Tryton
 * When finish to create a database, go to Nereid menu and create a new website
   * Name: localhost

Configuration
-------------

Copy config.cfg.template to config.cfg and edit.

In nereid-demo dir, run:

    python application.py

New server run http://127.0.0.1:5000/

How to change server name
-------------------------

This demo use website name: localhost. If you like use another website name:

 * Edit config.cfg and change SITE param.
 * Go to Nereid / Configuration / Web Sites menu. Change website name server.
 * Copy localhost directory (templates) to 'newsite' name.

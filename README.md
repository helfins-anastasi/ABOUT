# ABOUT
An application that helps with utilizing unstructured time. Codenamed ABOUT, which stands for Application for Balancing Obligations in Unstructured Time.

Struggling to get things done? Want to learn a new skill but having trouble with motication? ABOUT can help you. Input the things you need to do, things you enjoy doing, and things you want to do, and ABOUT will help you decide what to do, and for how long.

## Setup Instructions (on MacOS)
* Install python 3.6 (`brew install python3`)
* Install heroku (`brew install heroku`)
* Install postgres (`brew install postgres`)
* Download django (`sudo -H pip3 install django`)
* download psycopg2 (`sudo -H pip3 install psycopg2`)
* Setup postgres (`mkdir /usr/local/pgsql && initdb -D /usr/local/pgsql/data -W -A password`)
* Create a database for about (`psql`; in shell enter `CREATE DATABASE aboutdb;` then `\q` to exit)

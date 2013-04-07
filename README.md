1Password for App Engine
========================

This App Engine app serves your 1PasswordAnywhere files so you can access your passwords through any modern browsers. 

See this page for information on 1PasswordAnywhere:
http://help.agilebits.com/1Password3/1passwordanywhere.html

You passwords should be reasonably safe. The keychain files are encrypted, all data will be sent over SSL, and only user logged in with your Google account will be able to access the files.

Setup
=====
1. Clone this project.
1. Zip your "1Password.keychain" file. You can also use a backup copy of your keychain, which is already zipped.
1. Add the zipped keychain file to the same directory as app.yaml.
1. Create a new App Engine app. https://cloud.google.com/console
1. Edit app.yaml with your app ID, filename of the keychain zip archive, and an email tied to your Google account.
1. Deploy your app and visit https://YOUR_APP_ID.appspot.com.

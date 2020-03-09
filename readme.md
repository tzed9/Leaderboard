Leaderboard update tool

Problem:  Existing Wordpress leadboard tool requires administrator access to perform updates on the admin portal
Solution: Create the client their own tool to add new drivers and lap times without requiring admin access

I established that the Wordpress site uses a Leaderboard plugin to display the results sorted by fastest
I tested SQL executions from Python successfully and investigated solutions to create cross-platform apps 

My first app creation package to try was Kivy, while this appears a good solution I found this difficult to implement
I moved on to PySimpleGUI and Windowsinstaller to prove the functionality of a tool and equip the client with a Windows application
Then I moved onto Beeware and successfully tested a basic form packaged as a Windows installer

MIT @ TZed9


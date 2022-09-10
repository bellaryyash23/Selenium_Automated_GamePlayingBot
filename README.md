# 🍪Automated Cookie Clicker Game🍪 using Selenium Web Driver of Python

🌟An Automated Game Playing Bot developed using Selenium Python package which opens the game url, plays the game consistently and using the algorithm designed in the program
applies the upgrades so as to maximize the cookie count/second.

🌟It makes the tedious and repititive task of clicking on cookie automated using Selenium package which contains various classes and their respective methods to automate
the game process.

👉In the 'main.py' first the 'chromedriver' application is loaded. This is passed as an argument to the webdriver class of selenium package.

👉Once, the driver is set up, the website url is passed to the driver and which loads the website in a new chrome window from where the game will be operated. It can been 
seen that the window is controlled by selenium driver as Chrome dislays a prompt indicating 'Chrome is being controlled by automated test software'.

👉The cookie item is found from website using the class methods like '.find_element()' which returns the cookie item as a selenium object. After acquiring this object the 
gameplay is initiated. The cookie clicking mechanism is automated by using the '.click()' method for repetitive clicking.

![Selenium Driven Gameplay Chrome Window](https://github.com/bellaryyash23/Selenium_Automated_GamePlayingBot/blob/master/window.JPG?raw=true)

👆Selenium Driven Game window of Chrome browser👆

👉The time module is used to set cutoff time for the gameplay to end and also to track time for succissive upgradation.

👉Using while loop the process is repeated. The time of start of gameplay is recorded and the bot is run for 4 minutes. After every 5 seconds the selenium driver is 
called to check for upgrades to increase the click speed. 

👉This is done using the alogrithm where the driver acquires the price of all items available for upgrade and the total amount of cookies available. It compares the 
available amount with price of each upgrade and finds the maximum possisible upgrade and clicks on it. This is done for every 5 seconds time iinterval.

👉After 4 minutes the bot is stopped and the gameplay window is closed by the selenium driver. At the end the cookies/second score of the bot is printed in the program console
for users reference.

![Selenium Driver's final score](https://github.com/bellaryyash23/Selenium_Automated_GamePlayingBot/blob/master/end.JPG?raw=true)

👆Selenium Driven Bot's Final Score👆

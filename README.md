# LeagueExcel

### The easiest way to track your League of Legends stats in Excel.

This application was put together for a personal need to record my stats in League of Legends. After manually doing it
for years in high school, I decided to make my own application to do it automatically for me using the Riot Games API
and Pythonh with openpyxl to modify Excel files.

### Setup
-----
<strong>THIS APPLICATION IS CURRENTLY UNDER DEVELOPMENT. MAKE SURE YOU HAVE BACKUPS OF YOUR FILES BEFORE USE.</strong>

To run the program, you will require Python v3.6 or later.

This program is terminal based. After opening a terminal in the root directory of the project, you can run the following command to start the application:

````
python league_excel.py
````

Once the program starts, it will prompt the user for input for three different fields:
<ul>
  <li>Riot API Key</li>
  <li>Summoner Name</li>
  <li>File Name</li>
</ul>

An API Key can be generated for anyone with a League of Legends account at the url https://developer.riotgames.com/.

The Summoner Name field is simply the username of the person whose stats you would like to track.

The file name will be whatever you would like to name the output excel file.

After these fields are correctly inputted, the output will be an excel file with the last 10 games that the person has played.

### Future Additions/Changes
-----
<ul>
  <li>Updating existing excel files</li>
  <li>More information generated, charts and tables on seperate sheets</li>
  <li>Graphical User Interface</li>
</ul>

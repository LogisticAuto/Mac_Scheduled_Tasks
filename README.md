# Getting Started
Cron jobs are used to schedule tasks or commands that need to be ran at certain points in time.

<b>Command:</b>&emsp;      <i>Cmd + Spacebar, type 'Terminal'</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Open Terminal Window</i><br>
<br>
<b>Command:</b>&emsp;      <i>crontab -l</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>List all cron jobs (This will show blank for now.)</i><br>
<br>
Crontab Editor is vim (Default). If you want to change it to Nano:<br>
&emsp;&emsp;<b>Command:</b>&emsp;      <i>export EDITOR=/usr/bin/nano</i><br>
&emsp;&emsp;<b>Purpose:</b>&emsp;&emsp;<i>Change editor to nano</i><br>
<br>
<b>Command:</b>&emsp;      <i>crontab -e</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Enter (VIM) edit mode. (Add, Remove, and Modify cron jobs)</i><br>
<br>
<b>Command:</b>&emsp;      <i>Press i</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Enter Insert Mode</i><br>
<br>
<b>Command:</b>&emsp;      <i>Press Esc, type :w, press Enter</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>To save a file</i><br>
<br>
<b>Command:</b>&emsp;      <i>Press Esc, type :x, press Enter</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>To save and quit</i><br>
<br>
<b>Command:</b>&emsp;      <i>type :q, press Enter</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>To quit (VIM)</i><br>
<br>
<b>Command:</b>&emsp;      <i>cat /tmp/test.tsx</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>View the file (cat means to print the content of a file onto the standard output stream, allowing us to view contents of the file.)</i><br>
<br>
# Cron commands
Cron values are used in the Unix-based cron scheduling system to define when and how often tasks or jobs should be executed. Cron uses a set of time-based fields to specify the schedule. The format consists of five fields, each representing a time unit. These fields are, in order:

<ol>
<li><b>Minutes (0-59):</b>&nbsp;The first field represents the minutes of the hour when the task will be executed. Valid values range from 0 to 59.</li>
  <b><li>Hours (0-23):</b>&nbsp;The second field represents the hours of the day when the task will run. Valid values range from 0 to 23 in a 24-hour format.</li>
  <b><li>Day of the Month (1-31):</b>&nbsp;The third field specifies the day of the month when the task should run. Valid values range from 1 to 31.</li>
  <b><li>Month (1-12 or Jan-Dec):</b>&nbsp;The fourth field designates the month when the task should be executed. You can use either numeric values (1-12) or the three-letter abbreviations of the month (e.g., Jan, Feb, Mar).</li>
  <b><li>Day of the Week (0-7 or Sun-Sat):</b>&nbsp;The fifth and final field defines the day of the week when the task is scheduled. Values can range from 0 to 7, where both 0 and 7 represent Sunday, or you can use the three-letter abbreviations of the days (e.g., Sun, Mon, Tue).</li>
</ol><br>
Each of these fields is separated by whitespace. You can use various special characters within these fields to create more complex schedules:<br>
<br>
<ul>
<li>An asterisk (*) signifies "every" or "any" value. For example, "*" in the minutes field means "every minute."</li>
  <li>A comma (,) allows you to specify a list of values. For example, "1,15,30" in the minutes field means the task will run at minutes 1, 15, and 30 past the hour.</li>
  <li>A hyphen (-) denotes a range of values. For example, "10-15" in the minutes field means the task will run from minute 10 to minute 15 past the hour.</li>
  <li>A slash (/) allows you to specify intervals. For example, "*/5" in the minutes field means the task will run every 5 minutes.</li>
  <li>You can also combine these characters to create more complex schedules. For example, "0 2-6,18-23 * * 1-5" means the task will run at minute 0, between 2AM and 6AM, and between the 18th and 23rd of each month, every weekday (1-5).</li>
  <li>'>>' means to append to the file</li>
  <li>'>' would mean to overwrite the file.</li>
</ul>

## Here are some examples of cron schedules:

<i></i>* * * * *:&emsp;&emsp;&emsp;&ensp;Run every minute.<br>
0 * * * *:&emsp;&emsp;&emsp;&nbsp;Run every hour, on the hour.<br>
0 0 * * *:&emsp;&emsp;&emsp;Run once a day, at midnight.<br>
0 12 * * 1-5:&emsp;&ensp;Run every weekday (Monday to Friday) at noon.<br>
0 0 * * 1:&emsp;&emsp;&emsp;Run every Monday at midnight.<br>
30 2 * 1,6 *:&emsp;&emsp;Run at 2:30 AM on the 1st and 6th day of the month.<br>
<br>
0 5 * * 5 rm -rf /tmp/*&emsp;&emsp;Empty temp folder every Friday at 5pm<br>
0 0 * * * rsync -a ~/Pictures/ ~/Google\ Drive/Pictures/&emsp;&emsp;Backup images to Google Drive, every night at midnight<br>
<i></i>* * * * * conda activate hack&emsp;&emsp;Activate Virtual Environment, every minute<br>
<br>
## Cron Job - Example 1
<b>Command:</b>&emsp;      <i>Cmd + Spacebar, type 'Terminal'</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Open Terminal Window</i><br>
<p></p>

<b>Command:</b>&emsp;      <i>crontab -e</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Enter edit mode</i><br>
<br>
<b>Command:</b>&emsp;      <i>Press i</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Enter Insert Mode</i><br>
<br>
<b>Command:</b>&emsp;      <i>* * * * * echo "Cron is running at $(date)" >> /tmp/test.txt.</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Output some text into a text file every minute of every hour of every day of every month</i><br>
<br>
<b>Command:</b>&emsp;      <i>Press Esc, type :w, press Enter</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Save the file</i><br>
<br>
<b>Command:</b>&emsp;      <i>type :q, press Enter</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>Quit (VIM editor)</i><br>
<br>
<b>Command:</b>&emsp;      <i>crontab -l</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>List your cron job(s) (Your command should now be listed.)</i><br>
<br>
<b>Command:</b>&emsp;      <i>cat /tmp/test.tsx</i><br>
<b>Purpose:</b>&emsp;&emsp;<i>View the file</i><br>
<br>
### Example 1 - Summary
Now, every minute, "Cron is running at the runtime" will be appended to the /tmp/test.txt. file.<br>
<br>
#### It is helpful to include the below syntax as a reminder within your cronjobs

# Crontab Structure
<i></i>#&ensp;┌───────────── minute (0 - 59)<br>
<i></i>#&ensp;│&nbsp;┌───────────── hour (0 - 23)<br>
<i></i>#&ensp;│&ensp;│&nbsp;┌───────────── day of month (1 - 31)<br>
<i></i>#&ensp;│&ensp;│&ensp;│&nbsp;┌───────────── month (1 - 12) (JAN-DEC)<br>
<i></i>#&ensp;│&ensp;│&ensp;│&ensp;│&nbsp;┌───────────── day of week (0 - 6) (SUN to SAT);<br>
<i></i>#&ensp;│&ensp;│&ensp;│&ensp;│&ensp;│<br>
<i></i>#&ensp;│&ensp;│&ensp;│&ensp;│&ensp;│<br>

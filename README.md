# no-ip.autorenew

Automate the process of renewing a no-ip account.

This respository consist of a python script that can be setup to be runed by a job scheduler, like cron,
every x time to update the no-ip account lease to another month.

I'n my case I use this to run on a RPi, which takes a while to run but works fine.


Dependencies
-----------------------------------------------------------

- iceweasel
- xvfb
- python
  - Selenium
  - pyvirtualdisplay

# SpaceShare

Package to setup ride and hotel room sharing.

For documentation, please refer to https://spaceshare.readthedocs.io/en/latest/

[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

An example config file is provided here:
```
# the config file for the email module
[EMAIL]
username=svenheydenreich
# password=123456
smtp_domain=smtp.gmail.com
smtp_port=587

[GOOGLE.SHEET]
sheet_id=1M6akYJ46z-qMZ_DDHyJvXr2U4rlqvZ8epe6PCa5tpHQ

[OPTIMIZATION]
#maximum difference in preferred departure time between people sharing a ride
max_wait_time=0.5
#maximum number of people per rideshare
max_people_per_car=3
```

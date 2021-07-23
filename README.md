# Python-IoT-Dashboard-Home-Automation

This project was developed by me using Python-Flask Webframework as backend, front end uses HTML with Bootstrap. The project can be taken as a template and can be used to make a bigger IoT Dashboard. 

The project currently supports 11 appliances of 2 rooms. First Room has 4 lights and 2 fans, while second room has 3 lights and 2 fans.

API request is in json format which can be viewed at localhost:5000/api_key=shahrukh123 after the project is up and running. The request can be parsed by a microcontroller such as an ESP8266 or ESP32 which then can be used to turn appliances On / Off.

# Files and directories

``` r
Python-IoT-Dashboard-Home-Automation
|--website
    |--static
        |--pic_1.jpg
        |--states.txt
    |--templates
        |--base.html
        |--index.html
        |--dashboard.html
        |--about.html
        |--contact.html
     |--__init__.py
     |--views.py
     |--api.py
|--main.py
```

# Screenshots of Project

Homepage

<kbd>![screencapture-localhost-5000-2021-07-23-20_58_31](https://user-images.githubusercontent.com/34818652/126810498-602571d9-c09e-4aae-9693-e2cb7f5e3a2f.png)</kbd>

Dashboard

<kbd>![screencapture-localhost-5000-dashboard-2021-07-23-20_58_57](https://user-images.githubusercontent.com/34818652/126810516-8a33f351-1f69-4dbf-8451-cf99e0eba5ba.png)</kbd>

Api Request json

<kbd>![screencapture-localhost-5000-api-key-shahrukh123-2021-07-23-21_10_44](https://user-images.githubusercontent.com/34818652/126810837-8a50fce9-a856-4a35-9a84-d2acb313c2fe.png)</kbd>

About page

<kbd>![screencapture-localhost-5000-about-2021-07-23-20_59_12](https://user-images.githubusercontent.com/34818652/126810526-08f22410-3bf3-4822-b286-77c020673f03.png)</kbd>

Contact page

<kbd>![screencapture-localhost-5000-contact-2021-07-23-20_59_18](https://user-images.githubusercontent.com/34818652/126810536-8200fa72-565e-4cf3-bada-8dc77933c3df.png)</kbd>

# How to run
Project can be run through main.py


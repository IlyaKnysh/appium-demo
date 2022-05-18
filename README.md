# Appium demo project (functional approach)

This is a demo project for appium tests for Android platform.

Stack:
- PyTest
- Appium
- Selene
- Allure

Supports for MacOS on real devices.

## Prerequisites:
### General
- node 10+ 

      $ brew install node
- appium 

      $ npm install -g appium
- wd 

      $ npm install wd
- java (8 version)

Set system variables:
- JAVA_HOME

### Android
- install android SDK (E.G. with Android Studio)

Set system variables:
- ANDROID_HOME (tools, platform-tools, build-tools)

## Install requirements:

    $ pip install -e .

## Run tests and generate report:

### 1. install allure globally

    $ npm install -g allure-commandline --save-dev

### 2. Run tests

    $ pytest --alluredir=allure-results

### 3. Generate report

    $ allure generate allure-results --clean -o allure-report && allure open


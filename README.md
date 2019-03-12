# Appium demo project

This is a demo project for appium tests for Android and iOS platforms.

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

### iOS
- Xcode
- libimobiledevice

      $ brew install libimobiledevice
- ios-deploy (brew install ios-deploy)

      $ brew install ios-deploy
- carthage

      $ brew install carthage

## Install requirements:

    $ pip install -e .

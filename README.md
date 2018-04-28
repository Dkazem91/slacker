# Slacker

*a simple slack app to update you on your docker containers*

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [File Structure](#file-structure)
* [Getting Started](#getting-started)
* [Usage Examples](#usage-examples)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


## Description

**Slacker** is a simple slack chat app that uses real-time monitorying to helps the user manage her Docker containers. The primary use of **Slacker 1.0** is to send a warning message when a container exceeds appropriate memory usage.  

## Purpose

**Slacker** was created as part of the 2018 \#HolbertonLovesDocker hackathon, a collaboration between Holberton School, an alternative to traditional software engineering education, and Docker, a popular open-source technology that enables users to containerize their programs, enabling faster, more efficient, and more versatile production and delivery. The hackathon was 24 hours long and teams had a maximum size of 3, necessitating flexibility and creativity.   

## File Structure

* [README](README.md) - this README file
* [pyslack](pyslack.py) - the python file containing the Slacker program

## Requirements

* Docker
* Python3
* Slack

## Usage Examples

**Slacker** will send you a message on Slack when the memory usage of any of your containers exceeds a set threshold; the default danger level is set to `1%` but can easily be changed in the function. 

## Bugs

At this time, there are no known bugs.


## Authors

Greg Dame | [GitHub](https://github.com/gjdame) | [Twitter](https://twitter.com/gjdame)   
Dan Kazemian | [GitHub](https://github.com/dkazem91) |[Twitter](https://twitter.com/Dan_Kazam)   
Lizzie Turner | [GitHub](https://github.com/lizzieturner) | [Twitter](https://twitter.com/_lizzieturner_)


## License

**slacker** is open source and free to download and use
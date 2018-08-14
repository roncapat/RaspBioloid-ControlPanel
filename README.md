# RaspBioloid-ControlPanel

A Control Panel for remote control and monitoring of RaspBioloid

## Introduction
The RaspBioloid Control Panel is part of a collection of packages grouped under the umbrella 
of the [RaspBioloid](https://github.com/roncapat/RaspBioloid) project. \
The aim of the project is to
provide a software infrastructure enabling an affordable robotic platform that could be used for
academic research.

This module aims to provide a minimal diagnostic GUI for the robot subsystems.

In particular:
* motors can be moved, locked and unlocked. Events such as goal position reached 
and overload are also notified with meaningful colors for easy understanding on what's going on.
* data from the inertial module and the onboard power supply manager are shown
* File-safe system shutdown can be enabled by setting a lower bound on external (battery) power source voltage.

This module (and other related modules in the project) is built on top the Robotic Operating system (ROS), 
and leverages the simplicity of Python and the brand new Qt for Python binding.

See [this wiki page](https://github.com/roncapat/RaspBioloid/wiki/Master-node-setup) for detailed instructions
on how to install the required dependencies and the module itself.

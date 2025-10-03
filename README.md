# Wowool SDK Examples

This repository contains examples for the Wowool SDK.

Note: You need to request an evaluation license at philippe@wowool.com. We will happily provide one.

## Installation

First, install the dependencies:

    python3 -m venv .env && . .env/bin/activate
    pip install -r requirements.txt


Next, set the environment variables, you can request a key by logging in and generating one. 
The samples are coded to use with the SDK and not the Cloud version.

    export WOWOOL_SDK_KEY=[wowool_key]
    

## Running the examples

Now you can start running the samples. For example:

    python sdk/samples/english-entities.py


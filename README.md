# Ircamamplify.io demo scripts

Try out ircamamplify.io APIs with this set of easy to use scripts. All you need is some audio files

## What's included

we've added a few simple to run examples of our beloved APIs to run quickly against your own account.

You can test:

- [Music Tagger](https://docs.ircamamplify.io/api#tag/Music-Tagger)

- [Ai Detector](https://docs.ircamamplify.io/api#tag/AI-Detector)

- [Quality Check](https://docs.ircamamplify.io/api#tag/Quality-Check)

## Getting started

![](/Users/romainsimiand/repositories/demo-scripts/medias/credentials.gif)



- go to https://app.ircamamplify.io/ and create an account if you haven't already

- head to [IRCAM Amplify](https://app.ircamamplify.io/api-credentials) credentials to generate a new pair of ID and Secret

- Select the API you wish to try, and paste your credentials in the `client_id` and `client_secret` 

- Run the script against any file you have locally

## How to use AI Detector

In order to help you test our AI Generated Detector API, we've included a `/medias` folder containing **one** simple audio file.


To use this file, simply run the following command

`python3 samplecode_aiDetector.py -i medias/aiGen1.wav`

# Streamlit-Docker-App

In this project, I used docker to package and ship a python based streamlit web app for an ROI calculator.

Steps

- I have a python file (app.py) where I imported streamlit as st

- I have my dependency file (requirements.txt) that has python library streamlit ready to be installed during the image build

- Then I have my Dockerfile where I used the base image (python:3.8) from the docker hub.

Configuring the Image Build/Run/Push

- I logged into docker via the command “docker login”

- then I built my custom image via the command “docker build -t <image-name> .”

- then I created a container out of the image via the command “docker run -d -p 8501:8501 <image-name>”

Pushing the image to docker hub I created a repository (make sure to create a profile first in ticket hub)

- First I gave the image a tag via the command “docker tag <image-id> <dockerhub-username>/<repo-name>:<tag>”

- Then I pushed to docker hub via the command “docker push <dockerhub-username>/<repo-name>:<tag>”

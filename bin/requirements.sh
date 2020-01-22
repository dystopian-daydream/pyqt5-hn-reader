#!/bin/bash

pip freeze | grep -vE "0.0.0" > requirements.txt
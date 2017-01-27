#!/bin/bash

rm -rf liphtePy.egg-info dist build
find . -name "*.pyc" -exec rm {} \;
find . -name "*~" -exec rm {} \;

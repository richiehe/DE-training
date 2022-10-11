#!/bin/bash

export AIRFLOW_HOME=$(PWD)/airflow

export PYTHONPATH=$PYTHONPATH:$(PWD)/

airflow standalone

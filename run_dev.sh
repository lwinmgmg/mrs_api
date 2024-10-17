#!/bin/bash

.venv/bin/python -m uvicorn mrs_api.main:app --reload

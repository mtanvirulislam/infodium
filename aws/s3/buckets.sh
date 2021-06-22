#!/bin/bash
set -x
awslocal s3 mb s3://raw-data
awslocal s3 mb s3://processed-data
set +x
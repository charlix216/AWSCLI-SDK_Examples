#!/usr/bin/env python

import boto3

# Connect to the Amazon EC2 service
ec2_client = boto3.client('ec2')

keypairs = ec2_client.describe_key_pairs()

for key in keypairs['KeyPairs']:
  if 'lab' not in key['KeyName'].lower():
    print "Deleting key pair", key['KeyName']
    ec2_client.delete_key_pair(KeyName=key['KeyName']

'''
The script does the following:

Connects to the Amazon EC2 service
Obtains a list of all Key Pairs
Deletes all Key Pairs except for the one with ‘lab’ in the name

'''

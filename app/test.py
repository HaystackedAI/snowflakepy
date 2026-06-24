#!/usr/bin/env python
# -*- coding: utf-8 -*-
import snowflake.connector
import getpass

"""
Simple Snowflake connection test using password authentication.

Note: externalbrowser auth doesn't work due to SAML configuration (error 390190).
Use password authentication instead.
"""

# Get password securely
password = getpass.getpass("Enter password for HAYSTACKEDAI: ")

# Connect to Snowflake
ctx = snowflake.connector.connect(
    account="NAYDHXW-NW07024",
    user="HAYSTACKEDAI",
    password=password
)

# Test the connection by getting Snowflake version
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(f"Connected successfully!")
    print(f"Snowflake version: {one_row[0]}")
finally:
    cs.close()

ctx.close()

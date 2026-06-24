#!/usr/bin/env python
# -*- coding: utf-8 -*-
import snowflake.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path='../.env')

# Get password from environment
password = os.getenv('SF_PWD')

if not password:
    raise ValueError("SF_PWD not found in .env file")

# Connect to Snowflake
ctx = snowflake.connector.connect(
    account="NAYDHXW-NW07024",
    user="HAYSTACKEDAI",
    password=password,
    session_parameters={'QUERY_TAG': 'EndOfMonthFinancials',}
)

# Test the connection by getting Snowflake version
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(f"Connected successfully!")
    print(f"Snowflake version: {one_row[0]}")
    cs.execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
    cs.execute("USE WAREHOUSE tiny_warehouse_mg")

finally:
    cs.close()

ctx.close()

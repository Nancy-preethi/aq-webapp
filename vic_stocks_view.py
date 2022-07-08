# streamlit_app.py

import streamlit as st
import psycopg2
import pandas as pd

# Initialize connection.
# Uses st.experimental_singleton to only run once.
from postgres_queries import *


@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
def run_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def fetch_stocks(erng_start_date, erng_end_date, hasEarnings, hasOptions, vic, insiders, hedgeFunds, vic_start_date, vic_end_date):
    connection = init_connection()
    subquery = ''
    if hasEarnings:
        subquery = postgres_select_stocks_for_earnings_criteria
    if hasOptions:
        subquery = subquery + postgres_select_stocks_for_options_criteria
    if insiders:
        subquery = subquery + postgres_select_stocks_for_insiders_criteria
    if vic:
        subquery = subquery + postgres_select_stocks_for_vic_criteria
    if hedgeFunds:
        subquery = subquery + postgres_select_stocks_for_hedge_fund_criteria
    fetch_stock_query = postgres_select_stocks_for_criteria + subquery + postgres_select_stocks_group_by_clause +postgres_select_stocks_order_by_clause

    if not vic and not hasEarnings:
        rows_df = pd.read_sql(fetch_stock_query, connection, params=[])
    elif vic and not hasEarnings:
        rows_df = pd.read_sql(fetch_stock_query, connection, params=[vic_start_date, vic_end_date])
    elif not vic and hasEarnings:
        rows_df = pd.read_sql(fetch_stock_query, connection, params=[erng_start_date, erng_end_date])
    else:
        rows_df = pd.read_sql(fetch_stock_query, connection, params=[vic_start_date, vic_end_date, erng_start_date, erng_end_date])
    print(fetch_stock_query)

    return rows_df


# rows = run_query("SELECT * from stocks_info;")
#
# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

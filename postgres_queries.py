postgres_select_stocks_for_criteria = """ select s.stock_ticker, s.name, e.earnings_date, v.published_date, v.published_price, s.price, 
        (s.price - v.published_price) as delta_from_publish, s.market_cap, s.cash, s.total_debt, s.eps, s.pe, s.day_low, s.day_high, v.vic_url  
        from stocks_info s left outer join vic_stocks v using (stock_ticker) 
        left outer join earnings_calendar_info e using (stock_ticker) 
        where 1=1 """  # dummy condition added so that the other subqueries can be added dynamically

postgres_select_stocks_for_earnings_criteria = " and s.stock_ticker=e.stock_ticker and e.earnings_date between %s and %s "
postgres_select_stocks_for_options_criteria = " and s.options = 'TRUE' "
postgres_select_stocks_for_insiders_criteria = " and s.insiders = 'TRUE' "
postgres_select_stocks_for_vic_criteria = " and (s.vic = 'TRUE' or s.stock_ticker=v.stock_ticker) and v.published_date between %s and %s "
postgres_select_stocks_for_hedge_fund_criteria = " and s.hedge_fund = 'TRUE' "
postgres_select_stocks_group_by_clause = """ group by s.stock_ticker, s.name, e.earnings_date, v.published_date, v.published_price, s.price,
        delta_from_publish, s.market_cap, s.cash, s.total_debt, s.eps, s.pe, s.day_low, s.day_high, v.vic_url """
postgres_select_stocks_order_by_clause = " order by  e.earnings_date, s.stock_ticker"

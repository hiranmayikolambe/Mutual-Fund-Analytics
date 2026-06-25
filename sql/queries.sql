SELECT scheme_name,
       aum_crore
FROM fact_aum a
JOIN dim_fund d
ON a.amfi_code=d.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;

SELECT strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

SELECT
strftime('%Y',transaction_date),
SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY 1;

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY 2 DESC;

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code=d.amfi_code
WHERE expense_ratio_pct<1;

Top 10 funds by Sharpe Ratio

Highest Alpha Funds

Average investment by city tier

Redemption amount by state

Fund house wise AUM


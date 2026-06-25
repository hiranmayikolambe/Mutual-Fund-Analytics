# Mutual Fund Data Dictionary

## aum_by_fund_house_cleaned.csv

Monthly AUM by Fund House

| Column | Data Type |
|----------|----------|
| date | datetime64[ns] |
| fund_house | object |
| aum_lakh_crore | float64 |
| aum_crore | int64 |
| num_schemes | int64 |


## benchmark_indices_cleaned.csv

Benchmark Index Values

| Column | Data Type |
|----------|----------|
| date | datetime64[ns] |
| index_name | object |
| close_value | float64 |


## category_inflows_cleaned.csv

Monthly Category Wise Net Inflows

| Column | Data Type |
|----------|----------|
| month | datetime64[ns] |
| category | object |
| net_inflow_crore | float64 |


## fund_master_cleaned.csv

Master Table of Mutual Funds

| Column | Data Type |
|----------|----------|
| amfi_code | int64 |
| fund_house | object |
| scheme_name | object |
| category | object |
| sub_category | object |
| plan | object |
| launch_date | datetime64[ns] |
| benchmark | object |
| expense_ratio_pct | float64 |
| exit_load_pct | float64 |
| min_sip_amount | int64 |
| min_lumpsum_amount | int64 |
| fund_manager | object |
| risk_category | object |
| sebi_category_code | object |


## industry_folio_count_cleaned.csv

Industry Folio Statistics

| Column | Data Type |
|----------|----------|
| month | datetime64[ns] |
| total_folios_crore | float64 |
| equity_folios_crore | float64 |
| debt_folios_crore | float64 |
| hybrid_folios_crore | float64 |
| others_folios_crore | float64 |


## monthly_sip_inflows_cleaned.csv

Industry SIP Statistics

| Column | Data Type |
|----------|----------|
| month | datetime64[ns] |
| sip_inflow_crore | int64 |
| active_sip_accounts_crore | float64 |
| new_sip_accounts_lakh | float64 |
| sip_aum_lakh_crore | float64 |
| yoy_growth_pct | float64 |


## portfolio_holdings_cleaned.csv

Fund Portfolio Holdings

| Column | Data Type |
|----------|----------|
| amfi_code | int64 |
| stock_symbol | object |
| stock_name | object |
| sector | object |
| weight_pct | float64 |
| market_value_cr | float64 |
| current_price_inr | float64 |
| portfolio_date | datetime64[ns] |



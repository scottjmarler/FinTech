import pip

def convert_usd_to_btc(usd_amount):             ## Define a function named convert_usd_to_bitcoin that accepts a single integer paramter named usd_amount
    current_btc_value = 9670                    ## Inside the function we store a new integer name current_btc_value
    return usd_amount / current_btc_value       ## Divide the usd_amount value by the current_btc_value and return the result

## Can also be written more concise

def convert_usd_to_btc(usd_amount, btc_value):
    return usd_amount / btc_value


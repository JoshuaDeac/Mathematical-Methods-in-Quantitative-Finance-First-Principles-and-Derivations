import os
import yfinance as yf

def run_and_export_lbo(ticker_symbol, debt_pct, annual_fcfs, exit_multiple, exit_ebitda):
    # 1. Fetch live market data
    ticker = yf.Ticker(ticker_symbol)
    try:
        share_price = ticker.fast_info['lastPrice']
    except Exception:
        history = ticker.history(period='1d', interval='1m')
        share_price = history['Close'].iloc[-1]
        
    try:
        shares = ticker.info.get('sharesOutstanding', 1000000000)
    except:
        shares = 1000000000
        
    live_equity_value = (share_price * shares) / 1e6  # in $M
    control_premium = 0.25  # 25% buyout premium
    purchase_price = live_equity_value * (1 + control_premium)
    
    total_debt = purchase_price * debt_pct
    sponsor_equity = purchase_price - total_debt
    
    # Track debt paydown
    current_debt = total_debt
    for fcf in annual_fcfs:
        current_debt -= fcf
    ending_debt = max(0.0, current_debt)
    
    # 2. Setup safe file path using os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "lbo-matrix.csv")
    
    # 3. Calculate matrix and write data to CSV
    multiples_to_test = [exit_multiple - 2.0, exit_multiple, exit_multiple + 2.0, exit_multiple + 4.0]
    
    print(f"\nWriting LBO results for {ticker_symbol} to CSV...")
    
    with open(output_file, "w") as f:
        # Write CSV Headers
        f.write("Ticker,Exit_Multiple,Exit_EV,Exit_Equity_Value,MoIC,IRR_Percent\n")
        
        for mult in multiples_to_test:
            exit_ev = exit_ebitda * mult
            exit_equity_value = exit_ev - ending_debt
            
            moic = exit_equity_value / sponsor_equity
            if moic > 0:
                irr = ((moic ** (1 / len(annual_fcfs))) - 1.0) * 100.0
            else:
                irr = -100.0
                
            # Print to terminal for your own visibility
            print(f"Exit: {mult}x | MoIC: {moic:.2f}x | IRR: {irr:.1f}%")
            
            # Write row to CSV
            f.write(f"{ticker_symbol},{mult},{exit_ev:.2f},{exit_equity_value:.2f},{moic:.2f},{irr:.2f}\n")
            
    print(f"Successfully saved file to: {output_file}")

if __name__ == "__main__":
    run_and_export_lbo(
        ticker_symbol="KKR",
        debt_pct=0.55,
        annual_fcfs=[150.0, 175.0, 200.0, 225.0, 250.0],
        exit_multiple=14.0,
        exit_ebitda=1200.0
    )

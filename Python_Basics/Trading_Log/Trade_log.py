#ANSI Colour Design Here
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[33m'

def get_best_trades(trade_log):
    most_profitable = []
    highest_profit = float('-inf')
    pnl = 0
    winning_trade = 0
    losing_trade = 0
    for trade in trade_log:
        trade_ids = trade["trade_id"]
        buy_priced = trade["buy_price"]
        sell_priced = trade["sell_price"]
        
        profit = sell_priced - buy_priced
        pnl += profit
        if profit >=0:
            winning_trade += 1
        else:
            losing_trade += 1

        if profit > highest_profit:
            highest_profit = profit
            most_profitable = [trade_ids]
        elif profit == highest_profit:
            most_profitable.append(trade_ids)

    the_winrate = winrate(losing_trade,winning_trade)   
    return most_profitable, highest_profit, pnl, the_winrate

def winrate(lost,win):
    total = win + lost
    percentage = (win/total) * 100
    
    return percentage

daily_trades = []

print(f"--{BOLD}{GREEN}WELCOME TO TRADE LOGGING CENTRE{END}--")
while True:
    while True:
        try:
            options = int(input(f"{BOLD}Please Choose Options Below\n1.Insert Trading Log\n2.Calculate Trading Log\n3.Exit\nInsert Number: {END}"))
            break
        except ValueError :
            print(f"{BOLD}{RED}Error: Please insert a number!{END}")
            continue

    if options == 1:
        counter = 1
        while True:
            try:
                trade_amount = int(input(f"{BOLD}\nPlease insert amount of trades done: {END}"))
                break
            except ValueError:
                print(f"{BOLD}{RED}Error: Please insert a number!{END}")
                continue

        for trade in range(trade_amount):
            trade_id = f"T-00{counter}"
            while True:
                try:
                    asset = str(input(f"{BOLD}Insert Ticker : {END}"))
                    buy_price = float(input(f"{BOLD}Insert Buy Price : {END}"))
                    sell_price = float(input(f"{BOLD}Insert Sell Price : {END}"))
                    break
                except ValueError:
                    print(f"{BOLD}{RED}Error: Please insert a right value!{END}")
                    continue
            
            daily_trades.append({  
                                 "trade_id": trade_id,
                                 "asset": asset,
                                 "buy_price": buy_price,
                                 "sell_price": sell_price})
            print (f'{BOLD}\n{YELLOW}Added:\nTrade ID :{trade_id}\nTicker:{asset}\nBuy Price:{buy_price}\nSell Price:{sell_price}{END}')
            counter += 1
            print(f'{BOLD}---------------------------------------{END}')
            
        print (f"{GREEN}{BOLD}Succesfully Added!{END}")

    elif options == 2:
       while True:
        if daily_trades == []:
            print(f"{BOLD}{RED}There is no trade logged. Please Choose Option 1 First.{END}")
            break   
        else:
            most_profitable, highest_profit, pnl, the_winrate =  get_best_trades(daily_trades)
            if highest_profit < 0:
                colour = RED
                most_profitable = None
            else : 
                colour = GREEN
            print (f"{BOLD}\nMost Profitable Trade : {most_profitable}\n{colour}Highest Profit Trade : {highest_profit}$\nPnL Data: {pnl}$\nWinrate Percentage {round(the_winrate,2)}%{END}")
            break

    elif options == 3:
        print(f"{BOLD}{RED}Initiating Exit Protocol. Exiting....{END}")
        break

    print(f'{BOLD}---------------------------------------{END}')



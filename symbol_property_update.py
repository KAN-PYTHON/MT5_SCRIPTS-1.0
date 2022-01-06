# ====================================================================
# MT5 Script for update quotes filtration properties of symbols
# ====================================================================
import datetime
import json
import mt5_webapi_lib as mt5
import logging

logging.basicConfig(filename="symbols_update.log", level=logging.INFO)

# Constants of MT5 Server
MT5_SERVER = 'webapi.educationvector.com'
MANGER_LOGIN = '1003'
MANGER_PASSWORD = 'hf7jrf83er'
SYMBOL_SUBSTR = ''

# Open session and get symbols count
# /api/symbol/total - Get symbols count total
session = mt5.connect(MT5_SERVER, MANGER_LOGIN, MANGER_PASSWORD)

try:
    symbols_total = session.get('https://' + MT5_SERVER + '/api/symbol/total')
except Exception:
    logging.error(str(datetime.datetime.now()) + ' Can\'t get the count of symbols')
    exit()

retcode = symbols_total.json().get('retcode')
answer = symbols_total.json().get('answer')

if retcode == "0 Done" and len(answer) != 0:
    symbols_total = int(symbols_total.json().get('answer')['total'])
    logging.info('\n' + 'START at ' + str(datetime.datetime.now()) + '\n' + 'Symbols total: ' + str(symbols_total) + '\n')
else:
    print('Error:', symbols_total.json().get('retcode'))
    logging.error(str(datetime.datetime.now()) + ' Can\'t get the count of symbols' +
                  str(symbols_total.status_code))
    exit()

# Main cycle while
# Sort through the symbols in order and change the properties
i = 0
updated_count = 0

while i < symbols_total:

    # /api/symbol/next?index= - Get Symbol properties by index
    try:
        symbol_property = session.get('https://' + MT5_SERVER + '/api/symbol/next?index=' + str(i))
    except Exception:
        logging.error(str(datetime.datetime.now()) + ' Can\'t get the symbol property, ID: ' + str(i))
        i += 1
        continue

    retcode = symbol_property.json().get('retcode')
    answer = symbol_property.json().get('answer')

    if retcode == "0 Done" and len(answer) != 0:
        symbol_name = str(symbol_property.json().get('answer')['Symbol'])
    else:
        logging.error(str(datetime.datetime.now()) + ' Can\'t get the symbol name, ID: ' + str(i))
        i += 1
        continue

    # /api/tick/last - Get Symbol prices by name
    try:
        symbol_price = session.get('https://' + MT5_SERVER + '/api/tick/last',
                                   params={'symbol': symbol_name, 'trans_id': 0}, verify=False, timeout=2)
    except Exception:
        logging.error(str(datetime.datetime.now()) + ' Can\'t get the symbol price, ID: ' + str(i) + '; ' + symbol_name)
        i += 1
        continue

    retcode = symbol_price.json().get('retcode')
    answer = symbol_price.json().get('answer')

    if retcode == "0 Done" and len(answer) != 0:
        symbol_path = symbol_property.json().get('answer')['Path']
        if symbol_path.find(SYMBOL_SUBSTR) < 0:
            logging.error(str(datetime.datetime.now()) + ' Symbol skipped, ID: ' + str(i) + '; ' + symbol_name)
            i += 1
            continue

        symbol_digits = symbol_property.json().get('answer')['Digits']
        symbol_ask = float(symbol_price.json().get('answer')[0]['Ask'])
        symbol_bid = float(symbol_price.json().get('answer')[0]['Bid'])
        symbol_spread = int((symbol_ask - symbol_bid) * 10 ** int(symbol_digits))

        if symbol_spread == 0:
            logging.error(str(datetime.datetime.now()) + ' Symbol spread error, ID: ' + str(i) + '; ' + symbol_name)
            i += 1
            continue
        # logging.info(symbol_name + '/' + str(symbol_digits) + '/' + str(symbol_bid) + '/' + str(symbol_ask))

        # Formation of new parameters to json
        symbol_property = symbol_property.json()
        symbol_property['answer']['FilterSoft'] = str(symbol_spread * 10)
        symbol_property['answer']['FilterSoftTicks'] = '2'
        symbol_property['answer']['FilterHard'] = str(symbol_spread * 20)
        symbol_property['answer']['FilterHardTicks'] = '3'
        symbol_property['answer']['FilterDiscard'] = str(symbol_spread * 100)
        symbol_property = json.dumps(symbol_property['answer'])

        # Update symbols params
        try:
            symbol_update = session.post('https://' + MT5_SERVER + '/api/symbol/add?', symbol_property,
                                     verify=False, timeout=2)
        except Exception:
            logging.error(str(datetime.datetime.now()) + ' Can\'t get update the symbol, ID: ' + str(i) + '; ' + symbol_name)
            i += 1
            continue

        retcode = symbol_update.json().get('retcode')
        answer = symbol_update.json().get('answer')

        if retcode == "0 Done" and len(answer) != 0:
            logging.info(str(datetime.datetime.now()) + ' Update, ID: ' + str(i) + '; ' + symbol_name + ' (' +
                         str(symbol_spread) + '/' +
                         str(symbol_spread * 10) + '/' +
                         str(symbol_spread * 20) + '/' +
                         str(symbol_spread * 100) + ')' + ' -> Ok')
            updated_count += 1
        else:
            logging.error(str(datetime.datetime.now()) + ' Update error, ID: ' + str(i) + '; ' + symbol_name)
            i += 1
            continue
    else:
        logging.error(str(datetime.datetime.now()) + ' Request price error, ID: ' + str(i) + '; ' + symbol_name)
        i += 1
        continue
    i += 1

logging.info('\n' + 'END at ' + str(datetime.datetime.now()) + '\n' + 'Updated symbols: ' + str(updated_count) + '\n')
# End of while
# End of PROGRAM

# Python Version : 3
# Packages 
# ---------
#   pip install beautifulsoup4
#   pip install requests



from bs4 import BeautifulSoup
from requests import get

arz = {
    "BTC": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "ETH": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "BNB": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "USDT": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "ADA": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "SOL": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "XRP": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "DOGE": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "USDC": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "LINK": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "LTC": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "BUSD": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "BCH": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "TRX": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
    "ETC": {
        "nerkhToman": None,
        "nerkhDolar": None,
        "taqiratRozane": None,
    },
}

result = get("https://ramzarz.news/coins/")

content = BeautifulSoup(result.text,"html.parser")


def BTC():
    Toman = content.find("span",attrs={"name":"tomanPrice_bitcoin"})
    Dolar = content.find("span",attrs={"data-live-price":"bitcoin"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"BTC"})




    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for btc in Toman.text:
        if btc in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(btc)
        else: pass


    arz["BTC"]["nerkhToman"] = toman
    arz["BTC"]["nerkhDolar"] = dolar
    arz["BTC"]["taqiratRozane"] = taqirat_rozane

    return "BTC - OK"






def ETH():
    Toman = content.find("span",attrs={"name":"tomanPrice_ethereum"})
    Dolar = content.find("span",attrs={"data-live-price":"ethereum"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"ETH"})




    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for eth in Toman.text:
        if eth in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(eth)
        else: pass


    arz["ETH"]["nerkhToman"] = toman
    arz["ETH"]["nerkhDolar"] = dolar
    arz["ETH"]["taqiratRozane"] = taqirat_rozane

    return "ETH - OK"



def BNB():

    Toman = content.find("span",attrs={"name":"tomanPrice_binance-coin"})
    Dolar = content.find("span",attrs={"data-live-price":"binance-coin"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"BNB"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for bnb in Toman.text:
        if bnb in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(bnb)
        else: pass


    arz["BNB"]["nerkhToman"] = toman
    arz["BNB"]["nerkhDolar"] = dolar
    arz["BNB"]["taqiratRozane"] = taqirat_rozane

    return "BNB - OK"


def USDT():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_tether"})
    Dolar = content.find("span",attrs={"data-live-price":"tether"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"USDT"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for usdt in Toman.text:
        if usdt in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(usdt)
        else: pass


    arz["USDT"]["nerkhToman"] = toman
    arz["USDT"]["nerkhDolar"] = dolar
    arz["USDT"]["taqiratRozane"] = taqirat_rozane

    return "USDT - OK"


def ADA():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_cardano"})
    Dolar = content.find("span",attrs={"data-live-price":"cardano"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"ADA"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for ada in Toman.text:
        if ada in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(ada)
        else: pass


    arz["ADA"]["nerkhToman"] = toman
    arz["ADA"]["nerkhDolar"] = dolar
    arz["ADA"]["taqiratRozane"] = taqirat_rozane

    return "ADA - OK"


def SOL():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_solana"})
    Dolar = content.find("span",attrs={"data-live-price":"solana"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"SOL"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for sol in Toman.text:
        if sol in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(sol)
        else: pass


    arz["SOL"]["nerkhToman"] = toman
    arz["SOL"]["nerkhDolar"] = dolar
    arz["SOL"]["taqiratRozane"] = taqirat_rozane

    return "SOL - OK"


def XRP():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_ripple"})
    Dolar = content.find("span",attrs={"data-live-price":"ripple"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"XRP"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for xrp in Toman.text:
        if xrp in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(xrp)
        else: pass


    arz["XRP"]["nerkhToman"] = toman
    arz["XRP"]["nerkhDolar"] = dolar
    arz["XRP"]["taqiratRozane"] = taqirat_rozane

    return "XRP - OK"


def DOGE():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_dogecoin"})
    Dolar = content.find("span",attrs={"data-live-price":"dogecoin"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"DOGE"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for doje in Toman.text:
        if doje in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(doje)
        else: pass


    arz["DOGE"]["nerkhToman"] = toman
    arz["DOGE"]["nerkhDolar"] = dolar
    arz["DOGE"]["taqiratRozane"] = taqirat_rozane

    return "DOGE - OK"



def USDC():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_usd-coin"})
    Dolar = content.find("span",attrs={"data-live-price":"usd-coin"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"USDC"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for usdc in Toman.text:
        if usdc in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(usdc)
        else: pass


    arz["USDC"]["nerkhToman"] = toman
    arz["USDC"]["nerkhDolar"] = dolar
    arz["USDC"]["taqiratRozane"] = taqirat_rozane

    return "USDC - OK"

def LINK():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_chainlink"})
    Dolar = content.find("span",attrs={"data-live-price":"chainlink"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"LINK"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for link in Toman.text:
        if link in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(link)
        else: pass


    arz["LINK"]["nerkhToman"] = toman
    arz["LINK"]["nerkhDolar"] = dolar
    arz["LINK"]["taqiratRozane"] = taqirat_rozane

    return "LINK - OK"


def LTC():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_litecoin"})
    Dolar = content.find("span",attrs={"data-live-price":"litecoin"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"LTC"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for ltc in Toman.text:
        if ltc in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(ltc)
        else: pass


    arz["LTC"]["nerkhToman"] = toman
    arz["LTC"]["nerkhDolar"] = dolar
    arz["LTC"]["taqiratRozane"] = taqirat_rozane

    return "LTC - OK"


def BUSD():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_binance-usd"})
    Dolar = content.find("span",attrs={"data-live-price":"binance-usd"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"BUSD"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for busd in Toman.text:
        if busd in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(busd)
        else: pass


    arz["BUSD"]["nerkhToman"] = toman
    arz["BUSD"]["nerkhDolar"] = dolar
    arz["BUSD"]["taqiratRozane"] = taqirat_rozane

    return "BUSD - OK"

def BCH():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_bitcoin-cash"})
    Dolar = content.find("span",attrs={"data-live-price":"bitcoin-cash"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"BCH"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for bch in Toman.text:
        if bch in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(bch)
        else: pass


    arz["BCH"]["nerkhToman"] = toman
    arz["BCH"]["nerkhDolar"] = dolar
    arz["BCH"]["taqiratRozane"] = taqirat_rozane

    return "BCH - OK"


def TRX():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_tron"})
    Dolar = content.find("span",attrs={"data-live-price":"tron"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"TRX"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for trx in Toman.text:
        if trx in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(trx)
        else: pass


    arz["TRX"]["nerkhToman"] = toman
    arz["TRX"]["nerkhDolar"] = dolar
    arz["TRX"]["taqiratRozane"] = taqirat_rozane

    return "TRX - OK"



def ETC():
    
    Toman = content.find("span",attrs={"name":"tomanPrice_ethereum-classic"})
    Dolar = content.find("span",attrs={"data-live-price":"ethereum-classic"})
    TaqiratRozane = content.find("span",attrs={"data-table-change":"ETC"})

   



    toman = ""
    dolar = Dolar.text
    taqirat_rozane = TaqiratRozane.text


    for etc in Toman.text:
        if etc in ["1","2","3","4","6","7","8","9","0",","]:
            toman += str(etc)
        else: pass


    arz["ETC"]["nerkhToman"] = toman
    arz["ETC"]["nerkhDolar"] = dolar
    arz["ETC"]["taqiratRozane"] = taqirat_rozane

    return "ETC - OK"


def main():
    BTC()
    ETH()
    BNB()
    USDT()
    ADA()
    SOL()
    XRP()
    DOGE()
    USDC()
    LINK()
    LTC()
    BUSD()
    BCH()
    TRX()
    ETC()


main()

print(arz)
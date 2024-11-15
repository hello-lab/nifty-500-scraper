import yfinance as yf
import pandas as pd

# Function to calculate RSI
def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

gcnt=0
cnt=0
results=[["nifty 100","nifty 100","nifty 100","nifty 100","nifty 100"]]
names100=["ABB India Ltd.", "Adani Energy Solutions Ltd.", "Adani Enterprises Ltd.", "Adani Green Energy Ltd.", "Adani Ports and Special Economic Zone Ltd.", "Adani Power Ltd.", "Adani Total Gas Ltd.", "Ambuja Cements Ltd.", "Apollo Hospitals Enterprise Ltd.", "Asian Paints Ltd.", "Avenue Supermarts Ltd.", "Axis Bank Ltd.", "Bajaj Auto Ltd.", "Bajaj Finance Ltd.", "Bajaj Finserv Ltd.", "Bajaj Holdings & Investment Ltd.", "Bank of Baroda", "Bharat Electronics Ltd.", "Bharat Heavy Electricals Ltd.", "Bharat Petroleum Corporation Ltd.", "Bharti Airtel Ltd.", "Bosch Ltd.", "Britannia Industries Ltd.", "Canara Bank", "Cholamandalam Investment and Finance Company Ltd.", "Cipla Ltd.", "Coal India Ltd.", "DLF Ltd.", "Dabur India Ltd.", "Divi's Laboratories Ltd.", "Dr. Reddy's Laboratories Ltd.", "Eicher Motors Ltd.", "GAIL (India) Ltd.", "Godrej Consumer Products Ltd.", "Grasim Industries Ltd.", "HCL Technologies Ltd.", "HDFC Bank Ltd.", "HDFC Life Insurance Company Ltd.", "Havells India Ltd.", "Hero MotoCorp Ltd.", "Hindalco Industries Ltd.", "Hindustan Aeronautics Ltd.", "Hindustan Unilever Ltd.", "ICICI Bank Ltd.", "ICICI Lombard General Insurance Company Ltd.", "ICICI Prudential Life Insurance Company Ltd.", "ITC Ltd.", "Indian Oil Corporation Ltd.", "Indian Railway Catering And Tourism Corporation Ltd.", "Indian Railway Finance Corporation Ltd.", "IndusInd Bank Ltd.", "Info Edge (India) Ltd.", "Infosys Ltd.", "InterGlobe Aviation Ltd.", "JSW Energy Ltd.", "JSW Steel Ltd.", "Jindal Steel & Power Ltd.", "Jio Financial Services Ltd.", "Kotak Mahindra Bank Ltd.", "LTIMindtree Ltd.", "Larsen & Toubro Ltd.", "Life Insurance Corporation of India", "Macrotech Developers Ltd.", "Mahindra & Mahindra Ltd.", "Maruti Suzuki India Ltd.", "NHPC Ltd.", "NTPC Ltd.", "Nestle India Ltd.", "Oil & Natural Gas Corporation Ltd.", "Pidilite Industries Ltd.", "Power Finance Corporation Ltd.", "Power Grid Corporation of India Ltd.", "Punjab National Bank", "REC Ltd.", "Reliance Industries Ltd.", "SBI Life Insurance Company Ltd.", "Samvardhana Motherson International Ltd.", "Shree Cement Ltd.", "Shriram Finance Ltd.", "Siemens Ltd.", "State Bank of India", "Sun Pharmaceutical Industries Ltd.", "TVS Motor Company Ltd.", "Tata Consultancy Services Ltd.", "Tata Consumer Products Ltd.", "Tata Motors Ltd.", "Tata Power Co. Ltd.", "Tata Steel Ltd.", "Tech Mahindra Ltd.", "Titan Company Ltd.", "Torrent Pharmaceuticals Ltd.", "Trent Ltd.", "UltraTech Cement Ltd.", "Union Bank of India", "United Spirits Ltd.", "Varun Beverages Ltd.", "Vedanta Ltd.", "Wipro Ltd.", "Zomato Ltd.", "Zydus Lifesciences Ltd."]
tickers100 = "ABB ADANIENSOL ADANIENT ADANIGREEN ADANIPORTS ADANIPOWER ATGL AMBUJACEM APOLLOHOSP ASIANPAINT DMART AXISBANK BAJAJ-AUTO BAJFINANCE BAJAJFINSV BAJAJHLDNG BANKBARODA BEL BHEL BPCL BHARTIARTL BOSCHLTD BRITANNIA CANBK CHOLAFIN CIPLA COALINDIA DLF DABUR DIVISLAB DRREDDY EICHERMOT GAIL GODREJCP GRASIM HCLTECH HDFCBANK HDFCLIFE HAVELLS HEROMOTOCO HINDALCO HAL HINDUNILVR ICICIBANK ICICIGI ICICIPRULI ITC IOC IRCTC IRFC INDUSINDBK NAUKRI INFY INDIGO JSWENERGY JSWSTEEL JINDALSTEL JIOFIN KOTAKBANK LTIM LT LICI LODHA M&M MARUTI NHPC NTPC NESTLEIND ONGC PIDILITIND PFC POWERGRID PNB RECLTD RELIANCE SBILIFE MOTHERSON SHREECEM SHRIRAMFIN SIEMENS SBIN SUNPHARMA TVSMOTOR TCS TATACONSUM TATAMOTORS TATAPOWER TATASTEEL TECHM TITAN TORNTPHARM TRENT ULTRACEMCO UNIONBANK UNITDSPR VBL VEDL WIPRO ZOMATO ZYDUSLIFE"

names150=["3M India Ltd.", "ACC Ltd.", "AIA Engineering Ltd.", "APL Apollo Tubes Ltd.", "AU Small Finance Bank Ltd.", "Abbott India Ltd.", "Adani Wilmar Ltd.", "Aditya Birla Capital Ltd.", "Aditya Birla Fashion and Retail Ltd.", "Ajanta Pharmaceuticals Ltd.", "Alkem Laboratories Ltd.", "Apollo Tyres Ltd.", "Ashok Leyland Ltd.", "Astral Ltd.", "Aurobindo Pharma Ltd.", "BSE Ltd.", "Balkrishna Industries Ltd.", "Bandhan Bank Ltd.", "Bank of India", "Bank of Maharashtra", "Bayer Cropscience Ltd.", "Berger Paints India Ltd.", "Bharat Dynamics Ltd.", "Bharat Forge Ltd.", "Bharti Hexacom Ltd.", "Biocon Ltd.", "CG Power and Industrial Solutions Ltd.", "CRISIL Ltd.", "Carborundum Universal Ltd.", "Cochin Shipyard Ltd.", "Coforge Ltd.", "Colgate Palmolive (India) Ltd.", "Container Corporation of India Ltd.", "Coromandel International Ltd.", "Cummins India Ltd.", "Dalmia Bharat Ltd.", "Deepak Nitrite Ltd.", "Delhivery Ltd.", "Dixon Technologies (India) Ltd.", "Emami Ltd.", "Endurance Technologies Ltd.", "Escorts Kubota Ltd.", "Exide Industries Ltd.", "FSN E-Commerce Ventures Ltd.", "Federal Bank Ltd.", "Fertilisers and Chemicals Travancore Ltd.", "Fortis Healthcare Ltd.", "GMR Airports Infrastructure Ltd.", "General Insurance Corporation of India", "Gland Pharma Ltd.", "Glaxosmithkline Pharmaceuticals Ltd.", "Global Health Ltd.", "Godrej Industries Ltd.", "Godrej Properties Ltd.", "Grindwell Norton Ltd.", "Gujarat Fluorochemicals Ltd.", "Gujarat Gas Ltd.", "HDFC Asset Management Company Ltd.", "Hindustan Petroleum Corporation Ltd.", "Hindustan Zinc Ltd.", "Hitachi Energy India Ltd.", "Honeywell Automation India Ltd.", "Housing & Urban Development Corporation Ltd.", "IDBI Bank Ltd.", "IDFC First Bank Ltd.", "IRB Infrastructure Developers Ltd.", "Indian Bank", "Indian Hotels Co. Ltd.", "Indian Overseas Bank", "Indian Renewable Energy Development Agency Ltd.", "Indraprastha Gas Ltd.", "Indus Towers Ltd.", "Ipca Laboratories Ltd.", "J.K. Cement Ltd.", "JSW Infrastructure Ltd.", "Jindal Stainless Ltd.", "Jubilant Foodworks Ltd.", "K.P.R. Mill Ltd.", "KEI Industries Ltd.", "KPIT Technologies Ltd.", "Kalyan Jewellers India Ltd.", "L&T Finance Ltd.", "L&T Technology Services Ltd.", "LIC Housing Finance Ltd.", "Linde India Ltd.", "Lloyds Metals And Energy Ltd.", "Lupin Ltd.", "MRF Ltd.", "Mahindra & Mahindra Financial Services Ltd.", "Mangalore Refinery & Petrochemicals Ltd.", "Mankind Pharma Ltd.", "Marico Ltd.", "Max Financial Services Ltd.", "Max Healthcare Institute Ltd.", "Mazagoan Dock Shipbuilders Ltd.", "Metro Brands Ltd.", "Motherson Sumi Wiring India Ltd.", "MphasiS Ltd.", "Muthoot Finance Ltd.", "NLC India Ltd.", "NMDC Ltd.", "Nippon Life India Asset Management Ltd.", "Oberoi Realty Ltd.", "Oil India Ltd.", "One 97 Communications Ltd.", "Oracle Financial Services Software Ltd.", "PB Fintech Ltd.", "PI Industries Ltd.", "Page Industries Ltd.", "Patanjali Foods Ltd.", "Persistent Systems Ltd.", "Petronet LNG Ltd.", "Phoenix Mills Ltd.", "Polycab India Ltd.", "Poonawalla Fincorp Ltd.", "Prestige Estates Projects Ltd.", "Procter & Gamble Hygiene & Health Care Ltd.", "Rail Vikas Nigam Ltd.", "SBI Cards and Payment Services Ltd.", "SJVN Ltd.", "SKF India Ltd.", "SRF Ltd.", "Schaeffler India Ltd.", "Solar Industries India Ltd.", "Sona BLW Precision Forgings Ltd.", "Star Health and Allied Insurance Company Ltd.", "Steel Authority of India Ltd.", "Sun TV Network Ltd.", "Sundaram Finance Ltd.", "Sundram Fasteners Ltd.", "Supreme Industries Ltd.", "Suzlon Energy Ltd.", "Syngene International Ltd.", "Tata Chemicals Ltd.", "Tata Communications Ltd.", "Tata Elxsi Ltd.", "Tata Investment Corporation Ltd.", "Tata Technologies Ltd.", "The New India Assurance Company Ltd.", "Thermax Ltd.", "Timken India Ltd.", "Torrent Power Ltd.", "Tube Investments of India Ltd.", "UNO Minda Ltd.", "UPL Ltd.", "United Breweries Ltd.", "Vodafone Idea Ltd.", "Voltas Ltd.", "Yes Bank Ltd.", "ZF Commercial Vehicle Control Systems India Ltd."]
tickers150="3MINDIA ACC AIAENG APLAPOLLO AUBANK ABBOTINDIA AWL ABCAPITAL ABFRL AJANTPHARM ALKEM APOLLOTYRE ASHOKLEY ASTRAL AUROPHARMA BSE BALKRISIND BANDHANBNK BANKINDIA MAHABANK BAYERCROP BERGEPAINT BDL BHARATFORG BHARTIHEXA BIOCON CGPOWER CRISIL CARBORUNIV COCHINSHIP COFORGE COLPAL CONCOR COROMANDEL CUMMINSIND DALBHARAT DEEPAKNTR DELHIVERY DIXON EMAMILTD ENDURANCE ESCORTS EXIDEIND NYKAA FEDERALBNK FACT FORTIS GMRINFRA GICRE GLAND GLAXO MEDANTA GODREJIND GODREJPROP GRINDWELL FLUOROCHEM GUJGASLTD HDFCAMC HINDPETRO HINDZINC POWERINDIA HONAUT HUDCO IDBI IDFCFIRSTB IRB INDIANB INDHOTEL IOB IREDA IGL INDUSTOWER IPCALAB JKCEMENT JSWINFRA JSL JUBLFOOD KPRMILL KEI KPITTECH KALYANKJIL LTF LTTS LICHSGFIN LINDEINDIA LLOYDSME LUPIN MRF M&MFIN MRPL MANKIND MARICO MFSL MAXHEALTH MAZDOCK METROBRAND MSUMI MPHASIS MUTHOOTFIN NLCINDIA NMDC NAM-INDIA OBEROIRLTY OIL PAYTM OFSS POLICYBZR PIIND PAGEIND PATANJALI PERSISTENT PETRONET PHOENIXLTD POLYCAB POONAWALLA PRESTIGE PGHH RVNL SBICARD SJVN SKFINDIA SRF SCHAEFFLER SOLARINDS SONACOMS STARHEALTH SAIL SUNTV SUNDARMFIN SUNDRMFAST SUPREMEIND SUZLON SYNGENE TATACHEM TATACOMM TATAELXSI TATAINVEST TATATECH NIACL THERMAX TIMKEN TORNTPOWER TIINDIA UNOMINDA UPL UBL IDEA VOLTAS YESBANK ZFCVINDIA"

names250=["360 ONE WAM Ltd.", "Aadhar Housing Finance Ltd.", "Aarti Industries Ltd.", "Aavas Financiers Ltd.", "Action Construction Equipment Ltd.", "Aditya Birla Real Estate Ltd.", "Aditya Birla Sun Life AMC Ltd.", "Aegis Logistics Ltd.", "Affle (India) Ltd.", "Akums Drugs and Pharmaceuticals Ltd.", "Alembic Pharmaceuticals Ltd.", "Alkyl Amines Chemicals Ltd.", "Alok Industries Ltd.", "Amara Raja Energy & Mobility Ltd.", "Amber Enterprises India Ltd.", "Anand Rathi Wealth Ltd.", "Anant Raj Ltd.", "Angel One Ltd.", "Apar Industries Ltd.", "Aptus Value Housing Finance India Ltd.", "Archean Chemical Industries Ltd.", "Asahi India Glass Ltd.", "Aster DM Healthcare Ltd.", "AstraZenca Pharma India Ltd.", "Atul Ltd.", "Avanti Feeds Ltd.", "BASF India Ltd.", "BEML Ltd.", "BLS International Services Ltd.", "Balaji Amines Ltd.", "Balrampur Chini Mills Ltd.", "Bata India Ltd.", "Bikaji Foods International Ltd.", "Birla Corporation Ltd.", "Birlasoft Ltd.", "Blue Dart Express Ltd.", "Blue Star Ltd.", "Bombay Burmah Trading Corporation Ltd.", "Brigade Enterprises Ltd.", "C.E. Info Systems Ltd.", "CCL Products (I) Ltd.", "CESC Ltd.", "CIE Automotive India Ltd.", "Campus Activewear Ltd.", "Can Fin Homes Ltd.", "Caplin Point Laboratories Ltd.", "Capri Global Capital Ltd.", "Castrol India Ltd.", "Ceat Ltd.", "Cello World Ltd.", "Central Bank of India", "Central Depository Services (India) Ltd.", "Century Plyboards (India) Ltd.", "Cera Sanitaryware Ltd", "Chalet Hotels Ltd.", "Chambal Fertilizers & Chemicals Ltd.", "Chemplast Sanmar Ltd.", "Chennai Petroleum Corporation Ltd.", "Cholamandalam Financial Holdings Ltd.", "City Union Bank Ltd.", "Clean Science and Technology Ltd.", "Computer Age Management Services Ltd.", "Concord Biotech Ltd.", "Craftsman Automation Ltd.", "CreditAccess Grameen Ltd.", "Crompton Greaves Consumer Electricals Ltd.", "Cyient Ltd.", "DOMS Industries Ltd.", "Data Patterns (India) Ltd.", "Deepak Fertilisers & Petrochemicals Corp. Ltd.", "Devyani International Ltd.", "Dr. Lal Path Labs Ltd.", "E.I.D. Parry (India) Ltd.", "EIH Ltd.", "Easy Trip Planners Ltd.", "Elecon Engineering Co. Ltd.", "Elgi Equipments Ltd.", "Emcure Pharmaceuticals Ltd.", "Engineers India Ltd.", "Equitas Small Finance Bank Ltd.", "Eris Lifesciences Ltd.", "Fine Organic Industries Ltd.", "Finolex Cables Ltd.", "Finolex Industries Ltd.", "Firstsource Solutions Ltd.", "Five-Star Business Finance Ltd.", "G R Infraprojects Ltd.", "GE Vernova T&D India Ltd.", "Garden Reach Shipbuilders & Engineers Ltd.", "Gillette India Ltd.", "Glenmark Pharmaceuticals Ltd.", "Go Digit General Insurance Ltd.", "Godawari Power & Ispat Ltd.", "Godfrey Phillips India Ltd.", "Godrej Agrovet Ltd.", "Granules India Ltd.", "Graphite India Ltd.", "Great Eastern Shipping Co. Ltd.", "Gujarat Ambuja Exports Ltd.", "Gujarat Mineral Development Corporation Ltd.", "Gujarat Narmada Valley Fertilizers and Chemicals Ltd.", "Gujarat Pipavav Port Ltd.", "Gujarat State Fertilizers & Chemicals Ltd.", "Gujarat State Petronet Ltd.", "H.E.G. Ltd.", "HBL Power Systems Ltd.", "HFCL Ltd.", "Happiest Minds Technologies Ltd.", "Himadri Speciality Chemical Ltd.", "Hindustan Copper Ltd.", "Home First Finance Company India Ltd.", "Honasa Consumer Ltd.", "ICICI Securities Ltd.", "IFCI Ltd.", "IIFL Finance Ltd.", "INOX India Ltd.", "IRCON International Ltd.", "ITI Ltd.", "Indegene Ltd.", "India Cements Ltd.", "Indiamart Intermesh Ltd.", "Indian Energy Exchange Ltd.", "Inox Wind Ltd.", "Intellect Design Arena Ltd.", "J.B. Chemicals & Pharmaceuticals Ltd.", "JBM Auto Ltd.", "JK Lakshmi Cement Ltd.", "JK Tyre & Industries Ltd.", "JM Financial Ltd.", "Jaiprakash Power Ventures Ltd.", "Jammu & Kashmir Bank Ltd.", "Jindal Saw Ltd.", "Jubilant Ingrevia Ltd.", "Jubilant Pharmova Ltd.", "Jupiter Wagons Ltd.", "Justdial Ltd.", "Jyothy Labs Ltd.", "Jyoti CNC Automation Ltd.", "KNR Constructions Ltd.", "KSB Ltd.", "Kajaria Ceramics Ltd.", "Kalpataru Projects International Ltd.", "Kansai Nerolac Paints Ltd.", "Karur Vysya Bank Ltd.", "Kaynes Technology India Ltd.", "Kec International Ltd.", "Kfin Technologies Ltd.", "Kirloskar Brothers Ltd.", "Kirloskar Oil Eng Ltd.", "Krishna Institute of Medical Sciences Ltd.", "Latent View Analytics Ltd.", "Laurus Labs Ltd.", "Lemon Tree Hotels Ltd.", "MMTC Ltd.", "Mahanagar Gas Ltd.", "Maharashtra Seamless Ltd.", "Mahindra Lifespace Developers Ltd.", "Manappuram Finance Ltd.", "Mastek Ltd.", "Metropolis Healthcare Ltd.", "Minda Corporation Ltd.", "Motilal Oswal Financial Services Ltd.", "Multi Commodity Exchange of India Ltd.", "NATCO Pharma Ltd.", "NBCC (India) Ltd.", "NCC Ltd.", "NMDC Steel Ltd.", "Narayana Hrudayalaya Ltd.", "National Aluminium Co. Ltd.", "Navin Fluorine International Ltd.", "Netweb Technologies India Ltd.", "Network18 Media & Investments Ltd.", "Newgen Software Technologies Ltd.", "Nuvama Wealth Management Ltd.", "Nuvoco Vistas Corporation Ltd.", "Olectra Greentech Ltd.", "PCBL Ltd.", "PNB Housing Finance Ltd.", "PNC Infratech Ltd.", "PTC Industries Ltd.", "PVR INOX Ltd.", "Pfizer Ltd.", "Piramal Enterprises Ltd.", "Piramal Pharma Ltd.", "Poly Medicure Ltd.", "Praj Industries Ltd.", "Quess Corp Ltd.", "R R Kabel Ltd.", "RBL Bank Ltd.", "RHI MAGNESITA INDIA LTD.", "RITES Ltd.", "Radico Khaitan Ltd", "Railtel Corporation Of India Ltd.", "Rainbow Childrens Medicare Ltd.", "Rajesh Exports Ltd.", "Ramkrishna Forgings Ltd.", "Rashtriya Chemicals & Fertilizers Ltd.", "Ratnamani Metals & Tubes Ltd.", "RattanIndia Enterprises Ltd.", "Raymond Ltd.", "Redington Ltd.", "Route Mobile Ltd.", "SBFC Finance Ltd.", "Sammaan Capital Ltd.", "Sanofi India Ltd.", "Sapphire Foods India Ltd.", "Saregama India Ltd", "Schneider Electric Infrastructure Ltd.", "Shipping Corporation of India Ltd.", "Shree Renuka Sugars Ltd.", "Shyam Metalics and Energy Ltd.", "Signatureglobal (India) Ltd.", "Sobha Ltd.", "Sonata Software Ltd.", "Sterling and Wilson Renewable Energy Ltd.", "Sumitomo Chemical India Ltd.", "Sun Pharma Advanced Research Company Ltd.", "Suven Pharmaceuticals Ltd.", "Swan Energy Ltd.", "Syrma SGS Technology Ltd.", "TBO Tek Ltd.", "TVS Supply Chain Solutions Ltd.", "Tanla Platforms Ltd.", "Tata Teleservices (Maharashtra) Ltd.", "Techno Electric & Engineering Company Ltd.", "Tejas Networks Ltd.", "The Ramco Cements Ltd.", "Titagarh Rail Systems Ltd.", "Trident Ltd.", "Triveni Engineering & Industries Ltd.", "Triveni Turbine Ltd.", "UCO Bank", "UTI Asset Management Company Ltd.", "Ujjivan Small Finance Bank Ltd.", "Usha Martin Ltd.", "V-Guard Industries Ltd.", "V.I.P. Industries Ltd.", "Valor Estate Ltd.", "Vardhman Textiles Ltd.", "Varroc Engineering Ltd.", "Vedant Fashions Ltd.", "Vijaya Diagnostic Centre Ltd.", "Vinati Organics Ltd.", "Welspun Corp Ltd.", "Welspun Living Ltd.", "Westlife Foodworld Ltd.", "Whirlpool of India Ltd.", "Zee Entertainment Enterprises Ltd.", "Zensar Technolgies Ltd.", "eClerx Services Ltd."]
tickers250="360ONE AADHARHFC AARTIIND AAVAS ACE ABREL ABSLAMC AEGISLOG AFFLE AKUMS APLLTD ALKYLAMINE ALOKINDS ARE&M AMBER ANANDRATHI ANANTRAJ ANGELONE APARINDS APTUS ACI ASAHIINDIA ASTERDM ASTRAZEN ATUL AVANTIFEED BASF BEML BLS BALAMINES BALRAMCHIN BATAINDIA BIKAJI BIRLACORPN BSOFT BLUEDART BLUESTARCO BBTC BRIGADE MAPMYINDIA CCL CESC CIEINDIA CAMPUS CANFINHOME CAPLIPOINT CGCL CASTROLIND CEATLTD CELLO CENTRALBK CDSL CENTURYPLY CERA CHALET CHAMBLFERT CHEMPLASTS CHENNPETRO CHOLAHLDNG CUB CLEAN CAMS CONCORDBIO CRAFTSMAN CREDITACC CROMPTON CYIENT DOMS DATAPATTNS DEEPAKFERT DEVYANI LALPATHLAB EIDPARRY EIHOTEL EASEMYTRIP ELECON ELGIEQUIP EMCURE ENGINERSIN EQUITASBNK ERIS FINEORG FINCABLES FINPIPE FSL FIVESTAR GRINFRA GVT&D GRSE GILLETTE GLENMARK GODIGIT GPIL GODFRYPHLP GODREJAGRO GRANULES GRAPHITE GESHIP GAEL GMDCLTD GNFC GPPL GSFC GSPL HEG HBLPOWER HFCL HAPPSTMNDS HSCL HINDCOPPER HOMEFIRST HONASA ISEC IFCI IIFL INOXINDIA IRCON ITI INDGN INDIACEM INDIAMART IEX INOXWIND INTELLECT JBCHEPHARM JBMA JKLAKSHMI JKTYRE JMFINANCIL JPPOWER J&KBANK JINDALSAW JUBLINGREA JUBLPHARMA JWL JUSTDIAL JYOTHYLAB JYOTICNC KNRCON KSB KAJARIACER KPIL KANSAINER KARURVYSYA KAYNES KEC KFINTECH KIRLOSBROS KIRLOSENG KIMS LATENTVIEW LAURUSLABS LEMONTREE MMTC MGL MAHSEAMLES MAHLIFE MANAPPURAM MASTEK METROPOLIS MINDACORP MOTILALOFS MCX NATCOPHARM NBCC NCC NSLNISP NH NATIONALUM NAVINFLUOR NETWEB NETWORK18 NEWGEN NUVAMA NUVOCO OLECTRA PCBL PNBHOUSING PNCINFRA PTCIL PVRINOX PFIZER PEL PPLPHARMA POLYMED PRAJIND QUESS RRKABEL RBLBANK RHIM RITES RADICO RAILTEL RAINBOW RAJESHEXPO RKFORGE RCF RATNAMANI RTNINDIA RAYMOND REDINGTON ROUTE SBFC SAMMAANCAP SANOFI SAPPHIRE SAREGAMA SCHNEIDER SCI RENUKA SHYAMMETL SIGNATURE SOBHA SONATSOFTW SWSOLAR SUMICHEM SPARC SUVENPHAR SWANENERGY SYRMA TBOTEK TVSSCS TANLA TTML TECHNOE TEJASNET RAMCOCEM TITAGARH TRIDENT TRIVENI TRITURBINE UCOBANK UTIAMC UJJIVANSFB USHAMART VGUARD VIPIND DBREALTY VTL VARROC MANYAVAR VIJAYA VINATIORGA WELCORP WELSPUNLIV WESTLIFE WHIRLPOOL ZEEL ZENSARTECH ECLERX"

for ticker in tickers100.split():
    # Download historical data for the past year
    ticker+='.NS'
    data = yf.download(ticker, period="1y")

    if data.empty:
        print(f"No data found for {ticker}. Please check the ticker symbol.")
        results.append([names100,0,0,0])
    else:
        # Calculate the 52-week high
        high_52wk = data['High'].max()  # This is a scalar value

        # Get the latest closing price
        present_price = data['Close'].iloc[-1]  # This is a scalar value

        # Calculate the discount percentage from the 52-week high
        discount_pct = ((high_52wk - present_price) / high_52wk) * 100

        # Calculate the 14-day RSI
        rsi = calculate_rsi(data['Close'])
        rsi_14 = rsi.iloc[-1]  # Extract the latest RSI value as a scalar

        # Display the results
        print(ticker,cnt/1)
        gcnt+=1
        print(gcnt/5,"%",sep="")
        
        results.append([names100[cnt],round(list(high_52wk)[0],2),round(list(present_price)[0],2),round(list(discount_pct)[0],2),round(list(rsi_14)[0],2)])
        cnt+=1
results.append(["nifty 150","nifty 150","nifty 150","nifty 150","nifty 150"])



cnt=0
for ticker in tickers150.split():
    # Download historical data for the past year
    ticker+='.NS'
    data = yf.download(ticker, period="1y")

    if data.empty:
        print(f"No data found for {ticker}. Please check the ticker symbol.")
        results.append([names150[cnt],0,0,0])
    else:
        # Calculate the 52-week high
        high_52wk = data['High'].max()  # This is a scalar value

        # Get the latest closing price
        present_price = data['Close'].iloc[-1]  # This is a scalar value

        # Calculate the discount percentage from the 52-week high
        discount_pct = ((high_52wk - present_price) / high_52wk) * 100

        # Calculate the 14-day RSI
        rsi = calculate_rsi(data['Close'])
        rsi_14 = rsi.iloc[-1]  # Extract the latest RSI value as a scalar

        # Display the results
        print(ticker,cnt/1.5)
        gcnt+=1
        print(gcnt/5,"%",sep="")
        results.append([names150[cnt],round(list(high_52wk)[0],2),round(list(present_price)[0],2),round(list(discount_pct)[0],2),round(list(rsi_14)[0],2)])
        cnt+=1

results.append(["nifty250","nifty250","nifty250","nifty250","nifty250"])


cnt=0
for ticker in tickers250.split():
    # Download historical data for the past year
    ticker+='.NS'
    data = yf.download(ticker, period="1y")

    if data.empty:
        print(f"No data found for {ticker}. Please check the ticker symbol.")
        results.append([names250,0,0,0])
    else:
        # Calculate the 52-week high
        high_52wk = data['High'].max()  # This is a scalar value

        # Get the latest closing price
        present_price = data['Close'].iloc[-1]  # This is a scalar value

        # Calculate the discount percentage from the 52-week high
        discount_pct = ((high_52wk - present_price) / high_52wk) * 100

        # Calculate the 14-day RSI
        rsi = calculate_rsi(data['Close'])
        rsi_14 = rsi.iloc[-1]  # Extract the latest RSI value as a scalar

        # Display the results
        print(ticker,cnt/2.5)
        gcnt+=1
        print(gcnt/5,"%",sep="")
        results.append([names250[cnt],round(list(high_52wk)[0],2),round(list(present_price)[0],2),round(list(discount_pct)[0],2),round(list(rsi_14)[0],2)])
        cnt+=1
dff = pd.DataFrame(results, columns=["Name", "52-Week High", "Present Price", "Discount %","14-Day RSI"])
dff.to_excel("sharemaket.xlsx", index=False)
print("Results have been saved to 'sharemaket.xlsx'")



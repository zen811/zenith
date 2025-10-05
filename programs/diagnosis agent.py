from data_analysis_agent import Engine_Condition_Checker as ecc
import pandas as pd
rpm = int(input('Engine rpm'))
oil_p = int(input('Lub oil pressure'))
fuel_p = int(input('Fuel pressure'))
coolant_p = int(input('Coolant pressure'))
oil_t = int(input('lub oil temp'))
coolant_t = int(input('Coolant temp'))


User_data={'Engine rpm': [rpm],
                'Lub oil pressure': [oil_p],
    'Fuel pressure': [fuel_p],
    'Coolant pressure': [coolant_p],
    'lub oil temp': [oil_t],
    'Coolant temp': [coolant_t]}
User_df=pd.DataFrame(User_data)

Engine_Condition=ecc(User_df)

if Engine_Condition==0:
    print("very good engine")
if Engine_Condition==1:
    print("The engine is overheating check coolant level or visit the nearest service centre")
    #function to book a servcie
if Engine_Condition==2:
    print("you probbaly have a oil leak do not drive the vehicle get it towed")
    #function to get towing vehicle
if Engine_Condition==3:
    print("engine is misfiring do not turn it on and call a mechanic or get it towed")
    #function to get towing vehicle
if Engine_Condition==4:
    print("Your Engine is Exhibiting Poor performance please visit the nearest service centre")
    #function to book a service



    
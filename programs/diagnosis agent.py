from data_analysis_agent import Engine_Condition_Checker as ecc
import pandas as pd
import traceback


print("Program started successfully ✅")

from programs.data_analysis_agent import Engine_Condition_Checker as ecc
import pandas as pd

rpm = float(input('Engine rpm: '))
oil_p = float(input('Lub oil pressure: '))
fuel_p = float(input('Fuel pressure: '))
coolant_p = float(input('Coolant pressure: '))
oil_t = float(input('Lub oil temp: '))
coolant_t = float(input('Coolant temp: '))

User_data = {
    'Engine rpm': [rpm],
    'Lub oil pressure': [oil_p],
    'Fuel pressure': [fuel_p],
    'Coolant pressure': [coolant_p],
    'lub oil temp': [oil_t],
    'Coolant temp': [coolant_t]
    }

User_df = pd.DataFrame(User_data)
print("\nData captured successfully ✅")

Engine_Condition = ecc(User_df)
print(f"Engine condition result: {Engine_Condition}")

if Engine_Condition == 0:
        print("Very good engine")
elif Engine_Condition == 1:
        print("The engine is overheating. Check coolant level or visit the nearest service centre.")
elif Engine_Condition == 2:
        print("You probably have an oil leak. Do not drive the vehicle — get it towed.")
elif Engine_Condition == 3:
        print("Engine is misfiring. Do not turn it on — call a mechanic or get it towed.")
elif Engine_Condition == 4:
        print("Your engine is exhibiting poor performance. Please visit the nearest service centre.")


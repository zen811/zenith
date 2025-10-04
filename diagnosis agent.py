rpm = input('Engine rpm')
oil_p = input('Lub oil pressure')
fuel_p = input('Fuel pressure')
coolant_p = input('Coolant pressure')
oil_t = input('lub oil temp')
coolant_t = input('Coolant temp')

#compare to  the actual ai model data

#recommend visitation to the service centre 
#Engine_condition=function()
if Engine_condition==0:
    print("very good engine")
if Engine_condition==1:
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
    
    

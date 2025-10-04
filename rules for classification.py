''' data manipulation '''

def classify_engine(row):
    rpm = row['Engine rpm']
    oil_p = row['Lub oil pressure']
    fuel_p = row['Fuel pressure']
    coolant_p = row['Coolant pressure']
    oil_t = row['lub oil temp']
    coolant_t = row['Coolant temp']
    
    # Rule 1: Engine heating 
    if coolant_t > 100 or oil_t > 110:
        return 1
    
    # Rule 2: Oil leak 
    if (rpm < 1000 and oil_p < 1) or (rpm >= 1000 and oil_p < 2):
        return 2
    
    # Rule 3: Engine misfiring 
    if (fuel_p < 2 or fuel_p > 5) and (rpm < 900 or rpm > 3000):
        return 3
    
    # Rule 4: Poor performance 
    # Trigger only if temps are slightly off, but not high enough for heating or misfiring
    if (95 <= coolant_t <= 100 or 105 < coolant_t <= 110) or (100 <= oil_t <= 110 or 115 < oil_t <= 120):
        return 4
    
    # Rule 0: Good engine 


from datetime import datetime, timedelta 
  
updated = ( datetime.now() +
           timedelta( hours=5 )).strftime('%H:%M:%S') 
  
print( updated )
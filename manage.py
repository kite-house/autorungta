import pyuac
from main import main
import time

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin() 

else:
    timeout = int(input("Через сколько запускаем гта?(В секундах): "))
    time.sleep(timeout)
    main()
    
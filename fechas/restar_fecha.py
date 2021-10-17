"""
Manejo basico para la resta entre fechas
"""

from datetime import datetime
from datetime import timedelta

ahora = datetime.now()
print("Ahora: " + str(ahora))
hace_una_semana = ahora - timedelta(days=7)
print("Hace una semana: " + str(hace_una_semana))
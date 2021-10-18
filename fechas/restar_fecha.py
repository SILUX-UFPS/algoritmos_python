"""
Manejo basico para la resta entre fechas
"""

from datetime import datetime
from datetime import timedelta

ahora = datetime.now()
print("Ahora: " + str(ahora))
hace_una_semana = ahora - timedelta(days=7)
print("Hace una semana: " + str(hace_una_semana))
hace_una_semana_formateada = hace_una_semana.strftime("%Y-%m-%d")
print("Hace una semana, solo fecha: " + hace_una_semana_formateada)
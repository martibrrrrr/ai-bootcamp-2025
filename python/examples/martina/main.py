from python.examples.martina.constants import PI
from python.examples.martina.functions import foo

print(PI)
print(foo)

#se importo il mudulo
import martina
print(martina.functions.foo())
#from .. main (vado nella cartella precedente)
#from martina.constants import PI (se constants è nella sotto cartella Martina)
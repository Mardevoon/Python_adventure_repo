#Este código faz uma contagem recressiva para os fogos de artifício estourarem
from time import sleep

for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print("BUM! BUUM! POOW!")
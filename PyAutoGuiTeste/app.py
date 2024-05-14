import pyautogui
import time

print(pyautogui.size())
print(pyautogui.position())

#size da tela 1920x1080
#funções de mouse
#clicar metodo.click,  o sleep serve pra dar um tempo entre uma ação e outra

#  time.sleep(1)
#  pyautogui.click(x=1114, y=15)
#  time.sleep(1)
#  pyautogui.click(x=1242, y=13)
#  time.sleep(1)
#  pyautogui.click(x=1359, y=16)

#pra pegar as posições, seto um tempo de sleep pra rodar um print em pyautogui.position() que ele vai printar no console a posição
#da pra passar o botão do mouse que é clicado, e a quantidade de cliques, intervalo de cliques, é possível também usar o scroll do mouse prop middle
#arrastar o mouse || da pra passar modificações

# pyautogui.moveTo(x=1351, y=152)
pyautogui.moveTo(x=1351, y=152, duration=1)


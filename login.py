import win32gui
import pyautogui as pag

#Тут необходимо ввести свои логин и пароь от рума
EMAIL = 'nickname@gmail.com'
PASS = 'password'

'''
Некоторые настройки подробности по ссылке ниже
https://automatetheboringstuff.com/chapter18/
Pauses and Fail-Safes
'''
pag.PAUSE = 2 
pag.FAILSAFE = True


#Находим окно по названию
hwnd = win32gui.FindWindow(None, r'Virtue Poker Beta')

if hwnd != 0:
    #На всякий случай делаем его поверх всех окон
    win32gui.SetForegroundWindow(hwnd)
    #Определяем верхний левый угол ширину и высоту окна
    x,y,w,h = win32gui.GetWindowRect(hwnd)

    #Теперь нужно кликнуть по координатам кнопки Login
    pag.click(x+280, y+390)

    '''
    По умолчанию курсор уже в поле Email,
    но мы на всякий случай кликнем еще раз,
    заполним форму и кликаем Login
    '''
    pag.click(x+378, y+362)
    pag.typewrite(EMAIL, 0.25)

    pag.click(x+378, y+442)
    pag.typewrite(PASSWORD, 0.25)

    #pag.moveTo(x+500, y+520)
    pag.click(x+500, y+520)
    
else:
    print('Клиент не запущен!')

import PySimpleGUI as sg
from functions import Juros_Simples
from functions import Juros_Compostos
# Tema da Janela
sg.theme('DarkAmber')

# Layout
layout = [
            [sg.Text('Juros'), sg.Listbox(('Simples', 'Composto'), size=(10, 2), key='jur'), sg.Text('', text_color='red',key='erro')],
            [sg.Text("OBS: As grandezas de Taxa de Juros e Tempo devem ser iguais. EX:\n30%.ao mês\nPor 3 meses")],
            [sg.Text('Capital Incial(R$):', (13, 1)), sg.Input('1200.00', (7, 1), key='c'), sg.Text('', key='cerro',text_color='red')],
            [sg.Text('Taxa de Juros:', (13, 1)), sg.Input('10', (3, 1), key='i'), sg.Text("%"), sg.Text('', key='ierro',text_color='red')],
            [sg.Text('Tempo:', (13, 1)), sg.Input('15', (4, 1), key='t'), sg.Text('', key='terro', text_color='red')],
            [sg.Button('Calcular'), sg.Text('Juros: ', key='juros'), sg.Text('Montante: ', key='M')]
        ]
        
# Janela
janela = sg.Window("Calculadora de Juros", layout)

# Informações da Janela
while True:
    event, values = janela.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Calcular':
        
        try:
            c = float(values['c'])
            janela['cerro'].update('')
        except ValueError:
            janela['cerro'].update('Insira um valor válido.')
        
        try:
            i = int(values['i'])
            janela['ierro'].update('')
        except ValueError:
            janela['ierro'].update('Insira um valor válido.')
        
        try:
            t = int(values['t'])
            janela['terro'].update('')
        except ValueError:
            janela['terro'].update('Insira um valor válido.')
        
        try:
            janela['erro'].update('')
            if(values['jur'][0] == 'Simples'):   
                js = Juros_Simples(c, i, t)
                j = js.calcular()
                m = j + c
                janela['juros'].update(f'Juros: R${j:.2f}')
                janela['M'].update(f'Montante: R${m:.2f}')

            elif(values['jur'][0] == 'Composto'):
                jc = Juros_Compostos(c, i, t)
                j, m = jc.calcular()
                janela['juros'].update(f'Juros: R${j:.2f}')
                janela['M'].update(f'Montante: R${m:.2f}')
        except IndexError:
            janela['erro'].update('Por favor selecione uma opção.')

# Fechar janela
janela.close()

# CÓDIGO DE WELLINGTON LUIZ DE FARIA --> GitHub: https://github.com/WellingtonLFaria ✌
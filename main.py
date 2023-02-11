import openai
import PySimpleGUI as sg
import pyperclip

# Adicione sua chave de API aqui
openai.api_key = "SUA API"

# Defina o modelo a ser usado
model_engine = "text-davinci-003"

def determinador_qualidade_sing_fem(criativo, detalhado, humanizado, sensacionalista, prefix):
    if criativo == True and detalhado == False and humanizado == False and sensacionalista == False:
        prefix += " criativa"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == False:
        prefix += " detalhada"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == False:
        prefix += " criativa e detalhada"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " criativa, detalhada e humanizada"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " humanizada"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " criativa e humanizada"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " detalhada e humanizada"
    elif criativo == True and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " criativa e sensacionalista"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == True:
        prefix += " detalhada e sensacionalista"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == True:
        prefix += " criativa, detalhada e sensacionalista"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " criativa, detalhada, humanizada  e sensacionalista"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " humanizada e sensacionalista"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " criativa, humanizada e sensacionalista"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " detalhada, humanizada e sensacionalista"
    elif criativo == False and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " sensacionalista"
    global prompt
    prompt = (f'{prefix}')

def determinador_qualidade_plu_fem(criativo, detalhado, humanizado, sensacionalista, prefix):
    if criativo == True and detalhado == False and humanizado == False and sensacionalista == False:
        prefix += " criativas"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == False:
        prefix += " detalhadas"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == False:
        prefix += " criativas e detalhadas"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " criativas, detalhadas e humanizadas"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " humanizadas"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " criativas e humanizadas"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " detalhadas e humanizadas"
    elif criativo == True and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " criativas e sensacionalistas"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == True:
        prefix += " detalhadas e sensacionalistas"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == True:
        prefix += " criativas, detalhadas e sensacionalistas"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " criativas, detalhadas, humanizadas e sensacionalistas"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " humanizadas e sensacionalistas"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " criativas, humanizadas e sensacionalistas"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " detalhadas, humanizadas e sensacionalistas"
    elif criativo == False and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " sensacionalistas"
    global prompt
    prompt = (f'{prefix}')

def determinador_qualidade_sing_masc(criativo, detalhado, humanizado, sensacionalista,prefix):
    if criativo == True and detalhado == False and humanizado == False and sensacionalista == False:
        prefix += " criativo"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == False:
        prefix += " detalhado"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == False:
        prefix += " criativo e detalhado"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " criativo, detalhado e humanizado"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " humanizado"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " criativo e humanizado"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " detalhado e humanizado"
    elif criativo == True and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " criativo e sensacionalista"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == True:
        prefix += " detalhado e sensacionalista"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == True:
        prefix += " criativo, detalhado e sensacionalista"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " criativo, detalhado, humanizado  e sensacionalista"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " humanizado e sensacionalista"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " criativo, humanizado e sensacionalista"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " detalhado, humanizado e sensacionalista"
    elif criativo == False and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " sensacionalista"
    global prompt
    prompt = (f'{prefix}')

def determinador_qualidade_plu_masc(criativo, detalhado, humanizado, sensacionalista,prefix):
    if criativo == True and detalhado == False and humanizado == False and sensacionalista == False:
        prefix += " criativos"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == False:
        prefix += " detalhados"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == False:
        prefix += " criativos e detalhados"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " criativos, detalhados e humanizados"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " humanizados"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == False:
        prefix += " criativos e humanizados"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == False:
        prefix += " detalhados e humanizados"
    elif criativo == True and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " criativos e sensacionalistas"
    elif detalhado == True and criativo == False and humanizado == False and sensacionalista == True:
        prefix += " detalhados e sensacionalistas"
    elif criativo == True and detalhado == True and humanizado == False and sensacionalista == True:
        prefix += " criativos, detalhados e sensacionalistas"
    elif criativo == True and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " criativos, detalhados, humanizados  e sensacionalistas"
    elif criativo == False and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " humanizados e sensacionalistas"
    elif criativo == True and detalhado == False and humanizado == True and sensacionalista == True:
        prefix += " criativos, humanizados e sensacionalistas"
    elif criativo == False and detalhado == True and humanizado == True and sensacionalista == True:
        prefix += " detalhados, humanizados e sensacionalistas"
    elif criativo == False and detalhado == False and humanizado == False and sensacionalista == True:
        prefix += " sensacionalistas"
    global prompt
    prompt = (f'{prefix}')

def buscar(prompt):
    global res
    try:
        response = openai.Completion.create(
        engine=model_engine,
        prompt= prompt,
        max_tokens=1024,
        temperature=0.6
        )
        res = response['choices'][0]['text']
        values['Output1'] = print(f'Prompt: {prompt}.')
        values['Output1'] = print(res)
    except:
        response = openai.Completion.create(
        engine=model_engine,
        prompt= prompt,
        max_tokens=1024,
        temperature=0.6
        )
        res = response['choices'][0]['text']
        values['Output1'] = print(f'Prompt: {prompt}.')
        values['Output1'] = print(res)

def main():
    sg.theme("Dark Blue")

    layout = [
              [sg.Text('GERADOR DE PLR')],
              [sg.Output(size=(75,15), key='Output', text_color='white')],
              [sg.Text('Modos:'), sg.Checkbox("Criativo", key="criativo"),
                sg.Checkbox("Detalhado", key="detalhado"),
                sg.Checkbox("Humanizado", key="humanizado"),
                sg.Checkbox("Sensacionalista", key="sensacionalista")],
              [sg.Button('Copiar ultima saida'), sg.Button('Limpar prompt')],
              [sg.Combo(values=['Gerar ideias de livro sobre:',
                                'Gerar introdução de um livro sobre:',
                                'Gerar capítulos de um livro sobre:',
                                'Gerar tópicos de um livro sobre:',
                                'Gerar conteúdo de um tópico sobre:',
                                'Crie um artigo sobre:',
                                'Crie um poema sobre:',
                                ],
                                size=(30, 1), default_value='Gerar ideias de livro sobre:', key='opcoes', readonly=True),
                                sg.Input(key='prompt', text_color='white', size=20), sg.Button('Enviar')],
             ]
    
    return sg.Window('Gerador de PLR', layout, finalize=True, resizable=True)

window = main()

window.Element('Output').Update(disabled=True) # torna o output não editavel

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        criativo = values['criativo']
        detalhado = values['detalhado']
        humanizado = values['humanizado']
        sensacionalista = values['sensacionalista']
        opcoes = values['opcoes'] #opcoes de gerador
        
        if opcoes == 'Gerar ideias de livro sobre:':
            prefix = "Gere ideias"
            determinador_qualidade_plu_fem(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} de um livro sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Gerar introdução de um livro sobre:':
            prefix = "Gere uma introdução"
            determinador_qualidade_sing_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} de um livro sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Gerar capítulos de um livro sobre:':
            prefix = "Gere capítulos"
            determinador_qualidade_plu_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} de um livro sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Gerar tópicos de um livro sobre:':
            prefix = "Gere tópicos"
            determinador_qualidade_plu_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} de um livro sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Crie um artigo sobre:':
            prefix = "Crie um artigo"
            determinador_qualidade_sing_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Crie um poema sobre:':
            prefix = "Crie um poema"
            determinador_qualidade_sing_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} sobre {values["prompt"]}')
            buscar(prompt)

        elif opcoes == 'Gerar conteúdo de um tópico sobre:':
            prefix = "Gere um texto"
            determinador_qualidade_sing_masc(criativo, detalhado, humanizado, sensacionalista,prefix)
            prompt = (f'{prompt} sobre um tópico intitulado {values["prompt"]}')
            buscar(prompt)
        
    elif event == 'Copiar ultima saida':
        pyperclip.copy(res)

    elif event == 'Limpar prompt':
        window.FindElement('Output').Update('')

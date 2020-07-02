from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

bot = ChatBot('Test2')
# bot.storage.drop()


# ===== VARIAVEIS =====
perguntaAtual = 1
responseGlobal = ""
helloStatus = False
pergCidade = False

resp1 = False
resp2 = False
resp3 = False
# =====================


# -------------------------- FUNCAO ERRO DE ENTENDIMENTO --------------------------

def erroEntendimento():
    print('Saúde Bot: Desculpe, não entendi. Responda novamente')


# ----------------------------- FUNCAO RESULTADO FINAL -----------------------------

def resultadoFinal(pergCidade):

    text = ""

    # RESPOSTA2
    if(resp2 == True):

        # RESPOSTA3
        if(resp3 == True):
            pergCidade = True
            text = ("\n Em caso de falta de ar é aconselhado procurar tratamento médico e aumentar o isolamento. \n"
                    "Informe a sua cidade para saber onde tem um hospital que você possa ir. \n"
                    "Para maiores informações sobre o Covid-19, acesse o link:  https://datastudio.google.com/u/0/reporting/5b72d54e-a0c2-4748-acf0-9688f42278aa/page/spmIB")

        else:
            text = ("\n Em casos de sintomas leves é aconselhado aumentar o nivel de isolamento \n"
                    "mas não é necessário procurar atendimento médico. Só procure atendimento se apresentar falta de ar. ")

            if(resp1 == True):
                text = text + ("\n Por ter tido contato com alguém que testou positivo, redobre os cuidados \n"
                               " e fique um periodo em total isolamento para garantir que não foi contaminado. \n"
                               "Para maiores informações sobre o Covid-19, acesse o link:  https://datastudio.google.com/u/0/reporting/5b72d54e-a0c2-4748-acf0-9688f42278aa/page/spmIB")

    else:

        if(resp1 == True):
            text = ("\n Por não estar apresentando sintomas, são menores as chances de você estar contaminado. \n"
                    "Por isso não há necessidade de procurar um atendimento medico, apenas continue seguindo as medidas de isolamento e cuidados de prevenção. \n"
                    "Por ter tido contato com alguem que testou positivo, redobre os cuidados e aumente a intensidade do isolamento por alguns dias. \n"
                    "Para maiores informações sobre o Covid-19, acesse o link:  https://datastudio.google.com/u/0/reporting/5b72d54e-a0c2-4748-acf0-9688f42278aa/page/spmIB")
        else:
            text = ("\n Por não estar apresentando sintomas e por não ter tido contato com \n "
                    "alguem que teve resultado confirmado, são menores as chances de você estar contaminado. \n"
                    "Por isso não há necessidade de procurar um atendimento medico, apenas continue seguindo as medidas de isolamento e cuidados de prevenção. \n"
                    "Para maiores informações sobre o Covid-19, acesse o link:  https://datastudio.google.com/u/0/reporting/5b72d54e-a0c2-4748-acf0-9688f42278aa/page/spmIB")

    print(text)


# ---------------------------------------- ARRAYS ----------------------------------------

convConfirm = ['sim', 'true',
               'tive sim', 'true',
               'tive', 'true',
               'não', 'false',
               'nao', 'false',
               'tive nao', 'false',
               'tive não', 'false',
               'que eu saiba não', 'false',
               ]

convCidade = ['Ribeirão Preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'Ribeirao Preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'ribeirão preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'ribeirao preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'Ribeirão-Preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'Ribeirao-Preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'ribeirão-preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              'ribeirao-preto',
              'Você pode ir até o UPA da avenida 13 de maio, onde foi montada uma estrutura adicional para receber pacientes do Corona Virus',
              ]


trainer = ListTrainer(bot)
trainer.train(convConfirm)
trainer.train(convCidade)


while True:

    # ------------------------- pergunta 1 -------------------------

    if(perguntaAtual == 1):

        if(helloStatus == False):
            print("\n Ola, vou dar recomendações de como agir em diferentes situações relacionadas ao Corona Virus. Vamos começar?")

            quest = input(
                '\n Você recentemente teve contato com alguém que testou positivo para o Corona Virus? \n')
            response = bot.get_response(quest)

            helloStatus = True

        else:
            quest = input()
            response = bot.get_response(quest)

        if float(response.confidence) > 0.03:
            if (response.text == 'true'):
                resp1 = True
                perguntaAtual = 2
            else:
                resp1 = False
                perguntaAtual = 2

        else:
            erroEntendimento()

    # ------------------------- pergunta 2 -------------------------

    if(perguntaAtual == 2):

        quest = input(
            ' \n Você esta apresentando sintomas? \n')
        response = bot.get_response(quest)

        if float(response.confidence) > 0.03:
            if (response.text == 'true'):
                resp2 = True
                perguntaAtual = 3
            else:
                resp2 = False
                perguntaAtual = 0
                resultadoFinal(pergCidade)

        else:
            erroEntendimento()

    # ------------------------- pergunta 3 -------------------------

    if(perguntaAtual == 3):

        if(pergCidade == False):

            quest = input(
                '\n Dentre os sintomas você esta sentindo falta de ar? \n')
            response = bot.get_response(quest)

            if float(response.confidence) > 0.03:
                if (response.text == 'true'):
                    resp3 = True
                    pergCidade = True
                    resultadoFinal(pergCidade)
                else:
                    resp3 = False
                    perguntaAtual = 0
                    resultadoFinal(pergCidade)

            else:
                erroEntendimento()
        else:
            quest = input(
                'Sua cidade: ')
            response = bot.get_response(quest)
            if float(response.confidence) > 0.03:
                print(response)
                time.sleep(10)
                break
            else:
                erroEntendimento()

'''
    Funções para Auxiliar o código principal (kmp_princial): kmp_codigo.py

    Criado por: Gabriela Villani Moreira - RA: 181884 || 23/02/2023
    Alteração: Gabriela Villani Moreira - RA: 181884  || 30/02/2023 
    Alteração: Lucas Souza Frade - Ra: 181370         || 02/03/2023
    Alteração: Lucas Souza Frade - Ra: 181370         || 16/03/2023
    Alteração: Gabriela Villani Moreira - RA: 181884  || 13/04/2023 
    Alteração: Lucas Souza Frade - Ra: 181370         || 04/05/2023
'''


from tkinter import *
from tkinter import messagebox
import kmp_codigo as KMP

# Lucas Frade - 16/03/2023 || Função para Limpar Formulário
def LimparFormulario():
    txtSubSequencia.delete(0,END)
    txtSequenciaDNA.delete(1.0, END)
    txtResultado.config(state = NORMAL)
    txtResultado.delete(1.0, END)
    txtResultado.config(state = DISABLED)
    lblIndex['text'] = 'Index: '
    lblCompKMP['text'] = ''
    lblCompBasica['text'] = ''

# Lucas Frade - 02/03/2023 || Função para o Botão Resultado
def EventoBtnResultadoOnClick():
    # Limpando Resultado Anterior
    txtResultado.config(state = NORMAL)
    txtResultado.delete(1.0, END)
    vPosicoes = [] 
    vComparacaoBasica = 0
    vComparacaoKMP = 0

    vSequenciaDNA = txtSequenciaDNA.get(1.0, END)
    vSubsequencia = txtSubSequencia.get()

    # Gabriela Villani - 13/04/2023 || Adicionando mensagem para preencher campos
    if vSequenciaDNA.strip() == '' or vSubsequencia.strip() == '':
        vTitulo = 'Falta de Informação'
        vMensagem = 'Verifique se todos os campos estão preenchidos!!'
        messagebox.showwarning(title = vTitulo, message = vMensagem)
        return 0
    
    else:
        vPosicoes, vComparacaoBasica, vComparacaoKMP = KMP.BuscarSubsequencia(vSequenciaDNA, vSubsequencia)

        # Transformando Lista Inteiros para Str
        vPosicoesListaStr = [str(p) for p in vPosicoes]
        vSubstrings = []

        while vPosicoesListaStr:

            # Gabriela Villani - 13/04/2023 || Limitando para 12 elementos por linha
            vSubstrings.append(', '.join(vPosicoesListaStr[:12]))
            vPosicoesListaStr = vPosicoesListaStr[12:]
        
        txtResultado.insert(1.0, '\n'.join(vSubstrings))
        txtResultado.config(state = DISABLED)
        
        lblCompBasica['text'] = 'Comparação básica: \n' + str(vComparacaoBasica)
        lblCompKMP['text'] = 'Comparação KMP: \n' + str(vComparacaoKMP)
        lblIndex['text'] = 'Index [' + txtSubSequencia.get() + ']:'

    if txtResultado.get(1.0, END).strip() == '':
        lblCompKMP['text'] = ''
        lblCompBasica['text'] = ''
        vTitulo = 'Sem Index'
        vMensagem = 'Não foi possível encontrar nenhum index para sua Sequencia!!'
        messagebox.showwarning(title = vTitulo, message = vMensagem)


def EventoBtnInformacoesOnClick():
    messagebox.showinfo(title = 'Instruções', message = '- Para o funcionamento do programa faça: \n'  
                        +'• Preencha o Campo "Sequência de DNA" com a cadeia que pretende percorrer. \n'
                        +'• Preencha o Campo "Subsequência" com a sub-cadeia que pretende achar dentro da cadeia principal.\n'
                        +'• Em seguida clique no botão "Resultado" para ele fazer a procura. \n'
                        +'• Logo após, o resultado irá aparecer no Campo "Index".')

# Gabriela Villani - 23/02/2023 || Criando Formulário
Formulario = Tk()

# Criando Componentes da Tela(Formulario)

## Labels
lblSequenciaDNA = Label(Formulario, text = 'Sequência de DNA: ', font = 'Arial 15')
lblSubsequencia = Label(Formulario, text = 'Subsequência: ', font = 'Arial 15')
lblIndex = Label(Formulario, text = 'Index: ', font = 'Arial 15') 
lblCompKMP = Label(Formulario, font = 'Arial 15')
lblCompBasica = Label(Formulario, font = 'Arial 15') 

## Text e Entry
txtSequenciaDNA = Text(Formulario, background = 'white', width = 51, height = 5, font = 'Arial 15')
txtSubSequencia = Entry(Formulario, background = 'white', width = 51, font = 'Arial 15')
txtResultado = Text(Formulario, background = Formulario['background'], width = 74, borderwidth = 0,
    height = 5, font = 'Arial 15', state = DISABLED)

# Lucas Frade - 04/05/2023 || Criando ScrollBar para ficar melhor ao ver no Text
scrollbar = Scrollbar(Formulario, orient = VERTICAL, command = txtResultado.yview)
image = PhotoImage(file= r"src/icon_info.png")
image = image.subsample(25,25)

## Buttons
# Gabriela Villani - 30/02/2023 || Adicionando Funções aos Botões
btnResultado = Button(Formulario, width = 25, text = 'RESULTADO', command = EventoBtnResultadoOnClick,
    background = '#83A0A0', activebackground = '#83A0A0')
btnLimpar = Button(Formulario, width = 25, text = 'LIMPAR', command = LimparFormulario,
    background = '#EBEBD3', activebackground = '#EBEBD3')
btnInfo = Button(Formulario,width=50,text="info",image=image,compound = LEFT, font = 'Arial',
                 relief = FLAT, command = EventoBtnInformacoesOnClick)

# Colocando os Componentes na Tela
# Lucas Frade - 04/05/2023 || Realocando Componentes
lblSequenciaDNA.place(x = 25, y = 115)
txtSequenciaDNA.place(x = 215, y = 65)

lblSubsequencia.place(x = 66, y = 208)
txtSubSequencia.place(x = 215, y = 205)

lblIndex.place(x = 130, y = 260)
txtResultado.place(x = 130, y = 290)

scrollbar.place(x = 950, y = 290)
txtResultado.configure(yscrollcommand = scrollbar.set) 

lblCompKMP.place(x = 820, y = 65)
lblCompBasica.place(x = 820, y = 135)

btnResultado.place(x = 780, y = 420)
btnLimpar.place(x = 780, y = 460)
btnInfo.place(x = 1000, y = 510)

vLargura = 1100 
vAltura = 560

vLarguraTela = Formulario.winfo_screenwidth()
vAlturaTela = Formulario.winfo_screenheight()

x = (vLarguraTela // 2) - (vLargura // 2)
y = (vAlturaTela // 2) - (vAltura // 2)


Formulario.geometry('{}x{}+{}+{}'.format(vLargura, vAltura, x, y))
Formulario.title('Busca em DNA com KMP')

Formulario.resizable(height = FALSE, width = FALSE)
Formulario.mainloop()

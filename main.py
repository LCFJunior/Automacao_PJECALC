import subprocess
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
import csv
import os

# Caminhos
CAMINHO_BAT = r"D:\documentos\pjecalc-windows64-2.13.2\iniciarPjeCalc.bat"
PASTA_PJECALC = r"D:\documentos\pjecalc-windows64-2.13.2"
IMAGEM_BOTAO = "Criar_Calc.png"
IMAGEM_PARAMETROS = "Parametros.png"
CAMINHOS_CSV_CALCULO = "dados_calculo.csv"
CAMINHOS_CSV_PARAMETROS = "dados_parametro.csv"

def iniciar_pjecalc_com_enter():
    subprocess.Popen([CAMINHO_BAT], cwd=PASTA_PJECALC, shell=True)
    print("PJECALC iniciado. Aguardando popup...")
    time.sleep(1)
    pyautogui.press('enter')

def clicar_botao_criar_calculo():
    print("Aguardando o botão 'Criar Novo Cálculo' aparecer na tela...")
    for tentativa in range(30):
        pos = pyautogui.locateCenterOnScreen(IMAGEM_BOTAO, confidence=0.6)
        if pos:
            pyautogui.click(pos)
            return True
        time.sleep(1)
    return False

def clicar_botao_parametros():
    print("Aguardando o botão 'Parâmetros' aparecer na tela...")
    for tentativa in range(30):
        pos = pyautogui.locateCenterOnScreen(IMAGEM_PARAMETROS, confidence=0.6)
        if pos:
            pyautogui.click(pos)
            print("Botão 'Parâmetros' clicado.")
            return True
        time.sleep(1)
    print("Botão 'Parâmetros' não encontrado após 30 tentativas.")
    return False

def pular_campos_iniciais(numero_tabs=12):
    for _ in range(numero_tabs):
        pyautogui.press('tab')
        time.sleep(0.1)

def preencher_campos(dados):
    time.sleep(2)
    pular_campos_iniciais(12)

    campos_ordem = [
        dados.get("numero_processo"),
        dados.get("digito"),
        dados.get("ano"),
        dados.get("tribunal"),
        dados.get("vara"),
        dados.get("valor_causa"),
        dados.get("autuado_em"),

        dados.get("reclamante_nome"),
        "",
        dados.get("CPF_reclamante"),
        "",
        dados.get("pis_reclamante"),

        dados.get("advogado_reclamante_nome"),
        dados.get("oab_reclamante"),
        "",
        dados.get("CPF_advogado"),
        "#",

        dados.get("reclamado_nome"),
        "",  # radio 4
        dados.get("CPF_reclamado"),

        dados.get("advogado_reclamado_nome"),
        dados.get("oab_reclamado"),
        "",
        dados.get("cpf_advogado_reclamado"),
        "#",
    ]

    for valor in campos_ordem:
        if valor == "":
            pyautogui.press('space')
            time.sleep(0.1)
            pyautogui.press('tab')
        elif valor == "#":
            pyautogui.press('tab')
        elif not valor:
            for _ in range(3):
                pyautogui.press('tab')
        else:
            pyautogui.write(str(valor))
            pyautogui.press('tab')
        time.sleep(0.1)

    print("Campos preenchidos com sucesso. Tentando clicar no botão 'Parâmetros'...")
    clicar_botao_parametros()

def preencher_parametros_calculo(dados):
    print("Preenchendo parâmetros do cálculo...")
    time.sleep(2)

    campos = [
        "#",
        dados.get("estado"),
        dados.get("municipio"),
        dados.get("admissao"),
        "#",
        dados.get("demissao"),
        "#",
        dados.get("ajuizamento"),
        "#",
        dados.get("data_inicial_LC"),
        "#",
        dados.get("data_final_LC"),
        "#",
        "#",
        "#",        
        "#",
        dados.get("maior_remun"),
        dados.get("ultima_remun"),
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        dados.get("carga_horaria"),
        dados.get("excecoes_inicio"),
        "#",
        dados.get("excecoes_fim"),
        "#",
        dados.get("excecao"),
        "#",
        "",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        dados.get("Comentarios"),
        ""
    ]

    for valor in campos:
        if valor == "":
            pyautogui.press('space')
            time.sleep(0.1)
            pyautogui.press('tab')
        elif valor == "#":
            pyautogui.press('tab')
        elif not valor:
            for _ in range(3):
                pyautogui.press('tab')
        else:
            pyautogui.write(str(valor))
            pyautogui.press('tab')
        time.sleep(0.1)

    checkboxes = [
        ("projetar_aviso", "sim"),
        ("limitar_avos", "sim"),
        ("zerar_valor", "sim"),
        ("feriados_estaduais", "sim"),
        ("feriados_municipais", "sim"),
    ]

    for chave, esperado in checkboxes:
        if dados.get(chave, "").lower() == esperado:
            pyautogui.press('space')
        pyautogui.press('tab')
        time.sleep(0.1)

    print("Parâmetros do cálculo preenchidos.")

def ler_csv(caminho_csv):
    if not os.path.exists(caminho_csv):
        messagebox.showerror("Erro", f"Arquivo CSV '{caminho_csv}' não encontrado.")
        return None

    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            return linha
    return None

def on_click_iniciar():
    dados_calc = ler_csv(CAMINHOS_CSV_CALCULO)
    dados_param = ler_csv(CAMINHOS_CSV_PARAMETROS)

    if dados_calc and dados_param:
        iniciar_pjecalc_com_enter()
        time.sleep(2)
        if clicar_botao_criar_calculo():
            preencher_campos(dados_calc)
            preencher_parametros_calculo(dados_param)
        else:
            messagebox.showerror("Erro", "Botão 'Criar Cálculo' não encontrado.")

# Interface Tkinter
janela = tk.Tk()
janela.title("Automação PJECALC")
janela.geometry("300x160")
janela.resizable(False, False)

label = tk.Label(janela, text="Clique no botão para iniciar o PJECALC", font=("Arial", 11))
label.pack(pady=10)

btn_iniciar = tk.Button(janela, text="Iniciar Automação", font=("Arial", 12), command=on_click_iniciar)
btn_iniciar.pack(pady=15)

janela.mainloop()

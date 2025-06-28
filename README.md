# 🧾 Automação PJECALC - Preenchimento Inteligente  
Este é um aplicativo desktop em Python com interface gráfica (Tkinter) que automatiza o processo de preenchimento de dados no sistema PJECALC, simulando ações humanas como cliques e digitação, com base em arquivos CSV personalizados.  
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow) ![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-Educacional-lightgrey)  
## ✨ Funcionalidades  
✅ Interface simples para selecionar e iniciar o processo  
✅ Abertura automática do PJECALC via `.bat`  
✅ Reconhecimento visual de botões com imagens (.png)  
✅ Preenchimento automático dos campos do cálculo  
✅ Acesso e preenchimento da aba de parâmetros  
✅ Uso de arquivos `.csv` para controle total dos dados  
✅ Suporte a campos do tipo texto, botão e seletor  
✅ Execução com apenas um clique  
## 🖼️ Interface  
A interface foi desenvolvida com Tkinter. Ela possui apenas um botão de execução principal — o objetivo é ser o mais direto possível. A automação ocorre em segundo plano após o clique, com tempo de espera e movimentações automáticas usando PyAutoGUI.  
## 🧪 Tecnologias Utilizadas  
- [Python 3](https://www.python.org/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html)  
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)  
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)  
- [CSV / time / subprocess](https://docs.python.org/3/library/)  
## ⚙️ Como usar  
1. Clone este repositório: git clone https://github.com/seu-usuario/automacao-pjecalc.git && cd automacao-pjecalc  
2. Instale as dependências: `pip install pyautogui pillow`
3. Edite o caminho do PJECALC no script principal (linha com CAMINHO_BAT): `CAMINHO_BAT = r"D:\documentos\pjecalc-windows64-2.13.2\iniciarPjeCalc.bat"`
4. Execute o script: python script.py  
5. Aguarde o PJECALC abrir e o botão “Criar Novo Cálculo” ser reconhecido. A automação seguirá até preencher tudo automaticamente.  
## 📁 Estrutura esperada  
automacao-pjecalc/  
├── Criar_Calc.png             (`# Imagem do botão "Criar Novo Cálculo"`)  
├── Parametros.png             (`# Imagem do botão "Parâmetros"`)
├── dados_calculo.csv          (`# Dados principais do cálculo`)  
├── dados_parametro.csv        (`# Dados complementares (parâmetros)`)  
├── script.py                  (`# Código principal`)  
├── README.md                  (`# Este arquivo`)  
└── requirements.txt           (`# Lista opcional de dependências`)  

## 📌 Requisitos  
- Python 3.10 ou superior  
- Tela com resolução compatível com a captura das imagens  
- Imagens .png compatíveis com o seu ambiente (tema claro/escuro)  
- PJECALC instalado localmente, com script .bat de inicialização configurado corretamente


<br><br>
<p align="center"><em>Feito com 💻 por Luiz Carlos Francisco Junior</em></p>



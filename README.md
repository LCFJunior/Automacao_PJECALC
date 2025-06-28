# 🧾 Automação PJECALC

**Status**: 🚧 *Em desenvolvimento*  
**Descrição**: Este projeto realiza a automação do preenchimento de dados no sistema PJECALC, utilizando reconhecimento de imagens, automação de teclado e mouse com pyautogui, leitura de arquivos CSV com os dados do processo e parâmetros, e uma interface gráfica simples em tkinter.

## 📁 Estrutura de Arquivos Esperada

📦 Projeto  
├── dados_calculo.csv  
├── dados_parametro.csv  
├── Criar_Calc.png  
├── Parametros.png  
└── script.py

## 🧰 Tecnologias Utilizadas

- Python 3.x  
- PyAutoGUI  
- Tkinter (GUI)  
- Pillow (PIL)  
- Subprocess  
- CSV

## ⚙️ Funcionalidades

- Inicia o PJECALC via script .bat  
- Confirma alertas iniciais automaticamente  
- Localiza e clica no botão "Criar Novo Cálculo"  
- Preenche todos os campos automaticamente a partir de um CSV  
- Acessa e preenche os "Parâmetros" com base em outro CSV  
- Interface simples com botão de início

## 🧪 Pré-Requisitos

- Python 3.7 ou superior  
- Instalar as dependências:  
  `pip install pyautogui pillow`  
- O caminho para iniciar o PJECALC deve estar configurado nesta variável dentro do script:  
  `CAMINHO_BAT = r"D:\documentos\pjecalc-windows64-2.13.2\iniciarPjeCalc.bat"`  
- As imagens Criar_Calc.png e Parametros.png devem estar na mesma pasta do script e devem ter sido capturadas da sua tela, com a resolução e tema corretos, para o reconhecimento por imagem funcionar.

## 📝 Como Usar

1. Preencha os arquivos:  
   - dados_calculo.csv com as informações do cálculo  
   - dados_parametro.csv com as informações dos parâmetros  
2. Execute o script:  
   `python script.py`  
3. Na janela que abrir, clique no botão "Iniciar Automação"

## 📌 Observações

A automação depende da resolução da tela e da velocidade do sistema. Ajuste os time.sleep() conforme necessário. Os campos "#" no código são pulados com TAB, e campos "" são botões ou opções que recebem SPACE. Certifique-se de que o PJECALC esteja visível em tela cheia ou com as janelas desobstruídas. O script tenta clicar em botões com base em imagens da tela. Se a aparência visual do PJECALC mudar, será necessário capturar novamente as imagens.

## 💡 Melhorias Futuras

Adicionar suporte a múltiplos registros por execução. Incluir log de erros e progresso da automação. Permitir edição manual antes do envio final. Adicionar captura automática das imagens de referência.

## 📜 Licença

Este projeto é de uso educacional e interno. Não possui licença comercial ou garantia de funcionamento universal.

Feito com 💻 por Luiz Carlos Francisco Junior

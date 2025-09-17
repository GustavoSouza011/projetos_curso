
import os
import flet as ft

texto_2 = ""

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"
    page.bgcolor = "#121212"
   
    # Função para criar pastas
    def criar_pasta(e):
        global texto_2# ESTAMOS DEIXANDO VISIVEL PARA TODAS AS FUNÇÕES
        texto_2 = texto_recebido.value
        try:
            os.mkdir(texto_2)
            informativo.value = f"Pasta criada: '{texto_2}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto_2}' foi criada."
        page.update()
   
    # Função para criar arquivos
    def criar_arquivo(e):
        texto = texto_recebido.value
        if texto_2 == "":
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}.txt'"
        else:
            open(f"{texto_2}/{texto}", "w").close()
            informativo.value = f"Arquivo criado: '{texto_2}/{texto}.txt'"
        page.update()

       
    #funçâo para remover arquivo
    def remover_arquivo(e):
        texto = texto_recebido.value # PEGANDO O VALOR QUE ESTA ESCRITO NA CAIXA
        if texto_2 == "": # SE A CAIXA ESTIVER VAZIA
            os.remove(texto) # REMOVER O ARQUIVO QUE ESTIVER ESCRITO NA CAIXA
            informativo.value = f"Arquivo removido '{texto}'" # MOSTRANDO A MSG SE FUNCIONAR
        else: # SE NAO
            os.remove(f"{texto_2}/{texto}") # REMOVER O ARQUIVO DENTRO DA PASTA
            informativo.value = f"Arquivo removido '{texto_2}/{texto}'" # MOSTRANDO A MSG SE FUNCIONAR
        page.update() # ATUALIZANDO A PAGINA

    # Campos e botões
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta/remover...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="WHITE",color="GRAY", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="WHITE", color="GRAY", width=200, on_click=criar_arquivo)
    botao_remover_arquivo = ft.ElevatedButton("REMOVER ARQUIVO",bgcolor="WHITE",color="GRAY",width=200,on_click=remover_arquivo)
    informativo = ft.Text("", size=20, color="white")

    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo,botao_remover_arquivo], alignment="center"),
        ft.Row([informativo], alignment="center")
    )
ft.app(target=main)
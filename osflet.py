import os
import flet as ft

# Defina informativo como um controle de texto global
informativo = ft.Text(value="")
texto_recebido = ft.TextField(label="Ecreva o nome do arquivo/ pasta...")
def main(page: ft.Page):
    page.add(texto_recebido)
    page.add(informativo)
    page.add(informativo)

def main(page: ft.Page):
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    informativo = ft.Text("", size=20, color="white")
    


    def criar_pasta(e):
        global texto_pasta
        texto_pasta = texto_recebido.value
        try:
            os.mkdir(texto_pasta)
            informativo.value = f"Pasta criada: '{texto_pasta}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto_pasta}' já existe."
        page.update()

    def listar_pasta(e):
        try: 
            arquivos = os.listdir(texto_pasta)
            for item in arquivos:
                informativo.value = f"listar pasta: {arquivos}"
                page.update()
        except Exception as erro:
            informativo.value = f"Erro ao listar pasta: {erro}"
            page.update()

    def apagar_pasta(e):
        texto = texto_recebido.value
        try:
            os.rmdir(texto)
            informativo.value = f"Pasta apagada: '{texto}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' foi excluida."
        page.update()

    def criar_arquivo(e):
        texto = texto_recebido.value
        try:
            open(f"{texto_pasta}/{texto}", "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    def apagar_arquivo(e):
        texto = texto_recebido.value
        try:
            os.remove(f"{texto_pasta}/{texto}")
            informativo.value = f"Arquivo excluido : '{texto}'"
        except Exception as erro:
            informativo.value = f"erro: {erro}"
            page.update()

    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_apagar = ft.ElevatedButton("APAGAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=apagar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_arquivo)
    botao_arquivo_apg = ft.ElevatedButton("APAGAR ARQUIVO", bgcolor="PURPLE", color="WHITE", width=200, on_click=apagar_arquivo)
    botao_mostrar = ft.ElevatedButton("MOSTRAR ARQUIVO", bgcolor="PURPLE", color="WHITE", width=200, on_click=listar_pasta)

    page.title = "Interface com OS"
    page.theme_mode = "DARK"
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta,botao_apagar, botao_arquivo,botao_arquivo_apg,botao_mostrar], alignment="center"),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)

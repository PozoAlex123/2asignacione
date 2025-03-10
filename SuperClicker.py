import flet as ft
 
def main(page: ft.Page):
    count = ft.Text(value="0", size=25)
    mensaje = ft.Text(value="", size=25)
    
    
    
    def Aumentar1(e):
        count.value = int(count.value) + 1
        mensaje1()
        page.update()
 
 
    def mensaje1():
        contador = int(count.value)
        if contador == 15:
            mensaje.value = "Balbaro, 15 clicks"
        elif contador == 25:
            mensaje.value = "en verdad no es tanto pero dale"
        elif contador == 40:
            mensaje.value = "Te duele el dedo?????"
        elif contador == 65:
            mensaje.value = " haz otra cosa, como que 65"
        elif contador == 100:
            mensaje.value = "100 clicks viciao"
        elif contador == 500:
            mensaje.value = "GREEN FN(no me dejo pone emoji de fuego)"
        page.update()
 
    def botondereset(e):
        count.value = "0"
        mensaje.value = ""
        page.update()
 
    botonplus = ft.ElevatedButton("Aumentar", on_click=Aumentar1)
    boton0 = ft.ElevatedButton("Reiniciar", on_click=botondereset)
 
    page.add(count, mensaje, botonplus, boton0)
 
ft.app(target=main)

#Use Chatgpt por que taba haciendolo y no sabia que yo tenia mal

#https://chatgpt.com/share/67aaae48-b7a8-8004-8f85-d9272f09cb4a






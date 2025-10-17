import os
import customtkinter as ctk 
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress

def escolher_pasta():
    return filedialog.askdirectory(title="Escolha a pasta para salvar seu video")

def baixar_video():
    url = url_entrada.get()
    pasta = escolher_pasta()
    if not pasta:
        os.path.join(os.path.expanduser("~"),'Downloads')
    
    yt = YouTube(url,on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=pasta)
    
    label_sucess_alert.configure(text=f"Video baixado em {pasta}")



ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.resizable(True,True)
app.geometry("600x600")
app.title('Baixador de video do YouTube')

url_entrada = ctk.CTkEntry(app,placeholder_text="Cole aqui a URL do Video",width=400)
url_entrada.pack(pady=10)

botao_download = ctk.CTkButton(app,text="Baixar video", command=baixar_video)    
botao_download.pack(pady=10)    

label_sucess_alert = ctk.CTkLabel(app,text="")
label_sucess_alert.pack(pady=10)
app.mainloop()
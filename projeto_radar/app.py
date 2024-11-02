import customtkinter as ctk
import threading
from PIL import Image
import conexão_ard as ca
sist = ctk.CTk()
ca.cg.grafico_inicial()

def novo_grafico(grau, dist):  # Atualiza  a interface do aplicativo quando novas informações são recebidas
    global graus, distancia, label_radar_do_radar
    som = threading.Thread(target=ca.cg.som_sonar)
    som.daemon == True
    som.start()
    graus.configure(text=f"{grau}º")
    distancia.configure(text=f"{dist}cm")
    rad = Image.open("C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\radar.png")
    rad_img = ctk.CTkImage(rad, size= (600,550))
    label_radar_do_radar.configure(image=rad_img)
    

def atualizar_interface(): # Verifica se tem que atualizar a interface
    if ca.atualizar_agora:
        novo_grafico(ca.graus_graf, ca.dist)
        ca.atualizar_agora = False
    sist.after(100, atualizar_interface)

def status_conexao(): # Checa o status da conexão com o arduino
    global status, conectar
    if ca.conectado == True:
        status.configure(fg_color="green",text="Conectado ! ")
        conectar.configure(command=None)
    else:
        status.configure(fg_color="#8b0000",text=f"Desconectado!")
        conectar.configure(command=conectar_se)
    sist.after(100,status_conexao)

def conectar_se(): # Estabelece a conexão com o arduino
    global analise_porta
    analise_porta = threading.Thread(target=ca.analise)
    analise_porta.daemon == True
    analise_porta.start()

def sair(): # Fecha o aplicativo
    ca.desconectar = True
    sist.quit()
    sist.destroy()
    

sist.geometry("1920x1080")
sist.title("ECHO NAVIGATOR")

back = Image.open("C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\black.jpeg")
background = ctk.CTkImage(back, size= (1920,1080))

background_label = ctk.CTkLabel(sist,image = background)
background_label.place(relwidth=1, relheight=1)

rad = Image.open("C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\radar.png")
rad_img = ctk.CTkImage(rad, size= (600,550))
label_radar_do_radar = ctk.CTkLabel(sist,text = None, image=rad_img, padx = 30, pady=30)


label_registro = ctk.CTkFrame(sist,fg_color="black",bg_color="black", corner_radius=40)
label_titulo_registro = ctk.CTkLabel(label_registro,text="Coordenadas", justify="center",padx =30, pady=30,font=('Arial',23),text_color="#04D9C4", fg_color="black",bg_color="black")
label_nome_graus = ctk.CTkLabel(label_registro, text="Graus", padx = 20, pady = 20, width=100, height=100,font=('Arial',20),text_color="#04D9C4",fg_color="black",bg_color="black")
label_nome_distancia = ctk.CTkLabel(label_registro, text="Distância", padx= 15, pady = 20, width=90, height=100,font=('Arial',18),text_color="#04D9C4",fg_color="black",bg_color="black")
graus = ctk.CTkLabel(label_registro, text="Null", text_color="#04D9C4", padx = 30, pady = 30, width=100, height=100,font=('Arial',20),fg_color="black",bg_color="black")
distancia = ctk.CTkLabel(label_registro, text="Null",text_color="#04D9C4", padx = 30, pady = 30, width=100, height=100,font=('Arial',20),fg_color="black",bg_color="black")

conectar = ctk.CTkButton(sist,hover_color="red",bg_color = "black",fg_color="#03A696", text="Conectar-se", command = conectar_se, width = 400, height = 40, font = ("Arial",20), text_color="white")
status = ctk.CTkLabel(sist, text = f"{ca.conectado}",text_color="white",fg_color="red", font=("Arial",20), padx= 10, pady=10)
desconectar = ctk.CTkButton(sist, hover_color="red",bg_color="black",text = "Sair", command = sair, fg_color = "#03A696",width=150, height =50, font = ("Arial", 20))


status.grid(row=0,column=1, pady=30)
conectar.grid(row = 0, column=0)
desconectar.grid(row=3, column = 1, pady= 30)
label_registro.grid(row=1,rowspan = 2, column=1)
label_radar_do_radar.grid(row=1, rowspan=3,column=0,padx=170)
label_titulo_registro.grid(row=0, column = 0,columnspan=2)
label_nome_graus.grid(row = 1,column= 0)
label_nome_distancia.grid(row = 1,column=1)
graus.grid(row = 2, column = 0)
distancia.grid(row =2, column = 1)


analise_porta = threading.Thread(target=ca.analise)
analise_porta.daemon == True
analise_porta.start()

status_conexao()
atualizar_interface()
sist.mainloop()
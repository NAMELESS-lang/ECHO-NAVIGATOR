import matplotlib.pyplot as plt
import numpy as np

def atualizar_grafico(grau, dist):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    fig.set_facecolor("black")
    ax.set_facecolor("#01403A")
    ax.set_xlabel("Distância(cm)",color="#04D9C4",size=15)
    ax.set_thetamax(180)
    ax.set_ylim(0,3)
    ax.set_yticks(np.linspace(0, 30, 4))
    ax.tick_params(colors="#04D9C4", labelsize=15, size = 15, grid_color = "#05f2db")
    graus = grau*np.pi/180
    graus_sensor = 90*np.pi/180
    point, = ax.plot([graus], [dist], "r", marker = "o", markersize=9)
    ax.text(graus,dist+1.5,f"{dist}cm", fontsize = 10, ha="center",color="white")
    point, = ax.plot([graus_sensor],[1.2], "w",marker="*", markersize=10)
    fig.savefig("C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\radar.png")
    return

def grafico_inicial():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    fig.set_facecolor("black")
    ax.set_facecolor("#01403A")
    ax.set_xlabel("Distância(cm)",color="#04D9C4",size=15)
    ax.set_thetamax(180)
    ax.set_ylim(0,3)
    ax.set_yticks(np.linspace(0, 30, 4))
    ax.tick_params(colors="#04D9C4", labelsize=15, size = 15, grid_color = "#05f2db")
    point, = ax.plot([(90*np.pi/180)],[1.2], "w",marker="*", markersize=10)
    fig.savefig("C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\radar.png")
    return

def som_sonar():
    import pygame
    caminho = "C:\\Users\\mathe_u45khu0\\OneDrive\\Área de Trabalho\\projeto_radar\\sonar sound effect.WAV"
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    return

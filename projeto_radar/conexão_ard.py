import serial
import time
import criar_grafico as cg
atualizar_agora = False
conectado = False
desconectar = False
portas_disponiveis = None
def analise():
    global atualizar_agora, graus_graf, dist, conectado, desconectar
    try:
        ser = serial.Serial("COM9", 9600)  # Conecta à porta serial
        conectado = True
        while desconectar == False:  # Loop contínuo para ler os dados
            if ser.in_waiting:  # Verifica se há dados na porta
                graus_graf = ser.readline().decode("utf-8").strip()
                dist = ser.readline().decode("utf-8").strip()
                graus_graf =int(graus_graf)
                dist = int(dist)
                cg.atualizar_grafico(graus_graf, dist)
                atualizar_agora = True
            time.sleep(0.5)  # Pausa entre as leitura
        return # quando é clicado no botão sair a variavel desconectar muda para true

    except serial.SerialException as e:  # Se a conexão falhar
        print(f"Erro de conexão: {e}")
        conectado = False
    except Exception as e:  # Captura outros erros
        print(f"Erro ao processar dados: {e}")
        conectado = False
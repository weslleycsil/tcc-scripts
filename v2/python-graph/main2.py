import json
import matplotlib.pyplot as plt

def gerar_grafico_arquivos(arquivos,legendas):

    fig, ax = plt.subplots(figsize=(10, 6))  # Define o tamanho da figura

    for i, arquivo in enumerate(arquivos):
        tempos = []
        taxas = []
        
        with open(arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
        
        for item in dados['intervals']:
            tempos.append(item['sum']['start'])
            taxas.append(item['sum']['bits_per_second'] / 1e9)  # Converter para Gbps
    
        ax.plot(tempos, taxas, label=legendas[i], linewidth=2)
    
    ax.set_xlabel('Tempo (segundos)', fontsize=12)
    ax.set_ylabel('Taxa de Transferência (Gbps)', fontsize=12)
    ax.set_title('Comparação de Taxa de Transferência', fontsize=14)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend(fontsize=10, frameon=False, bbox_to_anchor=(0, -0.3), loc='lower left') #  Removendo a caixa da legenda, Movendo a caixa de legendas para o canto inferior esquerdo, abaixo do gráfico

    # Personalizando os ticks nos eixos x e y
    ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
    ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=True)

    plt.show()

# Exemplo de uso:
arquivos = ['iperf-out/ocn1.json', 'iperf-out/ocn1_docker_to_docker.json', 'iperf-out/ocn1_swarm_to_swarm.json']
legendas = ['Entre Hosts','Entre Contêineres','Entre Contêineres no Swarm']
gerar_grafico_arquivos(arquivos,legendas)

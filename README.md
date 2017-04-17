# TCP-X-UDP
Analisando tempo e confiabilidade entre os dois protocolos

Para realizar os testes, foi feita uma implementação nos dois dois protocolos TCP e UDP, no qual
obtemos as seguintes informações no cliente e servidor das conexões:

<pre>
Tempo
Tamanho
Código md5
</pre>

O objetivo é analisar o tempo entre um protocolo e outro, verificar se todos os dados foram recebidos
e verificar se todos os dados estão íntegros.

# Resultados

Foram feitos envios de 3 tamanhos de arquivos para o ip do roteador:
<pre>
585.2 KB
1.0 GB
2.0 GB
</pre>

No qual se foram obtidos os seguintes resultados:

585.2 KB
<pre>
TCP
tempo: 0.00467991828918
tamanho: 585239
d5d758ba536e4e5d6fc2ae9007a604ae

UDP 
tempo: 0.00361895561218
tamanho: 585239
d5d758ba536e4e5d6fc2ae9007a604ae
</pre>

1.0 GB
<pre>
</pre>

2.0 GB
<pre>
</pre>

e foram gerados os seguintes gráficos:

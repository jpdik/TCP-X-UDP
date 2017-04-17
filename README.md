# TCP-X-UDP
Analisando tempo e confiabilidade entre os dois protocolos

Para realizar os testes, foi feita uma implementação nos dois dois protocolos `TCP` e `UDP`, no qual
obtemos as seguintes informações no cliente e servidor das conexões:

`Tempo`: Tempo de envio para o servidor;__
`Tamanho`: Tamanho do arquivo recebido;__
`Código md5`: código de informa se o arquivo está integro, porque precisa ser o mesmo do arquivo original;__

O objetivo é analisar o tempo entre um protocolo e outro, verificar se todos os dados foram recebidos
e verificar se todos os dados estão íntegros.

# Arquivo de testes

Para arquivos grandes de testes, foi criado um gerador.
Basta executar o `gerar.py` passando a quantidade de GB's o arquivo de `teste.txt` terá.
Exemplo:

<pre>
python gerar.py 1
</pre>

# Resultados

Foram feitos envios de 3 tamanhos de arquivos para o ip do roteador:
<pre>
585.2 KB
1.1 GB
2.1 GB
</pre>

No qual se foram obtidos os seguintes resultados de recebimento no sevidor:

585.2 KB
<pre>
TCP
tempo: 0.00467991828918
tamanho: 585.239
d5d758ba536e4e5d6fc2ae9007a604ae (Correto)

UDP 
tempo: 0.00361895561218
tamanho: 585.239
d5d758ba536e4e5d6fc2ae9007a604ae (Correto)
</pre>

1.1 GB
<pre>
TCP
tempo: 11.0367531776
tamanho: 1.073.741.824
adb5a28fda6ec2a01075b9945887a083 (Correto)

UDP
tempo: 41.8832139969
tamanho: 1.070.774.272
2f1969c6c8f1390a664ef5bf81308643 (Incorreto)
</pre>

2.0 GB
<pre>
TCP
tempo: 89.9414391518
tamanho: 2.147.483.648
d81114fa7eec56193a13ca3cb2526991 (Correto)

UDP
tempo: 86.2373151779
tamanho: 2.141.937.664
db1fbba3b7068f69bb9a999f57899544 (Incorreto)
</pre>

e foram gerados os seguintes gráficos:

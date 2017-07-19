# TCP-X-UDP
Analisando tempo e confiabilidade entre os dois protocolos

Para realizar os testes, foi feita uma implementação nos dois dois protocolos `TCP` e `UDP`, no qual
obtemos as seguintes informações no cliente e servidor das conexões:

`Tempo`: Tempo de envio para o servidor; <br />
`Tamanho`: Tamanho do arquivo recebido; <br />
`Código md5`: código de informa se o arquivo está integro, porque precisa ser o mesmo do arquivo original;<br />

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

Foram feitos envios de 3 tamanhos de arquivos na rede para o ip do roteador:
<pre>
585.2 KB   md5(d5d758ba536e4e5d6fc2ae9007a604ae)
  1.1 GB   md5(adb5a28fda6ec2a01075b9945887a083)
  2.1 GB   md5(d81114fa7eec56193a13ca3cb2526991)
</pre>

No qual se foram obtidos os seguintes resultados de recebimento no sevidor:

585.2 KB
<pre>
TCP
tempo: 0.00249910354614
tamanho: 585.239
tempo médio: 1.57806423161e-06
md5: d5d758ba536e4e5d6fc2ae9007a604ae (Correto)

UDP 
tempo: 0.00267195701599
tamanho: 585.239
tempo médio: 2.1474344747e-06
md5: d5d758ba536e4e5d6fc2ae9007a604ae (Correto)
</pre>

1.1 GB
<pre>
TCP
tempo: 4.07875609398
tamanho: 1.073.741.824
tempo médio: 1.37013103085e-06
md5: adb5a28fda6ec2a01075b9945887a083 (Correto)

UDP
tempo: 4.1785800457
tamanho: 1.003.311.104
tempo médio: 1.96201576877e-06
md5: fd55dc73ac133f9e466e196237447975 (Incorreto)
</pre>

2.1 GB
<pre>
TCP
tempo: 36.678647995
tamanho: 2.147.483.648
tempo médio: 1.70333646565e-06
md5: d81114fa7eec56193a13ca3cb2526991 (Correto)

UDP
tempo: 8.46506595612
tamanho: 1.203.718.144
tempo médio: 2.0753563078e-06
md5: eb2513423f51a740a55350c399a5df56 (Incorreto)
</pre>

e foram gerados os seguintes gráficos:

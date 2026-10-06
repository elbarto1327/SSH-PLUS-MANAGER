# ELBARTO-VPN SSH (SSH-PLUS-MANAGER V32)

**Script de Gerenciamento**

## Requisitos

* Sistema operacional baseado em Linux (Ubuntu ou Debian)
* Recomendado: Ubuntu 16.04 Server x86_64
* Também pode funcionar em algumas versões do Debian Server x86_64

## Instalação e Atualização

Para instalar ou atualizar o painel para a última versão hospedada neste repositório, rode o seguinte comando no terminal (como root):

`ash
apt-get update -y; apt-get upgrade -y; wget -q https://raw.githubusercontent.com/elbarto1327/SSH-PLUS-MANAGER/main/Plus -O Plus; chmod 777 Plus; ./Plus
`

> **AVISO IMPORTANTE:** NUNCA utilize a opção [28] ATUALIZAR SCRIPT por dentro do painel da VPS! Essa opção tenta buscar os arquivos no repositório do desenvolvedor original, o que removerá as suas customizações e nomes do painel. Sempre atualize usando o comando acima!

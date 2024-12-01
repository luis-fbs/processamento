# Processamento
Desenvolvido para a disciplina de Arquitetura de Computadores, esse repositório contém o programa usado para filtrar CPU's por socket, atualizando os valores dos sockets desconhecidos. 

## Configuração
Para executar o programa, por segurança, optei por não deixar a chave de api escrita diretamente no código. Dessa forma, é necessário que, antes de executar o programa, o usuário crie uma variável de ambiente chamada API_GEMINI para armazenar a api-key do serviço de inteligência artificial da google (Gemini). Para isso, basta executar o comando:

`export API_GEMINI="valor da sua api-key"`

Após isso, o programa pode ser executado normalmente.

## Tempo
No momento em que criei esse repositório, o plano gratuito da Gemini tinha a limitação de 15 requests por minuto. Por conta disso, o programa faz as requisições a cada 4 segundos. Dessa forma, como temos 32 CPU's com socket desconhecido, o tempo de esperá para o processamento do arquivo será de aproximadamente 2 minutos e 8 segundos.

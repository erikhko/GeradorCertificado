# GeradorCertificado

Instruções para Executar o Projeto

	1.	Instale as dependências do projeto
Execute o comando abaixo para instalar todas as bibliotecas listadas no arquivo requirements.txt:

pip install -r requirements.txt


	2.	Inicie o Docker para conectar ao RabbitMQ
Utilize o comando abaixo para construir e subir os containers necessários:

docker compose up --build


	3.	Verifique se o container foi iniciado corretamente.
Após subir o container, siga para o próximo passo.
	4.	Realize uma solicitação POST no Postman
	•	URL: https://localhost:5000/certificates
	•	Método: POST
	•	Autenticação:
	•	Tipo: Basic Auth
	•	Usuário: user
	•	Senha: password
	•	Headers:
	•	Content-Type: application/json
	•	Body (em formato JSON):

{
  "name": "Erik Ko",
  "course": "SI",
  "date_issued": "30/05/2025"
}


	5.	Geração do PDF
Após enviar a solicitação, o PDF gerado será salvo automaticamente na pasta pdfs dentro do diretório do projeto.

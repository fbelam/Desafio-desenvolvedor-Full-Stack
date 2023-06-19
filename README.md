1-	Qual dos dois bancos (MySQL ou Postgres) você utilizou e o motivo;

O banco de dados utilizado no projeto foi o MySQL. Embora ambos, MySQL e PostgreSQL, tenham desempenho semelhante e possam ser utilizados como bancos de dados relacionais, o PostgreSQL oferece a opção adicional de ser um banco de dados de objetos. No entanto, para esse projeto em particular, não seria necessário utilizar essa funcionalidade extra. Sendo assim, o que mais influenciou minha escolha foi o meu conhecimento prévio do MySQL, levando em consideração o fato de que eu tinha um tempo limitado para aprender a utilizar novas ferramentas durante o desafio. Portanto, decidi investir em um banco de dados que eu já conhecia.

2-	Quais querys você usou para criar a estrutura do banco? 

CREATE DATABASE pre_venda;

CREATE TABLE tb_parceiros (
    id INT(11),
    nome_parceiro VARCHAR(100),
    endereco_parceiro VARCHAR(200),
    cnpj CHAR(18),
	uf_cobertura CHAR(2),
    PRIMARY KEY (id)
);

create table tb_viabilidade (
    id INT(11),
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),   
    produto VARCHAR(100),
    velocidade VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE tb_resultado_viabilidade (
	id int(11),
    id_parceiro_resposta INT(11),
    id_viabilidade INT(11),
    resultado_parceiro VARCHAR(100),
    PRIMARY KEY (id),
    CONSTRAINT fk_Parceiro_resultado FOREIGN KEY (id_parceiro_resposta) REFERENCES tb_parceiros (id),
    CONSTRAINT fk_viabilidade_resultado FOREIGN KEY (id_viabilidade) REFERENCES tb_viabilidade (id)
);


3-	Quais querys você usou para fazer a carga no banco de dados? 

insert into tb_parceiros (id, nome_parceiro, endereco_parceiro, cnpj, uf_cobertura)
 values 	
('1','13Telecom','Rua Abilio Soares, 15, Paraiso','888888888/0001-23','SP'),
('2','14Telecom','R. João Pessoa - Jacutinga','888888888/0001-24','SP'),
('3','15Telecom','Rua 10 - SHVP Colônia Agrícola Vicente Pires Chácara 147 - Setor Habitacional Vicente Pires - Taguatinga Brasília - DF','888888888/0001-25','DF'),
('4','16Telecom','Rua 10 - Setor Habitacional Vicente Pires - Taguatinga -  Brasília - DF','888888888/0001-26','RJ'),
('5','17Telecom','Avenida Jacutinga - Indianópolis - São Paulo - SP','888888888/0001-27','SP'),
('6','18Telecom','R. São Joaquim, 44 - Centro, Diadema - SP, 09911-020, Brasil','888888888/0001-28','SP'),
('7','19Telecom','Cachoeira do Arari - PA, 68840-000, Brasil','888888888/0001-29','PA'),
('8','20Telecom','Via L2 Sul - Asa Sul, Brasília - DF, 70297-400, Brasil - Asa Sul, Brasília - DF, 70200-010, Brasil','888888888/0001-30','DF'),
('9','21Telecom','Av. Argélia, 173 - Miragaia, Ubá - MG, 36500-000, Brasil','888888888/0001-31','MG'),
('10','22Telecom','QN 211 Cj. 1, 42 - Samambaia Norte, Brasília - DF, 72343-052, Brasil','888888888/0001-32','DF'),
('11','23Telecom','Av. Me. Tereza de Calcutá, 27 - Parque Industrial Joao Bras, Goiânia - GO, 74492-000, Brasil','888888888/0001-33','GO');


INSERT INTO tb_viabilidade (id, logradouro, numero, bairro, cidade, uf, produto, velocidade)
VALUES 
('1','Rod. Mario Batista Mori','33','Res. Ecopark','São Paulo','SP','Ip Connect','10MBPS'),
('2','Av. Paulista','1146','Bela Vista','São Paulo','SP','VPN VIP','10MBPS'),
('3','R. Francisco Bernardes de Assis','210','Jardin Brasilia','Uberlandia','MG','VPN VIP','1MBPS'),
('4','R. Dr. Tancredo de Almeida Neves','33',' Glória de Dourados','São Paulo','SP','Ip Connect','100MBPS'),
('5','Rua do Lavradio','71','Centro','Rio de Janeiro','RJ','DIGITRONCO','30CANAIS'),
('6','Rua Arq. Olavo Redig de campos','105','Morumbi','São Paulo','SP','Ip Connect','1GBPS'),
('7','R. Francisco Bezerra','10','Mambuca','Angra dos Reis','RJ','DIGITRONCO','10CANAIS'),
('8','Avenida Sto Amaro','94','Santo Amaro','São Paulo','SP','Ip Connect','50MBPS'), 
('9','Rua Itabapoana ','1000','Vila Isa','São Paulo','SP','Ip Connect','500MBPS'),
('10','Praça Milton Campos','100','Serra','Belo Horizonte','MG','Ip Connect','200MBPS');


INSERT INTO tb_resultado_viabilidade (id, id_viabilidade, id_parceiro_resposta, resultado_parceiro) VALUES 
('1','7','4','Viavel'),
('2','7','5','Projeto Especial'),
('3','7','1','Inviável'),
('4','7','6','Inviável'),
('5','1','1','Inviável'),
('6','1','2','Inviável'),
('7','1','5','Viavel'),
('8','1','6','Viavel'),
('9','1','7','Viavel'),
('10','1','8','Viavel'),
('11','1','10','Viavel'),
('12','3','1','Viavel'),
('13','3','9','Viavel'),
('14','3','4','Viavel'),
('15','3','10','Viavel'),
('16','10','1','Projeto Especial'),
('17','10','4','inviavel'),
('18','10','9','Viavel'),
('19','10','10','Projeto Especial'),
('20','8','1','Projeto Especial'),
('21','8','2','Projeto Especial'),
('22','8','5','inviavel'),
('23','8','6','Viavel'),
('24','8','7','inviavel'),
('25','8','8','Viavel'),
('26','8','10','inviavel'),
('27','5','1','Projeto Especial'),
('28','5','3','Projeto Especial'),
('29','5','4','Viavel'),
('30','5','5','Viavel'),
('31','5','6','Viavel');


4-	Você tem alguma sugestão de melhoria na estrutura de banco de dados enviado? 

Tive que fazer algumas alterações nos tipos e tamanhos das colunas. Por exemplo, a coluna "endereco_parceiro" foi modificada de VARCHAR(100) para VARCHAR(200), pois havia endereços que precisavam ser inseridos com mais de 100 caracteres. Já as colunas "cnpj" e "uf_cobertura" foram alteradas para CHAR(18) e CHAR(2), respectivamente, pois seus tamanhos são fixos.

5- Qual foi a lib Python usada para criar a API e por que? 

As três opções de bibliotecas mencionadas nas instruções do desafio são bem conhecidas, e a escolhida foi o Flask. Após uma extensa pesquisa, concluí que o Django é a opção mais popular, com mais projetos e apoio da comunidade para solução de bugs. No entanto, ao estudar sua documentação, percebi que levaria muito tempo para aprender a usá-lo devido à sua complexidade. Então, pesquisei sobre o FASTApi e descobri que ele é realmente simples. Cheguei a iniciar alguns projetos e aprendi sobre rotas usando essa biblioteca. No entanto, tive dificuldades para resolver problemas simples e acabei desistindo. Já havia gastado várias horas valiosas nessas duas bibliotecas, então optei pelo Flask. Acredito que o Flask conseguiu equilibrar a ajuda da comunidade e a facilidade de aprendizado. Encontrei alguns projetos que me apoiaram no desafio.

5-	Explique como você construiu o frontend da aplicação. 

Eu criei uma pasta chamada "templates" e dentro dela criei um arquivo chamado "index.html". Na página, criei uma estrutura simples utilizando HTML e adicionei a sintaxe do Jinja2 para adicionar dinamicamente conteúdo vindo do Flask, permitindo a iteração sobre uma lista. Para estilizar a página, utilizei a biblioteca Bootstrap, que oferece um conjunto de estilos pré-definidos e componentes para facilitar o design responsivo.

7- Como executar o Backend e Frontend da aplicação? 

1 - instale o Flask pip install flask
2 - Crie um arquivo chamado app.py e abra no VSCode
3-  Importe a classe Flask do módulo flask from flask import Flask
4- Crie uma instância do Flask: app = Flask(__name__)
5- Defina uma rota e uma função de visualização para a página inicial: 
@app.route('/')
def hello():
    return 'Hello, World!'
6- Adicione um bloco de código para executar o aplicativo somente quando o arquivo for executado diretamente:
if __name__ == '__main__':
    app.run()
7- execute no VScode
8- Abra o navegador e insira no endereço o numero http://localhost:5000




8- Print do Insomnia ou Postman com o método GET da API; 

![Metodo_GET](https://github.com/fbelam/Desafio-desenvolvedor-Full-Stack/assets/36649120/154a6da4-ec67-4ce5-a2d3-f2d171fef2d6)


9- Print do Insomnia ou Postman com o método POST da API;

![Metodo_POST](https://github.com/fbelam/Desafio-desenvolvedor-Full-Stack/assets/36649120/615e95b9-6c59-4a15-a101-16fcb9ca7a48)


10- Print do Insomnia ou Postman com o método PUT da API; 

Nao consegui fazer funcionar

11- Print do Insomnia ou Postman com o método DELETE da API;

![Metodo_DELETE](https://github.com/fbelam/Desafio-desenvolvedor-Full-Stack/assets/36649120/9445d639-6fde-4dcb-9e03-02787346728f)



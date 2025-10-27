# Análise de dados com um dataset de filmes.
> O projeto tem como motivação realizar uma análise em cima de um dataset com informações relacionadas a filmes, para assim orientar qual tipo de filme deve ser o próximo a ser desenvolvido.


### Objetivos que o projeto pretende alcançar

* Catalogar quais variáveis são importantes para a modelagem da previsão de notas.
* Análisar quais são os filmes mais populares e aqueles com melhor avaliação e se existe algum padrão que os estúdios podem seguir para produzir um filme lucrativo ou bem avaliado.


### Como instalar o projeto
Cabe destacar antes de tudo que o projeto foi construído no vscode, então recomenda-se que o leitor também utilize ele.
1. Clonar o repositório para sua máquina local
> git clone https://github.com/samylesousa/movies_imdb.git
2. Acessar o diretório em que o código está localizado
3. Criar um ambiente virtual
> python -m venv env
4. Ativar o ambiente virtual
> Windows : env\Scripts\Activate.ps1
> Linux : source venv\bin\activate
5. Instalar todas as bibliotecas necessárias
> pip install -r requirements.txt
6. Rodar todas as células do notebook desafio_ciencia_dados
7. Ler as conclusões e resultados apresentados


### Datasets
Além do dataset indicado também foram adicionados dados externos encontrados nos seguintes datasets:

* [Metacritic Scores for Games, Movies, TV & Music](https://www.kaggle.com/datasets/patkle/metacritic-scores-for-games-movies-tv-and-music) foi utilizado para suprir alguns dos valores que estavam faltando na coluna "Meta_score".
* [60,000+ Movies, 100+ Years of Data, Rich Metadata](https://www.kaggle.com/datasets/raedaddala/top-500-600-movies-of-each-year-from-1960-to-2024?utm_source=chatgpt.com) foi utilizado para as classificações etárias que estavam faltando no dataset.
* [Box Office Data (1984 to 2024) from BoxOfficeMojo](https://www.kaggle.com/datasets/harios/box-office-data-1984-to-2024-from-boxofficemojo?utm_source=chatgpt.com) auxiliou em relação as informações de bilheteria que estavam faltando para alguns filmes.

Deve-se enfatizar que mesmo com a adição dos 3 datasets citados, alguns filmes continuaram possuindo valores ausentes, por isso em algumas operações realizadas durante a análise esses filmes tiveram que ser descartados para não afetar a análise. No entanto, tem-se como tarefa para o futuro mapear essas informações ausentes e verificar se elas podem ser substituidas por valores reais ou se realmente são informações totalmente indisponíveis.


Outro detalhe importante sobre os datasets, é que apenas o principal, que foi o indicado para o projeto, recebeu um tratamento de dados mais profundo, com limpeza (foram verificados os valores nulos e duplicados) e engenharia de atributos (criação de novos atributos derivados de outros já existentes e tratamento de dados ausentes). Essa escolha foi motivada por questões referentes a limitação de tempo, por essa razão também indica-se como atividade futura a aplicação de operações de tratamento de dados nos 3 datasets externos.


### Metodologia

O projeto apresentou uma metodologia linear que se preocupou em inicialmente tratar os dados e suprir ausências, para somente depois análisar o significado deles. A etapa da modelagem foi a última, visto que os conhecimentos e informações levantadas anteriormente sobre os dados foram importantes na tomada de decisões, como quais variáveis seriam realmente importantes na modelagem.

Abaixo tem-se mais detalhadamente o processo de construção de cada etapa:

1. Tratamento dos dados
> Essa etapa investigou os valores nulos e duplicados em cada coluna. Após a identificação de quais elementos possuiam esses valores indesejados, alguns foram substituidos por valores corretos encontrados em outros datasets. Ademais, outra operação realizada durante essa etapa foi a conversão de tipos de dados para facilitar as operações de análise do projeto. Por fim, também foi instrumentalizado a criação de novos atributos derivados de outros, como as colunas "Genre 1", "Genre 2" e "Genre 3" que foram originadas da coluna "Genre", foi através dessa modificação que foi possível encontrar os gêneros mais populares na tabela e os menos populares.
2. Análise inicial dos dados
> A segunda etapa observou informações gerais e superficiais dos dados, através dessas informações algumas pontuações foram feitas, como por exemplo, o diretor que possui mais filmes no dataset é Alfred Hitchcock e o ator é Robert De Niro. Outras conclusões referentes ao filme mais antigo e filme com maior bilheteria também foram discutidas.
3. Análise exploratória dos dados
> O foco principal foi responder os questionamentos que foram levantados na requisição do projeto e responder as 3 perguntas. Qual filme eu recomendaria para um desconhecido; Quais os fatores relacionados ao alto faturamento de um filme; Quais insights podem ser tirados da coluna Overview e se é possível inferiro gênero do filme a partir dela.
4. Etapa de previsão dos dados
> Basicamente é a aplicação da modelagem que foi feita nos arquivos gradient_boosting_model e random_forest_model. Também é detalhado algumas das escolhas que foram realizadas durante o desenvolvimento do projeto. E por fim, exibe a previsão da nota para o filme The Shawshank Redemption.


### Resultados
Todos os resultados estão armazenados no próprio notebook ou em gráficos e arquivos que foram salvos e estão disponíveis no repositório.

### Atualizações futuras
* Adicionar uma coluna relacionada ao gênero dos atores e diretores para investigar de forma mais detalhada padrões relacionados aos envolvidos nos filmes mais populares 
* Mapear os valores ausentes e verificar se é possível substituir eles por valores reais.
* Realizar o tratamento de dados nos 3 datasets externos.
* Verificar se em casos que a bilheteria se adequa a inflação com o decorrer dos anos algo mudaria na análise.
* Refatorar o código, sempre existe algo que pode ser reescrito de uma maneira mais elegante e inteligente.

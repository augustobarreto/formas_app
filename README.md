

### Sobre

APP desenvolvido para disponibilizar os modelos de OIE desenvolvidos pelo FORMAS


#### Instalar ambiente virtual e suas dependências

* Confira se o python global da sua máquina é o Python3.8 ou maior

    >     python --version

* Crie um ambiente virtual:

     >    python3 -m venv tutorial-env.


* Vá a pasta raíz da projeto e execute:

    >    pip install -r requirements.txt

* Iniciar servidor de desenvolvimento
    >       python manage.py runserver
    
#### Baixar os modelos do APP OIE (FlairOIE-PT)

Baixe os modelos pré-treinados e coloque na pasta 'train_output' do app OIE.
link: https://drive.google.com/drive/folders/1w_yTuIrfLOtluQogalxRTaRzef9dy2m3?usp=share_link

#### Deploy no Doku

* O Dockerfile foi desenvolvido com o objetivo de dockerizar a aplicação e permitir o deploy no ambiente disponibilizado pelo IC UFBA, através do Iaas - Dokku. Mais detalhes sobre o procedimento para deploy podem ser consultados em: https://graco-ufba.github.io/app/


# MockDatasetGenerator

##  Gerador de datasets mockiados


#### Tendo como base dicionário de colunas (coluna: data_type) e número de linhas é gerado dataframes com dados aleatórios.

#### Facilita testes offline e customizados de aplicações voltadas para engenharia de dados.
---

### Data types mapeados até o momento:
1. float
2. integer
3. name
4. email
5. cpf
6. datetime
7. simple string

### Exemplo de uso (pandas dataframe):

    df_gen = DataframeGenerator()

    columns = {
        'login_date': 'datetime',
        'user_document': 'cpf',
        'user_email': 'email',
        'user_name': 'name',
        'user_coins': 'integer',
        'pf_rarity': 'float'
    }

    df = df_generator.generate_pandas_df(columns_dict=columns, rows=10)
    print(df.to_string())

##### output:
            login_date   user_document                    user_email         user_name  user_coins  pf_rarity
    0  2024-05-21 14:36:22  061.724.518-55         RobertaTerri@voila.fr  Rhiannon Shiflet         583     583.94
    1  2026-11-19 03:57:38  752.754.056-77          EthelCeleste@live.ca   Jennifer Aurora         348     678.55
    2  2013-09-28 10:45:34  409.535.169-11             RyanSteve@live.nl     Trula Strader         208     554.56
    3  2020-09-24 00:28:38  827.667.413-56          CarolTerri@yahoo.com    Melanie Rhodes         615     853.53
    4  2013-03-04 12:15:42  480.459.818-90          DaisyPeter@chello.nl  Suzanne Crawford         719     676.25
    5  2023-03-06 00:49:49  905.079.631-13     JacquettaTheodore@neuf.fr      Corey Curran         919     530.09
    6  2025-11-17 11:02:02  867.536.375-32          HowardRoger@yahoo.co        Dale Carol         892     588.10
    7  2015-05-24 18:43:31  042.593.775-58             WayneNolan@tin.it   Madeline Garcia          90     827.09
    8  2014-01-06 13:50:54  510.814.562-48  GeorgeLatonya@windstream.net      Tracy Wright         278     389.34
    9  2014-03-07 22:18:57  701.283.606-74        DanielRobert@yandex.ru     Oscar Russell         428     774.04

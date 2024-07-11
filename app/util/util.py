import json


def remove_key_from_json_array(file_path, key_to_remove):
    # Ler o arquivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # percorrer todos objetos no array e remover a chave especifica
    for obj in data:
        if key_to_remove in obj:
            del obj[key_to_remove]
            print(f'Chave "{key_to_remove}" removida do objeto')

    # gravar o json atualizado de volta no arquivo
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


file_path = 'data.json'
key_to_remove = ['mae',"signo","pai","data_nasc","telefone_fixo","altura","peso","tipo_sanguineo"]
for key in key_to_remove:
    remove_key_from_json_array(file_path,key)

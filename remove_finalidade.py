import argparse
import json


def remove_finalidade(json_file_path):
    try:
        # Ler o arquivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Verificar se o JSON é uma lista de objetos
        if isinstance(data, list):
            for item in data:
                # Verificar e exibir o conteúdo da chave 'Finalidades' em cada objeto
                if 'Finalidades' in item:
                    # Remover a chave 'Finalidades' e seu conteúdo
                    del item['Finalidades']
                    print("A chave 'Finalidades' foi removida.")
                else:
                    print("A chave 'Finalidades' não existe em um dos objetos.")

        # Salvar o JSON atualizado de volta no arquivo
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"O arquivo JSON atualizado foi salvo em {json_file_path}.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def main():
    parser = argparse.ArgumentParser(description="Remove 'Finalidades' key from a JSON file.")
    parser.add_argument("--input", help="Input JSON file path", type=str)
    args = parser.parse_args()

    json_file_path = args.input
    remove_finalidade(json_file_path)


if __name__ == "__main__":
    main()

import re
from collections import Counter 

class File_reader:
    def display_data_from_file(self, file_path):
        try:
            if hasattr(file_path, 'read'):
                file_path.seek(0)
                content = file_path.read()
                print("f\n--- Conteúdo do arquivo criado/aberto ---")
                print(content)
                print("-------------------------------------------")
                return content
            else:
                with open (file_path, 'r', encoding="UTF-8") as file:
                    content = file.read()
                    print(f"\n--- Conteúdo de '{file_path}' ---")
                    print(content)
                    print("-------------------------------\n")
                    return content
        except FileNotFoundError:
            print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return None

    def create_file(self, filename="testfile.txt"):
        """
        Cria ou abre um arquivo para escrita.
        Retorna o caminho do arquivo criado/aberto.
        """
        try:
            with open(filename, "w", encoding="UTF-8") as f:
                print(f"Arquivo '{filename}' criado/aberto com sucesso para escrita")
            return filename
        except Exception as e:
            print(f"Erro ao criar/abrir o arquivo '{filename}': {e}")
            return None

    def write_to_file_interactively(self, file_path):
        """
        Permite ao usuário escrever conteúdo em um arquivo interativamente.
        """
        if file_path is None:
            print("Nenhum arquivo váçido selecionado para escrita.")
            return

        try:
            with open(file_path, "a", encoding="UTF-8") as file:
                print(f"\n--- Escrevendo em '{file_path}' (digite 'SAIR' em uma nova linha para terminar) ---")
                while True:
                    line = input("> ")
                    if line.upper() == "SAIR":
                        break
                    file.write(line + '\n')
            print(f"Escrita e, '{file_path}' concluída.")
        except Exception as e:
            print(f"Erro ao escrever no arquivo '{file_path}': {e}")

    def choose_file(self):
        """
        Permite ao usuário escolher um arquivo e retorna seu caminho.
        Valida a entrada do usuário.
        """
        file_path = None
        while file_path is None:
            option = input("Qual arquivo vai querer ler? Selecione entre 1, 2 ou 3: ")
            if option == '1':
                file_path = "random_text.txt"
            elif option == '2':
                file_path = "ran_num.txt"
            elif option == '3':
                file_path = self.create_file("testfile.txt")
            else:
                print("Opção inválida. Por favor, digite '1', '2' ou '3'.")
            return file_path
    
    def count_wd_from_file(self, file_path):
        """
        Conta a quantidade de palavras em um arquivo específico.
        """
        content = self.display_data_from_file(file_path)
        if content is None:
            print("Não foi possível contar as palavras devido a um erro de leitura.")
            return 0

        words = content.split()
        word_count = len(words)
        print(f"O arquivo '{file_path}' possui {word_count} palavras.")
        return word_count

    def most_shown(self, file_path, num_words=5):
        """
        Encontra e exibe as N palavras mais frequentes em um arquivo.
        """
        data = self.display_data_from_file(file_path)
        if data is None:
            print(f"Não foi possível processar o arquivo '{file_path}'.")
            return

        normalized_data = data.lower()
        words = re.findall(r'\b\w+\b', normalized_data)
        freq_words = Counter(words)
        most_common_words = freq_words.most_common(num_words)

        if not most_common_words:
            print(f"Não foi possível encontrar palavras no arquivo '{file_path}'.")
            return
        print(f"\nAs {num_words} palavras mais frequentes no arquivo '{file_path}':")
        for words, count in most_common_words:
            print(f"- {words}: {count} ocorrências")

    def calculate_avg_from_file(self, file_path):
        """
        Calcula a média dos números em um arquivo.
        Assume que cada linha no arquivo contém em número.
        """
        content = self.display_data_from_file(file_path)

        if content is None:
            print(f"Não foi possível calcular a média do arquivo '{file_path}'.")
            return

        numbers = []
        for line in content.splitlines():
            line = line.strip()
            if line:
                try:
                    num = float(line)
                    numbers.append(num)
                except ValueError:
                    print(f"Aviso: Ignorando linha não numérica: '{line}'")

        if not numbers:
            print(f"Nenhum número válido encontrado no arquivo '{file_path}'.")
            return None

        avg = sum(numbers) / len(numbers)
        print(f"A média dos números em '{file_path}' é: {avg:.2f}")
        return avg

    def process_chosen_file(self):
        """
        Gerencia a escolha do arquivo e as operações que podem ser feitas nele.
        """
        choose_file_path = self.choose_file()

        if choose_file_path:
            print("\n--- Opções para o arquivo selecionado ---")
            print("a: Contar palavras")
            print("b: Encontrar palavras mais frequentes")
            print("c: Calcular média dos números (se for ran_num.txt)")
            print("d: Escrever no arquivo (se for testfile.txt)")
            print("e: Sair das opções do arquivo")
            print("-------------------------------------------")

            while True:
                action = input("O que você quer fazer? (a, b, c, d ou e): ").lower()

                if action == 'a':
                    self.count_wd_from_file(choose_file_path)
                elif action == 'b':
                    self.most_shown(choose_file_path)
                elif action == 'c':
                    if choose_file_path == "ran_num.txt":
                        self.calculate_avg_from_file(choose_file_path)
                    else:
                        print("Essa opção é apenas para 'ran_num.txt'.")
                elif action == 'd':
                    if choose_file_path == "testfile.txt":
                        self.write_to_file_interactively(choose_file_path)
                    else:
                        print("Essa opção é apenas para 'testfile.txt' (o arquivo que você pode criar).")
                elif action == 'e':
                    print("Saindo das opções do arquivo.")
                    break
                else:
                    print("Opção inválida. Por favor, digite 'a', 'b', 'c', 'd' ou 'e'.")
        else:
            print("Nenhum arquivo foi selecionado ou ocorreu um erro.")

def main():
    reader = File_reader()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Escolher e processar um arquivo")
        print("2. Sair do Programa")
        print("----------------------")
        main_option = input("Escolha uma opção: ")

        if main_option == '1':
            reader.process_chosen_file()
        elif main_option == '2':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, digite '1' ou '2'.")

if __name__ == "__main__":
    main()


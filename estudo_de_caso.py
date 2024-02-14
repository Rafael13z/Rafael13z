class SistemaEstoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_produto(self, nome, preco, quantidade):
        self.estoque[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto {nome} adicionado com sucesso!")

    def atualizar_produto(self, nome):
        if nome in self.estoque:
            preco = float(input(f"Digite o novo preço para {nome}: "))
            quantidade = int(input(f"Digite a nova quantidade para {nome}: "))
            self.estoque[nome]['preco'] = preco
            self.estoque[nome]['quantidade'] = quantidade
            print(f"Produto {nome} atualizado com sucesso!")
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def visualizar_estoque(self):
        if self.estoque:
            print("Estoque:")
            for produto, info in self.estoque.items():
                print(f"Nome: {produto}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")
        else:
            print("O estoque está vazio.")

def main():
    sistema = SistemaEstoque()
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Visualizar estoque")
        print("4. Sair do sistema")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            sistema.adicionar_produto(nome, preco, quantidade)
        elif escolha == '2':
            nome = input("Digite o nome do produto a ser atualizado: ")
            sistema.atualizar_produto(nome)
        elif escolha == '3':
            sistema.visualizar_estoque()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

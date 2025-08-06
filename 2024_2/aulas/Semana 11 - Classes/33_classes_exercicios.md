# Orientação a Objetos: Exercícios

## 1. Sistema de Gestão de Biblioteca
- **Classe `Book`**:
  - Atributos:
    - `title`: (string) nome do livro.
    - `author`: (string) autor do livro.
    - `isbn`: (string) código ISBN do livro.
- **Classe `Library`**:
  - Atributos:
    - `books`: (lista) uma lista que armazena objetos `Book`.
  - Métodos:
    - `add_book(book)`: adiciona um objeto `Book` à lista de livros.
    - `remove_book(isbn)`: remove um livro da lista com base no ISBN. Se o livro não existir, deve exibir uma mensagem informando.
    - `search_by_title(title)`: procura um livro pelo título e retorna suas informações. Se não encontrado, deve exibir uma mensagem informando.
    - `search_by_author(author)`: procura livros pelo autor e retorna uma lista de livros correspondentes.

- **Testar**

    ```python
    class LibraryApp:
        def __init__(self):
            self.library = Library()

        def run(self):
            while True:
                print("\n--- Library Menu ---")
                print("1. Add Book")
                print("2. Remove Book")
                print("3. Search by Title")
                print("4. Search by Author")
                print("5. List All Books")
                print("6. Exit")

                choice = input("Choose an option: ")

                if choice == '1':
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    isbn = input("Enter book ISBN: ")
                    self.library.add_book(Book(title, author, isbn))

                elif choice == '2':
                    isbn = input("Enter book ISBN to remove: ")
                    self.library.remove_book(isbn)

                elif choice == '3':
                    title = input("Enter book title to search: ")
                    books = self.library.search_by_title(title)
                    if books:
                        for book in books:
                            print(book)
                    else:
                        print('No books found with that title.')

                elif choice == '4':
                    author = input("Enter author name to search: ")
                    books = self.library.search_by_author(author)
                    if books:
                        for book in books:
                            print(book)
                    else:
                        print('No books found by that author.')

                elif choice == '5':
                    self.library.list_books()

                elif choice == '6':
                    print('Exiting...')
                    break

                else:
                    print('Invalid choice, please try again.')


    if __name__ == "__main__":
        app = LibraryApp()
        app.run()
    ```

## 2. Sistema de Gerenciamento de Estoque
- **Classe `Product`**:
  - Atributos:
    - `name`: (string) nome do produto.
    - `quantity`: (int) quantidade disponível em estoque.
    - `price`: (float) preço do produto.
  - Métodos:
    - `__init__(self, name, quantity, price)`: inicializa um novo produto.
    - `update_quantity(self, amount)`: atualiza a quantidade do produto. O parâmetro `amount` pode ser positivo (para adicionar) ou negativo (para remover).
    - `get_info(self)`: retorna uma string com as informações do produto, incluindo nome, quantidade e preço.
- **Classe `Inventory`**:
  - Atributos:
    - `products`: (lista) uma lista que armazena objetos `Product`.
  - Métodos:
    - `__init__(self)`: inicializa um novo inventário vazio.
    - `add_product(self, product)`: adiciona um objeto `Product` à lista de produtos.
    - `remove_product(self, product_name)`: remove um produto da lista com base no nome. Se o produto não existir, deve exibir uma mensagem informando.
    - `list_products(self)`: exibe todos os produtos no inventário com suas informações.
    - `find_product(self, product_name)`: procura um produto pelo nome e retorna suas informações. Se não encontrado, deve exibir uma mensagem informando.

- **Testar**

    ```python
    class InventoryApp:
        def __init__(self):
            self.inventory = Inventory()

        def run(self):
            while True:
                print("\n--- Inventory Menu ---")
                print("1. Add Product")
                print("2. Remove Product")
                print("3. List Products")
                print("4. Find Product")
                print("5. Exit")

                choice = input("Choose an option: ")

                if choice == '1':
                    name = input("Enter product name: ")
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price: "))
                    self.inventory.add_product(Product(name, quantity, price))

                elif choice == '2':
                    name = input("Enter product name to remove: ")
                    self.inventory.remove_product(name)

                elif choice == '3':
                    self.inventory.list_products()

                elif choice == '4':
                    name = input("Enter product name to find: ")
                    info = self.inventory.find_product(name)
                    print(info)

                elif choice == '5':
                    print('Exiting...')
                    break

                else:
                    print('Invalid choice, please try again.')


    if __name__ == "__main__":
        app = InventoryApp()
        app.run()
    ```

## 3. Estrutura Básica de Classes: Jogo da Cobra
- **Classe `Snake`**:
  - Atributos:
    - `length`: (int) comprimento da cobra.
    - `direction`: (string) direção atual da cobra (ex: "cima", "baixo", "esquerda", "direita").
    - `position`: (tuple) posição atual da cabeça da cobra (x, y).
  - Métodos:
    - `move()`: atualiza a posição da cobra com base na direção atual.
    - `grow()`: aumenta o comprimento da cobra em 1 unidade.
    - `change_direction(new_direction)`: atualiza a direção da cobra.
    - `check_collision()`: verifica se a cobra colide consigo mesma ou com as bordas do jogo. Retorna um booleano.

## 4. Herança: Power-ups no Jogo da Cobra
- **Classe base `PowerUp`**:
  - Atributos:
    - `position`: (tuple) posição do power-up (x, y).
    - `duration`: (int) duração do efeito do power-up em segundos.
- **Subclasses**:
  - `SpeedBoost`: aumenta a velocidade da cobra temporariamente.
  - `SlowDown`: diminui a velocidade da cobra temporariamente.
  - `Grow`: aumenta o comprimento da cobra temporariamente.
- Métodos:
  - `apply(snake)`: aplica o efeito do power-up à cobra.
  - `expire(snake)`: remove o efeito do power-up da cobra após a duração expirar.

## 5. Estrutura Básica de Classes: Jogo Tetris (Rotação de Peças)
- **Classe `TetrisPiece`**:
  - Atributos:
    - `shape`: (lista de listas) representa a forma da peça.
    - `position`: (tuple) posição atual da peça na grade (x, y).
    - `orientation`: (int) orientação atual da peça em graus (0, 90, 180, 270).
  - Métodos:
    - `rotate()`: altera a orientação da peça 90 graus no sentido horário.
    - `move_left()`, `move_right()`, `move_down()`: desloca a peça na grade na direção especificada.
    - `check_collision()`: verifica se a peça colide com as paredes ou outras peças. Retorna um booleano.

## 6. Herança: Peças de Tetris
- **Classe base `TetrisPiece`**:
  - Atributos:
    - `shape`: (lista de listas) forma da peça.
    - `color`: (string) cor da peça.
- **Subclasses**:
  - `LinePiece`, `SquarePiece`, `TPiece`, etc., cada uma com formas iniciais únicas.
- Métodos:
  - `rotate()`: sobrescreve o método de rotação, se necessário, para peças que se comportam de maneira diferente.
  - `move_left()`, `move_right()`, `move_down()`: cada peça pode ter implementações específicas de movimentação.

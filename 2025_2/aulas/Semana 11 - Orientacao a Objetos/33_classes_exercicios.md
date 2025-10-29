# Lista de Exercícios: Orientação a Objetos básico

## **1. Controle de Estoque**

Implemente um programa orientado a objetos com as classes **Produto**, **Vendedor**, **Fornecedor** e **Estoque**, conforme as especificações a seguir.

1. A classe **Produto** deve conter os atributos: nome, valor, categoria e quantidade.
2. A classe **Vendedor** deve conter: código único e nome.
3. A classe **Fornecedor** deve conter: nome e CNPJ.
4. A classe **Estoque** deve armazenar uma lista de produtos e oferecer os seguintes métodos:

   * **Cadastrar produto**: insere um novo item no estoque.
   * **Entrada de produto**: aumenta a quantidade de determinado produto (ex.: reposição ou compra de fornecedor).
   * **Saída de produto**: reduz a quantidade de determinado produto (ex.: venda por um vendedor).
   * **Auditoria**: informa, para cada produto, a quantidade total retirada por vendedor.

Você pode definir **quais argumentos** cada método deve receber (por exemplo, nome do produto, código, quantidade, vendedor, etc.), desde que o funcionamento geral do programa atenda ao enunciado.

**Demonstração mínima:**
Crie um exemplo de uso contendo pelo menos **3 produtos** e **2 vendedores**, realizando operações de entrada e saída, e exibindo o resultado da auditoria.

## **2. Encapsulamento e propriedades**

A partir da solução anterior, refatore o código aplicando **encapsulamento**.

Regras:

1. Nenhum atributo pode ser acessado diretamente fora da classe.
2. Utilize `@property` e `@<atributo>.setter` sempre que houver necessidade de validação ou acesso controlado.
3. Métodos de uso interno devem ser marcados como privados (prefixo `_`).
4. Reproduza o mesmo exemplo de uso do exercício anterior, garantindo que o comportamento permaneça correto.

## **3. Refatoração e coesão de classes**

Analise o código abaixo:

```python
class Pedido:
    def __init__(self, valor_total):
        self.valor_total = valor_total

    def calcular_desconto(self, cliente_vip):
        if cliente_vip:
            self.valor_total *= 0.9

    def gerar_nota_fiscal(self):
        print(f"Nota fiscal: valor total = R${self.valor_total:.2f}")

    def salvar_log(self):
        with open("log.txt", "a") as f:
            f.write(f"Pedido processado: R${self.valor_total:.2f}\n")
```

a) Avalie o código em termos de **coesão**, **acoplamento** e **facilidade de manutenção e extensão**.

b) Proponha uma **refatoração** que separe responsabilidades em classes mais coesas (por exemplo: `Pedido`, `NotaFiscal`, `Logger`, `CalculadoraDeDesconto`).

c) Apresente um **exemplo de funcionamento** da nova estrutura.

## **4. Modelagem - Jogo da Forca**

O jogo da forca é um jogo de adivinhação no qual o jogador tenta descobrir uma **palavra secreta** escolhida aleatoriamente a partir de um arquivo chamado `palavras_secretas.txt`.

**Regras do jogo:**

* No início, o programa seleciona uma palavra secreta e exibe na tela seus caracteres ocultos com `_`.
* A cada rodada, o jogador digita uma letra:

  * Se a letra estiver na palavra, ela deve ser revelada em todas as posições corretas.
  * Caso contrário, o jogo deve indicar que o palpite foi incorreto.
* O jogo continua até que o jogador descubra todas as letras ou até que o limite de erros seja atingido (Game Over).
* Durante o jogo, o programa deve exibir algo como:

```
Palavra: a _ g _ _ _ _ _ _
Palpites: a, b, z, g
Palpite? <nova letra>
```

**Tarefas:**

a) Descreva **quais classes** seriam necessárias para representar esse jogo de forma orientada a objetos.

b) Liste os **principais atributos** e **métodos** de cada classe.

c) Explique como adaptaria o projeto caso o número máximo de erros fosse **limitado a N tentativas**.

Não é necessário implementar o código - apenas **propor a modelagem** e justificar brevemente suas escolhas.

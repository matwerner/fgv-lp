# Níveis de Depuração de Código

Depuração é o processo de encontrar e corrigir erros em um programa de computador.
Independentemente da experiência do programador, erros são comuns e inevitáveis.
Portanto, saber como depurar código eficientemente é uma habilidade essencial para qualquer desenvolvedor.
Nesta aula, vamos explorar diferentes níveis de depuração, desde técnicas básicas até estratégias avançadas.

## 1. Nível Básico: Depuração Manual

### 1.1 Uso de Mensagens de Impressão

Uma das formas mais simples de depurar código é usar a função `print()` para exibir valores de variáveis e mensagens no console. Isso ajuda a entender o que está acontecendo em diferentes partes do código.

```python
def calcular_soma(a, b):
    print(f"Calculando a soma de {a} e {b}")  # Mensagem de depuração
    return a + b

resultado = calcular_soma(5, 3)
print(f"Resultado: {resultado}")
```

Vantagens:
* Simples de implementar.
* Útil para rastrear o fluxo de execução e valores de variáveis.

Desvantagens:
* Pode gerar muito output, tornando difícil encontrar informações relevantes.
* Não é eficiente para programas complexos ou de larga escala.

Quando Usar:
* **Ideal para problemas simples**:
Use `print()` quando estiver lidando com erros de lógica ou comportamento inesperado em partes específicas do código.
* **Rápida verificação**:
Quando você precisa de uma resposta rápida sobre o estado de uma variável ou para verificar se uma parte do código está sendo executada.
* **Projetos pequenos ou scripts**:
Adequado para projetos de pequena escala ou scripts curtos, onde a complexidade é mínima.

### 1.2 Verificação Visual

Ler e revisar o código com atenção para identificar erros de sintaxe ou lógicos. Algumas dicas incluem:
* Verificar indentação correta (especialmente em linguagens como Python).
* Conferir o uso correto de parênteses e chaves.
* Procurar por erros comuns, como variáveis não inicializadas ou uso incorreto de operadores.

Vantagens:
* Ajuda a desenvolver habilidades de leitura de código.
* Pode encontrar erros óbvios que passam despercebidos por testes automatizados.

Desvantagens:
* Pode ser demorado para códigos grandes.
* Erros sutis ou complexos podem não ser detectados apenas com a leitura.

Quando Usar:
* **Erros de sintaxe e formatação**:
Use a verificação visual para identificar problemas evidentes de sintaxe, formatação ou lógica básica.
* **Revisão de código**:
Ideal para revisões de código em equipe, onde múltiplos olhos podem detectar erros que passam despercebidos por uma única pessoa.

### 1.3 Testes Manuais

Executar o programa com diferentes entradas e observar se os resultados são os esperados.
Isso ajuda a identificar falhas em cenários específicos.

```python
# Testando manualmente a função de soma
print(calcular_soma(10, 5))  # Deve imprimir 15
print(calcular_soma(-3, 3))  # Deve imprimir 0
```

Vantagens:
* Facilita a identificação de cenários de falha específicos.
* Útil para testes iniciais e desenvolvimento rápido.

Desvantagens:
* Propenso a erros humanos.
* Não é escalável para testar todos os cenários possíveis em programas complexos.

Quando Usar:
* **Validação inicial**:
Use testes manuais para validar rapidamente novas funcionalidades ou correções.
* **Experimentação e prototipagem**:
Adequado para projetos em fase inicial, onde a velocidade de desenvolvimento é crucial.

## 2. Nível Intermediário: Uso de Ferramentas de Depuração

### 2.1 Depuradores Integrados

Ambientes de Desenvolvimento Integrados (IDEs) como
[Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging)
e [PyCharm](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html) 
oferecem depuradores que permitem:
* **Definir Breakpoints**:
Pontos no código onde a execução será pausada para análise.
* **Executar Passo a Passo**:
Permite executar o código linha por linha, observando como o estado do programa muda.
* **Inspecionar Variáveis**:
Visualizar o valor atual das variáveis em qualquer ponto durante a execução.

Vantagens:
* Fornece uma visão detalhada do comportamento do programa.
* Permite pausar e retomar a execução em pontos específicos.
* Facilita a identificação de problemas em loops e funções complexas.

Desvantagens:
* Pode ser complexo para iniciantes.
* Requer um ambiente de desenvolvimento configurado corretamente.

Quando Usar:
* **Depuração de problemas complexos**:
Use depuradores integrados para investigar bugs complexos ou para entender o fluxo de execução de código em projetos grandes.
* **Análise de loops e funções recursivas**:
Ideal para depurar código que envolve lógica complexa e múltiplas chamadas de funções.

### 2.2 Exploração de Pilhas de Chamada

A pilha de chamadas mostra a sequência de funções que foram chamadas até o ponto atual de execução.
Isso é útil para entender o contexto de um erro, especialmente em casos de chamadas recursivas ou funções aninhadas.

```python
def funcao_a():
    funcao_b()

def funcao_b():
    funcao_c()

def funcao_c():
    print("Dentro de funcao_c")

funcao_a()
```

### 2.3 Mensagens de Erro Detalhadas

Aprender a interpretar mensagens de erro pode fornecer pistas importantes sobre o que deu errado:
* **IndexError**:
Tentativa de acessar um índice que não existe em uma lista.
* **TypeError**:
Operação inválida para um tipo de dado (por exemplo, somar uma string com um número).
* **SyntaxError**:
Erro de sintaxe, como esquecer um parêntese ou dois pontos.

## 3. Nível Avançado: Testes Automatizados

Implementar testes unitários para verificar se cada parte do código funciona como esperado.
Isso é feito usando frameworks de teste, como unittest em Python ou JUnit em Java.

```python

import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma_positiva(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
```

Vantagens:
* Automatiza o processo de verificação de erros.
* Facilita a manutenção e evolução do código ao longo do tempo.
* Aumenta a confiança de que as alterações no código não introduziram novos bugs.

Desvantagens:
* Requer tempo e esforço inicial para configurar e escrever testes.
* Pode não cobrir todos os cenários possíveis.

Quando Usar:
* **Projetos de longa duração**:
Use testes automatizados em projetos que precisam de manutenção contínua e onde mudanças frequentes no código são esperadas.
* **Cobertura de código**:
Ideal para garantir que partes críticas do código sejam testadas consistentemente.
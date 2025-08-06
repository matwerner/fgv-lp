class Pagamento:

    def __init__(self, valor, data, status):
        self.valor = valor           # Atributo de instância
        self.data = data             # Atributo de instância
        self.status = status         # Atributo de instância

    def info(self):
        """Retorna informações básicas sobre o pagamento."""
        return f"Pagamento de R${self.valor:.2f} a ser pago até {self.data}. Status: {self.status}."
    
    def executar_operacao(self):
        raise NotImplemented('Implemente agora!')

pag = Pagamento(100, '2024-10-18', 'pendente')
print(pag.info())

class PagamentoCartaoCredito(Pagamento):

    def __init__(self, valor: float, data: str, status: str, n_cartao: str):
        super().__init__(valor, data, status)
        if not self.__validar(n_cartao):
            raise ValueError('Numero invalido')
        self.n_cartao = n_cartao

    def __validar(self, n_cartao: str) -> bool:
        return True
    
    def info(self):
        msg_base = super().info()
        msg = msg_base + f'\nNumero do cartao: {self.n_cartao}'
        return msg

    def executar_operacao(self):
        print("Executou tambem!")

class PagamentoPix(Pagamento):

    def __init__(self, valor: float, data: str, status: str, chave_devedor, chave_credor):
        super().__init__(valor, data, status)
        if not self.__validar_chave(chave_devedor):
            raise ValueError('Chave do devedor invalida')
        if not self.__validar_chave(chave_credor):
            raise ValueError('Chave do credor')
        self.chave_devedor = chave_devedor
        self.chave_credor = chave_credor
    
    def __validar_chave(self, chave):
        return True
    
    def info(self):
        msg_base = super().info()
        msg = msg_base + f'\nChave credor: {self.chave_credor}'
        msg = msg + f'\nChave devedor: {self.chave_devedor}'
        return msg
    
    def executar_operacao(self):
        print("Executou!")


pix = PagamentoPix(1_000, '2020-01-01', 'Pago', '111.111.111.90', '24232u5rhljtilwhnuvp8g')
cred = PagamentoCartaoCredito(10_000, '2024-01-01', 'Processando', '5561 0689 1331 4792')

print(pix.chave_credor)
print(cred.n_cartao)

print(pix.data)
print(cred.data)

print()
print(pix.info())
print()
print(cred.info())


print(pix.executar_operacao())
print(cred.executar_operacao())
class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = self._verificar_nome(nome)
        self.idade = self._verificar_idade(idade)


    def _verificar_nome(self, valor):
        """Método para verificação de nome"""
        self._verificar_nome_tipo_invalido(valor)
        self. _verificar_nome_vazio_invalido(valor)
        self.nome = valor
        return self.nome
       

    def _verificar_nome_tipo_invalido(self, valor):        
            """Metodos auxiliares para verificação de string"""
            if not isinstance(valor, str):
                raise TypeError("O nome deve ser um texo.")
            
    def _verificar_nome_vazio_invalido(self, valor: str):
        """Metodos auxiliares para verificação de string"""
        if not valor.strip():
            raise TypeError("O nome não deve estar vazio.")


    def _verificar_idade(self, valor):
        """Método para veriicação de tipo de idade"""
        self._verificar_idade_tipo_invalido(valor)
        self._verificar_idade_acima_de_130(valor)
        self._verificar_idade_negativa(valor)

        self.idade = valor
        return self.idade
        

    """Metodos auxiliares"""
    def _verificar_idade_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("A idade deve ser um numero inteiro.")
        
    def _verificar_idade_acima_de_130(self, valor):
         """Método auxiliar para verificação de idade acima de 130."""
         if valor > 130:
            raise ValueError("A idade não pode ser acima de 130 anos.")

    def _verificar_idade_negativa(self, valor):
         """Metodos auxiliar para verificação de idade abaixo de zero"""
         if valor < 0:
            raise ValueError("A idade não pode ser negativa.") 


   # def _verificar_idade(self, valor):
    #    if valor < 0:
     #       raise ValueError("A idade não pode ser negativa.") 

      #  if valor > 130:
       #     raise ValueError("A idade não pode ser acima de 130 anos.")

        #if not isinstance(valor, int):
         #   raise TypeError("A idade tem que ser do tipo inteiro")

        #self.idade = valor
        #return self.idade

        
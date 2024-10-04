import pytest
from models.pessoa import Pessoa


@pytest.fixture
def pessoa_valida():

    pessoa = Pessoa("Marta", 22)
    return pessoa


def test_pessoa_nome_valida(pessoa_valida):
    assert pessoa_valida.nome == "Marta"


def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22 

def test_pessoa_idade_negativa_retorna_mensagem():
    with pytest.raises(ValueError, match="A idade não pode ser negativa."):
        Pessoa("Marta", -22)
     

def test_idade_acima_130anos():
        with pytest.raises(ValueError, match="A idade não pode ser acima de 130 anos."):
            Pessoa("Marta", 131)

def test_pessoa_idade_tipo_invalido_negativa_retorna_mensagem():
    with pytest.raises(TypeError, match="A idade deve ser um numero inteiro."):
        Pessoa("Marta", "-22")

def verificar_nome_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texo."):
        Pessoa(22, 22)

def test_pessoa_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Pessoa("", 22)
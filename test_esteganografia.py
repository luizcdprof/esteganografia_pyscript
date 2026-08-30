import pytest
from esteganografia import texto_para_binario, binario_para_texto, aplicar_lsb, extrair_lsb, DELIMITADOR

def test_conversao_texto_binario():
    texto = "Oi"
    binario = texto_para_binario(texto)
    assert binario == "0100111101101001"
    assert binario_para_texto(binario) == texto

def test_aplicar_e_extrair_lsb():
    # Criando 256 pixels no formato RGBA (4 valores por pixel)
    pixels_falsos = [200, 150, 100, 255] * 256
    mensagem = "Teste"
    
    bits = texto_para_binario(mensagem + DELIMITADOR)
    pixels_modificados = aplicar_lsb(pixels_falsos, bits)
    
    assert pixels_modificados != pixels_falsos
    
    mensagem_recuperada = extrair_lsb(pixels_modificados)
    assert mensagem_recuperada == mensagem
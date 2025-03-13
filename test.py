import unittest
from predicado import extraia_predicado

class TestPredicado(unittest.TestCase):

    def test_identifica_predicado_1(self):
        frase = 'Agenor era lindo.'
        self.assertEqual(extraia_predicado(frase), 'era lindo')

    def test_identifica_predicado_2(self):
        frase = 'O cachorro latiu alto na rua.'
        self.assertEqual(extraia_predicado(frase), 'latiu alto na rua')

    def test_identifica_predicado_3(self):
        frase = 'A menina brincava no parque.'
        self.assertEqual(extraia_predicado(frase), 'brincava no parque')

    def test_identifica_predicado_4(self):
        frase = 'O professor explicou a matéria com detalhes.'
        self.assertEqual(extraia_predicado(frase), 'explicou a matéria com detalhes')

    def test_identifica_predicado_5(self):
        frase = 'Ela estudou a noite inteira.'
        self.assertEqual(extraia_predicado(frase), 'estudou a noite inteira')

    def test_identifica_predicado_6(self):
        frase = 'João escreveu uma carta para sua mãe.'
        self.assertEqual(extraia_predicado(frase), 'escreveu uma carta para sua mãe')

    def test_identifica_predicado_7(self):
        frase = 'Nós andamos pela cidade ontem.'
        self.assertEqual(extraia_predicado(frase), 'andamos pela cidade ontem')

    def test_identifica_predicado_8(self):
        frase = 'Pedro dormiu profundamente depois da prova.'
        self.assertEqual(extraia_predicado(frase), 'dormiu profundamente depois da prova')

    def test_identifica_predicado_9(self):
        frase = 'O cantor cantou uma música emocionante.'
        self.assertEqual(extraia_predicado(frase), 'cantou uma música emocionante')

    def test_identifica_predicado_10(self):
        frase = 'A criança correu rapidamente para os braços da mãe.'
        self.assertEqual(extraia_predicado(frase), 'correu rapidamente para os braços da mãe')

    def test_identifica_predicado_11(self):
        frase = 'O pássaro voou alto no céu.'
        self.assertEqual(extraia_predicado(frase), 'voou alto no céu')

    def test_identifica_predicado_12(self):
        frase = 'O aluno falou sobre seu projeto na feira de ciências.'
        self.assertEqual(extraia_predicado(frase), 'falou sobre seu projeto na feira de ciências')

    def test_identifica_predicado_13(self):
        frase = 'A luz estava acesa até tarde.'
        self.assertEqual(extraia_predicado(frase), 'estava acesa até tarde')

    def test_identifica_predicado_14(self):
        frase = 'O vento será forte no final da tarde.'
        self.assertEqual(extraia_predicado(frase), 'será forte no final da tarde')

    def test_identifica_predicado_15(self):
        frase = 'O carro foi muito rápido na corrida.'
        self.assertEqual(extraia_predicado(frase), 'foi muito rápido na corrida')

    def test_identifica_predicado_16(self):
        frase = 'Maria estaria estudando se não estivesse doente.'
        self.assertEqual(extraia_predicado(frase), 'estaria estudando se não estivesse doente')


if __name__ == '__main__':
    unittest.main()
import unittest
from predicado import extraia_predicado

class TestPredicado(unittest.TestCase):

    def test_identifica_predicado_1(self):
        frase = 'Agenor era lindo.'
        self.assertEqual('era lindo', extraia_predicado(frase))

    def test_identifica_predicado_2(self):
        frase = 'O cachorro latiu alto na rua.'
        self.assertEqual('latiu alto na rua', extraia_predicado(frase))

    def test_identifica_predicado_3(self):
        frase = 'A menina brincava no parque.'
        self.assertEqual('brincava no parque', extraia_predicado(frase))

    def test_identifica_predicado_4(self):
        frase = 'O professor explicou a matéria com detalhes.'
        self.assertEqual('explicou a matéria com detalhes', extraia_predicado(frase))

    def test_identifica_predicado_5(self):
        frase = 'Ela estudou a noite inteira.'
        self.assertEqual('estudou a noite inteira', extraia_predicado(frase))

    def test_identifica_predicado_6(self):
        frase = 'João escreveu uma carta para sua mãe.'
        self.assertEqual('escreveu uma carta para sua mãe', extraia_predicado(frase))

    def test_identifica_predicado_7(self):
        frase = 'Nós andamos pela cidade ontem.'
        self.assertEqual('andamos pela cidade ontem', extraia_predicado(frase))

    def test_identifica_predicado_8(self):
        frase = 'O cantor cantou uma música emocionante.'
        self.assertEqual('cantou uma música emocionante', extraia_predicado(frase))

    def test_identifica_predicado_9(self):
        frase = 'A criança correu rapidamente para os braços da mãe.'
        self.assertEqual('correu rapidamente para os braços da mãe', extraia_predicado(frase))

    def test_identifica_predicado_10(self):
        frase = 'O pássaro voou alto no céu.'
        self.assertEqual('voou alto no céu', extraia_predicado(frase))

    def test_identifica_predicado_11(self):
        frase = 'O aluno falou sobre seu projeto na feira de ciências.'
        self.assertEqual('falou sobre seu projeto na feira de ciências', extraia_predicado(frase))

    def test_identifica_predicado_12(self):
        frase = 'A luz estava acesa até tarde.'
        self.assertEqual('estava acesa até tarde', extraia_predicado(frase))

    def test_identifica_predicado_13(self):
        frase = 'O vento será forte no final da tarde.'
        self.assertEqual('será forte no final da tarde', extraia_predicado(frase))

    def test_identifica_predicado_14(self):
        frase = 'O carro foi muito rápido na corrida.'
        self.assertEqual('foi muito rápido na corrida', extraia_predicado(frase))

    def test_identifica_predicado_15(self):
        frase = 'Maria estaria estudando se não estivesse doente.'
        self.assertEqual('estaria estudando se não estivesse doente', extraia_predicado(frase))


if __name__ == '__main__':
    unittest.main()
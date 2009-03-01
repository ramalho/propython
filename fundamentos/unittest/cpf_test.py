# cpf_test.py

# cpf_test.py versao 2.1 20/12/2000
# 2.1: extraímos calcular_dc da função checar_cpf
# 2.0: não aceita CPFs como 111.111.111-11, 222.222.222-22 etc.

import unittest
from cpf import checar_cpf, so_digitos, calcular_dc

class Teste_CPF_Original(unittest.TestCase):
	def teste_valido(self):
		cpf_in	= '269504278-75'
		cpf_out = '269.504.278-75'
		assert checar_cpf(cpf_in) == cpf_out, 'cpf válido retornou diferente'

	def teste_valido2(self):
		cpf_in = '26950427875'
		cpf_out = '269.504.278-75'
		assert checar_cpf(cpf_in) == cpf_out, 'cpf válido retornou diferente'

	def teste_validos(self):
		lt_validos_in = ['289573458-50','033442686-35','25519774870',
			'28983542870','004.150.028-85',' 296.171.678.08 ',
			'08789778804','249018338-98','274.642.198-48']
		lt_validos_out = ['289.573.458-50','033.442.686-35','255.197.748-70',
			'289.835.428-70','004.150.028-85','296.171.678-08',
			'087.897.788-04','249.018.338-98','274.642.198-48']
		for cpf_in, cpf_out in map(None,lt_validos_in, lt_validos_out):
			assert checar_cpf(cpf_in) == cpf_out, 'cpf %s retornou %s' % (cpf_in, checar_cpf(cpf_in))

	def teste_invalido_rep1(self):
		cpf_in = '11111111111'
		assert checar_cpf(cpf_in) == None, 'cpf válido mas com repetição retornou não None'

	def teste_invalido_rep2(self):
		lt_invalidos = []
		for d in range(10):
			lt_invalidos.append(str(d)*11)
		for cpf in lt_invalidos:
			assert checar_cpf(cpf) == None, 'cpf %s retornou não None' % cpf

	def teste_invalido_123(self):
		cpf = '123.123.123-11'
		assert checar_cpf(cpf) == None, 'cpf tipo 123 retornou não None'

	def teste_invalido(self):
		cpf = '269504278-76'
		assert checar_cpf(cpf) == None, 'cpf inválido retornou não None'

	def teste_invalidos(self):
		lt_invalidos = ['2895743458-50','023442686-35','5519774870','18983542870',
			'004.150.028-86','296.a71.678.08','1234567890']
		for cpf in lt_invalidos:
			assert checar_cpf(cpf) == None, 'cpf inválido retornou não None'

	def teste_so_digitos1(self):
		cpf_hifen = '269504278-75'
		cpf = '26950427875'
		assert cpf == so_digitos(cpf_hifen)

	def teste_so_digitos2(self):
		cpf_pt = 'aaa269.504.278-75!!'
		cpf = '26950427875'
		assert cpf == so_digitos(cpf_pt)

	def teste_calculos_dc(self):
		lt_validos = ['289573458-50','033442686-35','25519774870',
			'28983542870','004.150.028-85',' 296.171.678.08 ',
			'08789778804','249018338-98','274.642.198-48']
		for cpf in lt_validos:
			cpf_digitos = so_digitos(cpf)
			num = cpf_digitos[:-2]
			assert calcular_dc(num) == cpf_digitos[-2:], 'cpf %s retornou dc = %s' % (cpf, cpf[-2:])


def suite():
	suite = unittest.makeSuite(Teste_CPF_Original, 'teste_')
	return suite

if __name__ == '__main__':
	unittest.TextTestRunner().run(suite())


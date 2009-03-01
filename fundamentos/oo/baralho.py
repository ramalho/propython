>>> naipes = ['espadas','copas','ouros','paus']
>>> cartas = [str(x) for x in range(2,11)] + ['J','Q','K','A']
>>> baralho = [(carta,naipe) for carta in cartas for naipe in naipes]
>>> baralho
[('2', 'espadas'), ('2', 'copas'), ('2', 'ouros'), ('2', 'paus'), 
 ('3', 'espadas'), ('3', 'copas'), ('3', 'ouros'), ('3', 'paus'), 
 ('4', 'espadas'), ('4', 'copas'), ('4', 'ouros'), ('4', 'paus'), 
 ('5', 'espadas'), ('5', 'copas'), ('5', 'ouros'), ('5', 'paus'),
 ('6', 'espadas'), ('6', 'copas'), ('6', 'ouros'), ('6', 'paus'),
 ('7', 'espadas'), ('7', 'copas'), ('7', 'ouros'), ('7', 'paus'),
 ('8', 'espadas'), ('8', 'copas'), ('8', 'ouros'), ('8', 'paus'),
 ('9', 'espadas'), ('9', 'copas'), ('9', 'ouros'), ('9', 'paus'),
 ('10', 'espadas'), ('10', 'copas'), ('10', 'ouros'), ('10', 'paus'),
 ('J', 'espadas'), ('J', 'copas'), ('J', 'ouros'), ('J', 'paus'),
 ('Q', 'espadas'), ('Q', 'copas'), ('Q', 'ouros'), ('Q', 'paus'), 
 ('K', 'espadas'), ('K', 'copas'), ('K', 'ouros'), ('K', 'paus'),
 ('A', 'espadas'), ('A', 'copas'), ('A', 'ouros'), ('A', 'paus')]
>>>

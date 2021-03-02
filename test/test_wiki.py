import unittest


class TestWiki(unittest.TestCase):
    def setUp(self):
        self.lat = 35.6761919
        self.lng = 139.6503106

        self.result_page = {'query': {'geosearch':
                                          [{'pageid': 63573}
                                           ]}}
        self.result_description = {'query':
                                       {'pages':
                                            {'63573':
                                                 {'extract':
                                                      "Machu Picchu (du quechua machu : vieille, et pikchu : "
                                                      "montagne, sommet) "
                                                      " est une ancienne cité inca du XVe siècle au Pérou, perchée sur"
                                                      "un promontoire rocheux qui unit les monts Machu Picchu et "
                                                      "Huayna Picchu "
                                                      "(« le Jeune Pic » en  quechua) sur le versant oriental des "
                                                      "Andes centrales. "
                                                      "Son nom aurait été Pikchu ou Picho.\nSelon des documents du "
                                                      "XVIe siècle, trouvés par "
                                                      "l'archéologue américain Hiram Bingham, professeur assistant "
                                                      "d'histoire de l'Amérique latine "
                                                      "à l’université Yale, Machu Picchu aurait dû être une des "
                                                      "résidences de l’empereur Pachacútec. "
                                                      "Cependant, quelques-unes des plus grandes constructions et le "
                                                      "caractère cérémonial de la principale "
                                                      "voie d’accès au llaqta démontreraient que le lieu fut utilisé "
                                                      "comme un sanctuaire religieux. "
                                                      " Les deux usages ne s’excluent pas forcément."}

                                             }}}

    def get_pageid(self):
        return self.result_page['query']['geosearch'][0]['pageid']

    def test_get_page(self):
        get_page = self.result_page['query']['geosearch'][0]['pageid']
        self.assertEqual(get_page, 63573)

    def test_get_description(self):
        get_description = self.result_description["query"]["pages"][str(self.get_pageid())]["extract"]
        self.assertIn("(« le Jeune Pic » en  quechua)", get_description)

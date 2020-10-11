import json
import unittest

from utils import get_entities


class TestGetEntities(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual([], get_entities(""))

    def test_single_entry(self):
        expected = ['エントリ']
        actual = get_entities("括弧でくくられた[[エントリ]]を取り出す")
        self.assertEqual(expected, actual)

    def test_none_param(self):
        with self.assertRaises(TypeError):
            get_entities(None)

    def setUp(self):
        """
        テストメソッドの開始前に実行したい前処理
        """
        print('setUp')

    def tearDown(self):
        """
        テストメソッドの終了後に実行したい後処理
        """
        print('tearDown')

    @classmethod
    def setUpClass(cls):
        """
        テストクラスの開始前に実行したい前処理
        """
        print('setUpClass')
        with open('./contents.json') as f:
            data = json.load(f)
        cls.contents = cls.get_contents(data)

    @classmethod
    def tearDownClass(cls):
        """
        テストクラスの終了後に実行したい後処理
        """
        print('tearDownClass')

    @classmethod
    def get_contents(cls, data):
        for key in data['query']['pages']:
            revision = data['query']['pages'][key]['revisions'][0]
            contents = revision['*']
            return contents

    def test_actual_contents(self):
        actual = get_entities(self.contents)
        self.assertEqual(223, len(actual))
        self.assertEqual('File:Prog_one.png', actual[0])
        self.assertEqual('Category:ソフトウェア開発工程', actual[-1])


if __name__ == '__main__':
    unittest.main()

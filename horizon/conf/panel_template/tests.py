from horizon import test


class {{ panel_name|title}}Tests(test.TestCase):
    # Unit tests for {{ panel_name }}.
    def test_me(self):
        self.assertTrue(1 + 1 == 2)

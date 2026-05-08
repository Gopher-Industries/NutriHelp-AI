import unittest

from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend


class DomainGuardTests(unittest.TestCase):
    def setUp(self):
        self.backend = GroqChromaBackend()

    def test_gluten_allergy_cereal_question_is_in_scope(self):
        self.assertTrue(
            self.backend._is_nutrition_domain_prompt(
                "If I'm allergic to gluten, can I still eat cereal?"
            )
        )

    def test_common_food_allergy_question_is_in_scope(self):
        self.assertTrue(
            self.backend._is_nutrition_domain_prompt(
                "I have a peanut allergy. What snacks should I avoid?"
            )
        )

    def test_non_food_allergy_question_is_out_of_scope(self):
        self.assertFalse(
            self.backend._is_nutrition_domain_prompt(
                "I'm allergic to cats. What medicine should I take?"
            )
        )

    def test_unrelated_general_knowledge_question_is_out_of_scope(self):
        self.assertFalse(
            self.backend._is_nutrition_domain_prompt(
                "Who won the FIFA World Cup in 2018?"
            )
        )


if __name__ == "__main__":
    unittest.main()

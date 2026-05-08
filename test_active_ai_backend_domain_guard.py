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

    def test_expanded_diet_terms_are_in_scope(self):
        in_scope_prompts = [
            "Can you make a vegan meal plan for me?",
            "Is pasta okay for a low-carb diet?",
            "Which cereals are dairy-free and nut-free?",
            "How much sugar and salt is too much?",
            "Does malt flour contain gluten?",
            "What high-protein vegetarian breakfast can I eat?",
            "What allergens should I check for in bread and noodles?",
        ]

        for prompt in in_scope_prompts:
            with self.subTest(prompt=prompt):
                self.assertTrue(self.backend._is_nutrition_domain_prompt(prompt))

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

import unittest

from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend


class DomainGuardTest(unittest.TestCase):
    def setUp(self):
        self.backend = GroqChromaBackend()

    def test_accepts_food_and_nutrition_questions(self):
        prompts = [
            "Is strawberry good for my health?",
            "Are bananas healthy?",
            "What are the benefits of avocado?",
            "Should I eat broccoli every day?",
            "How nutritious is Greek yogurt?",
            "Can I drink milk before bed?",
            "How many calories are in rice?",
        ]

        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertTrue(self.backend._is_nutrition_domain_prompt(prompt))

    def test_rejects_clear_non_nutrition_questions(self):
        prompts = [
            "What is the capital of France?",
            "Do you want to hang out with me?",
            "Can you write my history essay?",
            "Is gaming good for my health?",
            "Is smoking good for my health?",
        ]

        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertFalse(self.backend._is_nutrition_domain_prompt(prompt))


if __name__ == "__main__":
    unittest.main()

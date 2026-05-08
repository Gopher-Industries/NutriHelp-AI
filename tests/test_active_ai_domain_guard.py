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

    def test_accepts_gluten_allergy_and_diet_questions(self):
        prompts = [
            "If I'm allergic to gluten, can I still eat cereal?",
            "I have a peanut allergy. What snacks should I avoid?",
            "Can you make a vegan meal plan for me?",
            "Is pasta okay for a low-carb diet?",
            "Which cereals are dairy-free and nut-free?",
            "How much sugar and salt is too much?",
            "Does malt flour contain gluten?",
            "What high-protein vegetarian breakfast can I eat?",
            "What allergens should I check for in bread and noodles?",
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
            "I'm allergic to cats. What medicine should I take?",
        ]

        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertFalse(self.backend._is_nutrition_domain_prompt(prompt))


if __name__ == "__main__":
    unittest.main()

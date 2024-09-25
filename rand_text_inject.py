import random

class RandomWordInjector:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "main_text": ("STRING", {
                    "multiline": True,
                    "default": "This is a {1} prompt with {2} words.",
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff
                }),
                "random_word_1": ("STRING", {
                    "multiline": True,
                    "default": "cool, awesome, fantastic",
                }),
                "random_word_2": ("STRING", {
                    "multiline": True,
                    "default": "random, injected, special",
                }),
                "random_word_3": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "random_word_4": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "random_word_5": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "inject_random_words"
    CATEGORY = "text"

    def inject_random_words(self, main_text, seed, random_word_1, random_word_2, random_word_3, 
                            random_word_4, random_word_5):
        # Set the random seed
        random.seed(seed)
        
        random_word_lists = [random_word_1, random_word_2, random_word_3, random_word_4, random_word_5]
        
        for i, word_list in enumerate(random_word_lists, start=1):
            if word_list:
                words = [word.strip() for word in word_list.split(',') if word.strip()]
                if words:
                    random_word = random.choice(words)
                    main_text = main_text.replace(f"{{{i}}}", random_word)
        
        return (main_text,)

NODE_CLASS_MAPPINGS = {
    "RandomWordInjector": RandomWordInjector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomWordInjector": "Random Word Injector"
}

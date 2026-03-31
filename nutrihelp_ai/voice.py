# ============================================================================
# FILE 4: voice.py
# Voice recognition and text-to-speech using pyttsx3 and speech_recognition
# ============================================================================

import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE, VOICE_VOLUME, LISTEN_TIMEOUT, PHRASE_TIME_LIMIT


class VoiceAssistant:
    """Handles voice input/output for the nutrition assistant"""

    def __init__(self):
        # Initialize TTS engine
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', VOICE_RATE)
            self.engine.setProperty('volume', VOICE_VOLUME)

            # Set voice (prefer female voice if available)
            voices = self.engine.getProperty('voices')
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)

            self.tts_enabled = True
            print("[Voice] ✓ Text-to-Speech initialized")

        except Exception as e:
            print(f"[Voice] ⚠ TTS initialization failed: {e}")
            self.tts_enabled = False

        # Initialize speech recognizer
        try:
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 4000
            self.recognizer.dynamic_energy_threshold = True
            self.stt_enabled = True
            print("[Voice] ✓ Speech Recognition initialized")

        except Exception as e:
            print(f"[Voice] ⚠ Speech recognition initialization failed: {e}")
            self.stt_enabled = False

    def speak(self, text: str, print_text: bool = True) -> bool:
        """Convert text to speech"""

        if print_text:
            print(f"\n🤖 Assistant: {text}")

        if not self.tts_enabled:
            return False

        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return True

        except Exception as e:
            print(f"[Voice] ⚠ TTS error: {e}")
            return False

    def listen(self, prompt: str = "Listening...", timeout: int = LISTEN_TIMEOUT) -> str:
        """Listen to user speech and convert to text"""

        if not self.stt_enabled:
            print(f"\n❓ {prompt}")
            return input("Type your answer: ").strip()

        try:
            self.speak(prompt, print_text=False)
            print(f"\n🎤 {prompt}")

            with sr.Microphone() as source:
                print("[Voice] Adjusting for background noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                print("[Voice] 🎙️ Listening... (speak now)")
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )

                print("[Voice] Processing speech...")
                text = self.recognizer.recognize_google(audio)

                print(f"✓ You said: \"{text}\"")
                return text.lower().strip()

        except sr.WaitTimeoutError:
            print("[Voice] ⚠ No speech detected (timeout)")
            return self._fallback_text_input(prompt)

        except sr.UnknownValueError:
            print("[Voice] ⚠ Could not understand audio")
            return self._fallback_text_input(prompt)

        except sr.RequestError as e:
            print(f"[Voice] ⚠ Speech service error: {e}")
            return self._fallback_text_input(prompt)

        except Exception as e:
            print(f"[Voice] ⚠ Error: {e}")
            return self._fallback_text_input(prompt)

    def _fallback_text_input(self, prompt: str) -> str:
        """Fallback to text input if voice fails"""
        print(f"\n❓ {prompt}")
        return input("Type your answer: ").strip().lower()

    def ask_yes_no(self, question: str) -> bool:
        """Ask a yes/no question"""
        response = self.listen(f"{question} (say yes or no)")
        return response in ['yes', 'y', 'yeah', 'yep', 'sure', 'okay', 'ok']

    def get_choice(self, question: str, options: list) -> str:
        """Get user choice from options"""
        options_text = ", ".join(options)
        full_question = f"{question} Options are: {options_text}"

        response = self.listen(full_question)

        # Match response to options
        for option in options:
            if option.lower() in response:
                return option

        return response

"""
Unit tests for the emotion detection application.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    def test_joy(self):
        """Test joy as dominant emotion."""
        result = emotion_detector("I am glad this happened.")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test anger as dominant emotion."""
        result = emotion_detector("I am really mad about this.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test disgust as dominant emotion."""
        result = emotion_detector("I feel disgusted just thinking about it.")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        """Test fear as dominant emotion."""
        result = emotion_detector("I am afraid that something bad will happen.")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_sadness(self):
        """Test sadness as dominant emotion."""
        result = emotion_detector("I am sad and disappointed.")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()

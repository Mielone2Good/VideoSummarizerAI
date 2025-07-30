import unittest
from Backend.get_transcript import get_transcript
from Backend.ai_algorithm import YoutubeSummarizerAI

class TestBackend(unittest.TestCase):

    def test_transcript(self):
        url = 'https://www.youtube.com/watch?v=fQZntbd5QGI&ab_channel=MeticsMedia'
        test = get_transcript(url)
        self.assertIsNotNone(test)

    def test_ai_core(self):
        text = """Ella missed the last train home. Rain poured as she stood alone on the platform, 
        clutching her soaked coat. Her phone was dead, 
        and the station was silent—except for the hum of distant thunder. 
        A man in a gray hat appeared from the shadows. “Missed it too?” he asked with a gentle smile.
        She nodded, wary but curious. They shared stories to pass the time. Minutes turned into hours.
        When the next train finally arrived, dawn broke. They boarded together, 
        strangers no longer—just two souls who found something unexpected between missed connections 
        and the quiet rhythm of waiting."""
        
        ai = YoutubeSummarizerAI()
        test = ai.summarize_text(text = text)
        
        self.assertIsNotNone(test)


    def test_everything(self):
        url = 'https://www.youtube.com/watch?v=vhNJEDWqGL8&t=301s&ab_channel=Apple'
        transcript = get_transcript(url)
        print(transcript)
        ai = YoutubeSummarizerAI()
        test = ai.summarize_text(text = transcript['transcript'])
        
        print('\n\n AI SUMMARY -------------------------- \n\n')
        print(test)
        print('\n\n')
        
        self.assertIsNotNone(test)

if __name__ == '__main__':
    unittest.main()
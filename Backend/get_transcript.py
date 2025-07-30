from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url: str) -> str:
    """
    Get video id from video URL
    """
    regex_pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:[&?]|$)"
    match = re.search(regex_pattern, url)
    return match.group(1) if match else None


def get_transcript(url: str) -> dict:
    """
    Generate a transcript for a YouTube video given its URL.
    Version 1.0: Only english transcript
    """
    video_id = get_video_id(url)
    if not video_id: return {'error': f'No video ID found in url: {url}', 'status': 'error'}
    
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id=video_id)
        full_transcript = " ".join(snippet.text for snippet in transcript)
        return {'transcript': full_transcript, 'status': 'success'}
    
    except Exception as e:
        return {'error': e, 'status': 'error'}
    

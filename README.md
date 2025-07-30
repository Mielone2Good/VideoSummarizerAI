
<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/Mielone2Good/VideoSummarizerAI">
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" height="80">
  </a>

  <h3 align="center">Video Summarizer using Local LLM (facebook/bart-large-cnn)</h3>

  <p align="center">
    Submit a YouTube URL and get an AI-generated summary of the video.
    <br />
    <a href="https://github.com/Mielone2Good/VideoSummarizerAI"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mielone2Good/VideoSummarizerAI">View Demo</a>
    ·
    <a href="https://github.com/Mielone2Good/VideoSummarizerAI/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Mielone2Good/VideoSummarizerAI/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

---

## 📌 About The Project

This project allows you to generate AI-powered summaries of YouTube videos using the `facebook/bart-large-cnn` local language model. You just send a video URL to the FastAPI endpoint, and within ~8 seconds (depending on your GPU), you get a clean summary of the content.

💡 It works even for long transcripts or complex documents.

### 🔍 How it works

1. **Transcript download** using `get_transcript`.
2. **Chunking** of the text for better LLM input.
3. **Chunk-wise summarization** with `facebook/bart-large-cnn`.
4. **Merging summaries** into a final summary.
5. Exposed via API endpoint:  
   `GET /summarize-video?url=YOUR_YOUTUBE_URL`

---

## ⚙️ Structure

- `ai_core.py`: Handles tokenization and LLM model logic  
- `ai_algorithm.py`: Chunking and hierarchical summarization logic  
- `get_transcript.py`: Retrieves transcript from YouTube  
- `api.py`: FastAPI web server exposing the summarization endpoint  
- `tests/`: Unit tests for core components

---

## 🚀 Built With

* [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

---

## 🧪 Unit Tests

This repo contains a full suite of unit tests for the AI pipeline logic to ensure consistency and reliability.

Run them using:

```bash
python -m Backend.tests.unit_test
````

---

## 🚫 License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
That means:

* ✅ Free for **non-commercial** use
* ✅ Attribution required (mention the author)
* ❌ **Commercial use is forbidden**

Author: **Mikołaj Jaros. (aka MixDevv)**
[![LinkedIn](https://img.shields.io/badge/-Mikołaj%20Jaros-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/mikolajjaros/)

---

## 🙏 Acknowledgments

* [Hugging Face](https://huggingface.co/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Python Software Foundation](https://www.python.org/)

--- 

## 📷 Screenshots

### Request Sent - Test on iPhone Ad  
<img width="1100" alt="RequestSent_test_on_phone_ad" src="https://github.com/user-attachments/assets/4559673e-1bc7-40b5-9d23-1ce8b391c2c5" />
This screenshot shows the app sending a request and receiving a response from the server, highlighting the GPU usage during processing.


---

### Test Result on iPhone Ad  
<img width="1100" alt="TestResult_PhoneAd" src="https://github.com/user-attachments/assets/1f4c75dc-f40f-459d-9b51-e13d08f7f944" />
A detailed view of the server response corresponding to the previous request, showing the summarized content returned by the API.

---

### Unit Tests - Shopify Tutorial  
<img width="1100" alt="UnitTests_ShopifyTutorial" src="https://github.com/user-attachments/assets/38274e32-d92d-4c71-8b90-df07f94d9251" />
Demonstrates the successful execution of unit tests, ensuring the app's core functionalities work correctly.



<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/Mielone2Good/VideoSummarizerAI.svg?style=for-the-badge
[contributors-url]: https://github.com/Mielone2Good/VideoSummarizerAI/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Mielone2Good/VideoSummarizerAI.svg?style=for-the-badge
[forks-url]: https://github.com/Mielone2Good/VideoSummarizerAI/network/members

[stars-shield]: https://img.shields.io/github/stars/Mielone2Good/VideoSummarizerAI.svg?style=for-the-badge
[stars-url]: https://github.com/Mielone2Good/VideoSummarizerAI/stargazers

[issues-shield]: https://img.shields.io/github/issues/Mielone2Good/VideoSummarizerAI.svg?style=for-the-badge
[issues-url]: https://github.com/Mielone2Good/VideoSummarizerAI/issues

[license-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey?style=for-the-badge
[license-url]: https://creativecommons.org/licenses/by-nc/4.0/

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mikolajjaros/




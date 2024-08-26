# audio-deepfake

  <h3 align="center">Audio Deepfake Repository</h3>

  <p align="center">
    This is a repo of all the python scripts, files and resources used for deepfake generation and the LSTM model detector creation in the summer of 2024 at Columbia University.
    <br />
    <a href="">Report Bug</a>
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The proliferation of deepfake technology has raised significant concerns about the authenticity of audio content, necessitating robust detection mechanisms. The project focuses on generating high-quality audio deepfakes and developing effective detection models. With the hopes it will help counterattack adversaries using it for bad intentions. This project aims to develop a real-world deepfake audio detector at the end.

### Built With

* Python
* PyTorch

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

It's best to have a Linux server running whether locally or remotely. You will also need a GPU. This project used Nividia's L4 and V100 GPU's.

## Prerequisites

The requirements.txt contains most of the necessary libraires needed to be able to run the scripts.

* npm
  ```sh
  npm install -r requirements.txt
  ```

## Installation
Its best to have the latest version of Python, if not Python 3.6 is minimum requirement.

https://www.python.org/downloads/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

<h2>LSTM Audio Spoofing Detector</h2>

<p>This script loads a pre-trained LSTM model to evaluate its performance on an audio dataset and logs the results (accuracy, precision, recall, F1 score) to a text file.</p>

<h2>Key Features</h2>
<ul>
  <li><strong>Model</strong>: LSTM model for binary classification (real vs. spoofed audio).</li>
  <li><strong>Dataset</strong>: Test dataset loaded from file list and labels.</li>
  <li><strong>Metrics</strong>: Accuracy, precision, recall, F1 score.</li>
  <li><strong>Output</strong>: Results are saved to <code>test_results.txt</code>.</li>
</ul>

<h2>Steps</h2>
<ol>
  <li><strong>Model Loading</strong>: The LSTM model is loaded from <code>lstm_spoofing_detector_epoch_10.pth</code>.</li>
  <li><strong>Dataset Preparation</strong>: Test dataset is loaded using <code>AudioDataset</code> with file paths for audio files and their labels.</li>
  <li><strong>Evaluation</strong>: The model makes predictions on the test data, and accuracy, precision, recall, and F1 score are calculated.</li>
  <li><strong>Save Results</strong>: The results are saved in <code>test_results.txt</code>.</li>
</ol>

<h2>How to Run</h2>
<ol>
  <li>Ensure you have:
    <ul>
      <li>PyTorch</li>
      <li>NumPy</li>
      <li>Scikit-learn</li>
    </ul>
  </li>
  <pre><code>pip3 install torch numpy scikit-learn</code></pre>
  <li>Run the script:
    <pre><code>python3 lstm_audio_spoofing_test.py</code></pre>
  </li>
  <li>The test results will be saved in <code>test_results.txt</code>.</li>
</ol>

<h1>File Renaming Script</h1>

<p>This script renames all files in a specified directory by giving them a new name format and appending a counter to each file name.</p>

<h2>Key Features</h2>
<ul>
  <li><strong>Directory</strong>: The directory containing the files to be renamed is defined by the variable <code>directory</code>.</li>
  <li><strong>File Renaming</strong>: Files are renamed using a format (e.g., <code>joe-rogan-real-1.ext</code>), where the counter is incremented for each file.</li>
  <li><strong>File Extension</strong>: The original file extension is retained.</li>
  <li><strong>Completion</strong>: The script prints a message when all files have been renamed.</li>
</ul>

<h2>Steps</h2>
<ol>
  <li><strong>Directory Definition</strong>: Set the directory containing the files to rename by modifying the <code>directory</code> variable.</li>
  <li><strong>File Renaming Logic</strong>: The script iterates through all files, renames them using the specified format, and retains the original file extension.</li>
  <li><strong>Counter</strong>: The counter is incremented for each renamed file.</li>
  <li><strong>Completion</strong>: Once all files are renamed, the script outputs <code>"File renaming complete."</code>.</li>
</ol>

<h2>How to Run</h2>
<ol>
  <li>Ensure you have:
    <ul>
      <li>Python 3.6</li>
    </ul>
  </li>
  <li>Set the <code>directory</code> variable to the path containing the files you want to rename.</li>
  <li>Run the script:
    <pre><code>python3 file-rename.py</code></pre>
  </li>
  <li>The files in the specified directory will be renamed according to the new format.</li>
</ol>

<h2>About The Project</h2>

<p>This project contains a simple Python script that renames all files within a specified directory. Each file is renamed with a custom format and a unique counter, while maintaining the original file extension. This is particularly useful when you need to standardize the names of multiple audio files, for processing or organization.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p>This is a Python script that uses the PyDub library to split an audio file into two equal parts. The input audio is split at the midpoint, and each part is saved as a separate file in the specified output directory.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h3>Built With</h3>

<p>This script is built using the following technologies:</p>
<ul>
  <li><strong>Python</strong></li>
  <li><strong>PyDub</strong> - for audio file processing</li>
  <li><strong>os</strong> - for file handling</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p>This script can be run on any machine with Python and the necessary libraries installed. You will need to provide the input audio file and specify an output directory for saving the split audio files.</p>

<h3>Prerequisites</h3>

<p>Ensure you have Python and PyDub installed along with other required packages. You can install PyDub with the following command:</p>
<pre><code>pip install pydub</code></pre>

<p>You will also need FFmpeg installed, as PyDub relies on it to process audio files. You can download and install FFmpeg from <a href="https://ffmpeg.org/download.html">here</a>.</p>

<h3>Running the Script</h3>

<ol>
  <li>Run the script:
    <pre><code>python3 split.py</code></pre>
  </li>
</ol>

<p>This will split the input audio file into two equal parts and save them in the specified output directory as <code>_part1.mp3</code> and <code>_part2.mp3</code>.</p>

<p>This is a Python script that combines multiple small audio files into one large audio file for use in tasks such as speech synthesis. The script supports MP3 and WAV formats and processes all audio files in a specified directory.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h3>Built With</h3>

<p>This script is built using the following technologies:</p>
<ul>
  <li><strong>Python</strong></li>
  <li><strong>PyDub</strong> - for audio file processing</li>
  <li><strong>os</strong> - for file handling</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p>This script combines audio files from a specified directory into a single audio file. You will need to provide the directory path that contains the audio files and specify the output file path for the combined audio.</p>

<h3>Prerequisites</h3>

<p>Ensure you have Python and PyDub installed along with other required packages. You can install PyDub with the following command:</p>
<pre><code>pip install pydub</code></pre>

<p>You will also need FFmpeg installed, as PyDub relies on it to process audio files. You can download and install FFmpeg from <a href="https://ffmpeg.org/download.html">here</a>.</p>

<h3>Running the Script</h3>

<ol>
  <li>Run the script:
    <pre><code>python3 combine.py</code></pre>
  </li>
</ol>

<p>This will combine all the audio files in the specified directory into one large file and save it to the specified output path.</p>

<p>This script is a Python script that downloads YouTube Shorts as MP3 files. It uses <strong>yt-dlp</strong> to download the audio from the YouTube Shorts and converts it to MP3 format using FFmpeg.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h3>Built With</h3>

<p>This script is built using the following technologies:</p>
<ul>
  <li><strong>Python</strong></li>
  <li><strong>yt-dlp</strong> - for downloading YouTube videos</li>
  <li><strong>PyDub</strong> - for audio file processing</li>
  <li><strong>FFmpeg</strong> - for audio format conversion</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2>Getting Started</h2>

<p>This script allows you to download multiple YouTube Shorts as MP3 files by providing a text file containing the video links. Each link will be processed and the audio will be saved as an MP3 file in the specified directory.</p>

<h3>Prerequisites</h3>

<p>Ensure you have Python, <strong>yt-dlp</strong>, and <strong>PyDub</strong> installed. Additionally, <strong>FFmpeg</strong> is required for the audio extraction process.</p>

<pre><code>pip3 install yt-dlp pydub</code></pre>

<p>FFmpeg can be downloaded from <a href="https://ffmpeg.org/download.html">here</a>.</p>

<h3>Running the Script</h3>
<ol>
  <li>Run the script:
    <pre><code>python3 yt-shorts.py</code></pre>
  </li>
</ol>

<p>This will download and convert all the YouTube Shorts from the provided text file to MP3 format and save them to the specified output directory.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p>This will rename all files in the specified directory using the format <code>joe-rogan-real-&lt;counter&gt;.&lt;file-extension&gt;</code> and output a message when renaming is complete.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

No plan for adding features as of right now.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Emanuel Mendiola-Ortiz: [https://github.com/mannyortiz478/](https://github.com/mannyortiz478/)

Project Link: [https://github.com/mannyortiz478/audio-deepfake/tree/main](https://github.com/mannyortiz478/audio-deepfake/tree/main)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Software Systems Lab - Department of Computer Science - Columbia University

* Dr. Junfeng Yang - Professor
* Chengzi Mao - Postdoc
* Zirui Zhang - Masters Student

<p align="right">(<a href="#readme-top">back to top</a>)</p>

"""

Challenge: Concurrent File Download

Write an asyncio program that downloads multiple files concurrently. The program should take a list of URLs as input and download the corresponding files concurrently. Each file should be saved with its original name in the current directory.

Requirements:

The program should accept a list of URLs as command-line arguments or from user input.
Implement a function download_file(url) that takes a URL as input and downloads the file from that URL.
Use asyncio and coroutines to download the files concurrently.
Save each downloaded file with its original name in the current directory.
Display appropriate messages to indicate the progress of the downloads.
Feel free to use any third-party libraries or modules if necessary.

Once you have completed the challenge, you can test your program by providing a list of URLs and verifying that the files are downloaded concurrently.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import concurrent.futures
import os

import requests


def download_image(url: str, idx: int) -> None:
    """
    Downloads a single image from a given URL and
    saves it with a unique index.

    Args:
        url (str): The URL of the image to download.
        idx (int): The index used to create a unique filename.

    """
    filename = os.path.join("imgs", f"image_{idx}.jpg")
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, "wb") as f:
            f.write(r.content)
        print(f"Saved: {filename}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")


def download_images_multiprocess(urls: list[str], num_of_processes: int = 5) -> None:
    """
    Downloads multiple images using multiple processes (parallel execution).

    Parameters:
        urls (list[str]): List of image URLs to download.
        num_of_processes (int): Number of processes to use.
    """
    print(f"\n Starting multiprocessing download with {num_of_processes} processes.\n")

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_of_processes) as ex:
        futures = [ex.submit(download_image, url, idx) for idx, url in enumerate(urls, start=1)]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"[Process] Error: {e}")

# if __name__ == "__main__":
#     download_images_multiprocess(get_image_urls(num=50), num_of_processes=5)

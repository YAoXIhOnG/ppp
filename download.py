import requests
import os
from tqdm import tqdm

url = "http://dpv.videocc.net/a647f95e6e/b/a647f95e6e2519a44c0cb2bba06e19ab_1.mp4"
dst = r"E:\test.mp4"

def download(url, dst):
    session = requests.Session()
    response = session.get(url, stream=True)
    file_size = int(response.headers['content-length'])
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        print("finish download")

    header = {"Range": f"bytes={first_byte}-{file_size}"}
    pbar = tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, unit_divisor=1024, ncols=90, mininterval = 1,desc=dst)
    req = requests.get(url, headers=header, stream=True)
    with open(r'E:\test.mp4', 'wb') as fw:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                fw.write(chunk)
                pbar.update(1024)
        fw.flush()
    pbar.close()
    fw.close()

download(url, dst)

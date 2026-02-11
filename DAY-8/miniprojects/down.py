# Source - https://stackoverflow.com/a/57434176
# Posted by Danilo Filippo
# Retrieved 2026-02-04, License - CC BY-SA 4.0

import sys, os
import zipfile
import requests
from multiprocessing import Pool, cpu_count
from functools import partial
from io import BytesIO


def download_zip(url, filePath):
    try:
        file_name = url.split("/")[-1]
        response = requests.get(url)
        sourceZip = zipfile.ZipFile(BytesIO(response.content))
        print(" Downloaded {} ".format(file_name))
        sourceZip.extractall(filePath)
        print(" extracted {}".format(file_name))
        sourceZip.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    filePath = os.path.dirname(os.path.abspath(__file__))
    print("filePath is %s " % filePath)
    # sys.path.append(filePath) # why do you need this?
    urls = ["http://mlg.ucd.ie/files/datasets/multiview_data_20130124.zip"]

    print("There are {} CPUs on this machine ".format(cpu_count()))
    pool = Pool(cpu_count())
    download_func = partial(download_zip, filePath = filePath)
    results = pool.map(download_func, urls)
    pool.close()
    pool.join()

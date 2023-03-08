import os

from dotenv import load_dotenv, find_dotenv
from minio import Minio


def download_bucket(bucket_name: str, local_path: str) -> None:
    # return os.path.dirname(os.path.join(os.path.abspath(__file__),"../.."))
    load_dotenv(find_dotenv())
    key = os.environ.get("MINIO_KEY")
    secret = os.environ.get("MINIO_SECRET")
    # print("ROOT DIR:", ROOT_DIR)
    # print("KEY SECRET:", key, secret)
    client = Minio(
        "s3.juri.lol",
        access_key=key,
        secret_key=secret,
    )
    # found = client.bucket_exists("asiatrip")
    # if found:
    #     print("FOUND")
    # else:
    #     print("NOT FOUND")
    for item in client.list_objects(bucket_name, recursive=True):
        client.fget_object(bucket_name, item.object_name, os.path.join(local_path, item.object_name))
        print("Downloaded", item.object_name)


def download_raw_data() -> None:
    print("downloading raw data...")
    download_bucket("data", "../data")

import os

from dotenv import load_dotenv, find_dotenv
from minio import Minio

load_dotenv(find_dotenv())

KEY = os.environ.get("MINIO_KEY")
SECRET = os.environ.get("MINIO_SECRET")
BUCKET_NAME = "data"

client = Minio(
    "s3.juri.lol",
    access_key=KEY,
    secret_key=SECRET,
)


def upload_files(bucket_name: str, local_path: str) -> None:
    for root, dirs, files in os.walk(local_path):
        for file in files:
            print(bucket_name, file, os.path.join(root, file))
            # client.fput_object(bucket_name, file, os.path.join(root, file))
            print("Uploaded", file)


def download_bucket(bucket_name: str, local_path: str) -> None:
    for item in client.list_objects(bucket_name, recursive=True):
        client.fget_object(bucket_name, item.object_name, os.path.join(local_path, item.object_name))
        print("Downloaded", item.object_name)


def get_file_count(bucket_name: str) -> int:
    items = client.list_objects(bucket_name, recursive=True)
    count = sum(1 for _ in items)
    return count


def download_raw_data() -> None:
    print("downloading raw data...")
    download_bucket("data", "../data")


def test_minio() -> None:
    try:
        found = client.bucket_exists(BUCKET_NAME)
        items = client.list_objects(BUCKET_NAME, recursive=True)
        count = sum(1 for _ in items)
        assert found is True
        print(f"{BUCKET_NAME} bucket contains {count} items!")
    except Exception as e:
        print("error", e)

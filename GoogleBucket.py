from google.cloud import storage
from pathlib import Path
import base64
path_to_private_key = 'D:/fifth-compass-415612-76f634511b19.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
bucket = storage.Bucket(client, 'hackathon1415')

str_folder_name_on_gcs = 'RESUME/data'

# Create the directory locally
Path(str_folder_name_on_gcs).mkdir(parents=True, exist_ok=True)

blobs = bucket.list_blobs(prefix=str_folder_name_on_gcs)
# print(len(list(blobs)))
blb = list(blobs)
for itr in range(200):
    if not blb[itr].name.endswith('/'):
        # This blob is not a directory!
        print(f'Downloading file [{blb[itr].name}]')
        # content = blb[itr].download_as_string()
        blb[itr].download_to_filename(f'./{blb[itr].name}')
        # data =base64.b64decode(content)
        # data.decode('latin-1').translate()
    
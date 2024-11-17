import ipfshttpclient
from loguru import logger


def upload_ipfs_link(link):
    try:
        client = ipfshttpclient.connect("/dns/ipfs/tcp/5001/http")
        res = client.add(link)
        cid = res["Hash"]
        ipfs_url = f"https://ipfs.io/ipfs/{cid}"
        return cid, ipfs_url
    except Exception as e:
        logger.info(f"Failed to download IPFS link: {e}")
        return None, None

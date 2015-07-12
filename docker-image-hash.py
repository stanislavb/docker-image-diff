#!/usr/bin/env python3
import argparse
import json
import requests
import logging
import docker
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_registry_tag(image, tag='latest', registry_url=None, ver=1):
    if registry_url is None:
        registry_url = 'https://registry.hub.docker.com/v{}/'.format(ver)
    image_endpoint = 'repositories/{0}/tags/{1}'.format(image, tag)
    if ver == 2:
        image_endpoint += '/'
    image_url = urljoin(registry_url, image_endpoint)
    logger.info('GET {}'.format(image_url))
    response = requests.get(image_url)
    response.raise_for_status()
    content = response.json()
    logger.info('Got response: {}'.format(content))
    return content


def get_local_image(image, tag='latest'):
    c = docker.Client(**docker.utils.kwargs_from_env())
    images = c.images(name=image)
    for image_info in images:
        if '{}:{}'.format(image, tag) in image_info['RepoTags']:
            return image
    return None

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('image')
        args = parser.parse_args()

        split_image = args.image.split(':')
        image = split_image[0]
        tag = split_image[1] if len(split_image) > 1 else 'latest'

        local = get_local_image(image, tag)
        remote = get_registry_tag(image, tag)

        print(json.dumps(local, indent=4, sort_keys=True))
        print(json.dumps(remote, indent=4, sort_keys=True))

#!/usr/bin/env python3
# vim: expandtab shiftwidth=2 softtabstop=2

from concurrent import futures
import grpc
import io
import tagdeterminer_pb2
import tagdeterminer_pb2_grpc

from PIL import Image  # PIL is actually pillow
from ram import get_transform
from ram import inference_ram as inference
from ram.models import ram_plus
import torch


BLOCK_TAGS = [
    'boy',
    'goggles',
    'man',
    ]

PRETRAINED_MODEL = '/usr/src/app/ram_plus_swin_large_14m.pth'
IMAGE_SIZE = 384

ram_device = None
ram_transform = None
ram_model = None


def load_model():
  global ram_device, ram_transform, ram_model
  ram_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  ram_transform = get_transform(image_size=IMAGE_SIZE)
  model = ram_plus(pretrained=PRETRAINED_MODEL, image_size=IMAGE_SIZE, vit='swin_l')
  model.eval()
  ram_model = model.to(ram_device)


def eval_image(image_bytes):
  i = Image.open(io.BytesIO(image_bytes))
  t = ram_transform(i).unsqueeze(0).to(ram_device)
  res = inference(t, ram_model)
  tags_str = res[0]

  # TODO add checks for:
  # - tags all > 1 character
  # - return format has not changed
  tags = tags_str.split(' | ')
  tags = [t for t in tags if t not in BLOCK_TAGS]
  return tags


class Determiner(tagdeterminer_pb2_grpc.TagDeterminerServicer):

  def About(self, request, context):
    return tagdeterminer_pb2.AboutReply(
        name='Recognize Anything Model Tag Determiner',
        tag_cls='RecognizeAnything',
        )

  def DetermineTags(self, request_iterator, context):
    content = b''
    count = 0
    for req in request_iterator:
      content += req.content
      count += 1

    print('Received %s parts, %s bytes.' % (count, len(content)))
    tags = eval_image(content)
    print('Tags: %s' % tags)
    return tagdeterminer_pb2.DetermineTagsReply(tag=tags)


if __name__ == '__main__':
  load_model()
  bind_to = "0.0.0.0:30033"
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
  tagdeterminer_pb2_grpc.add_TagDeterminerServicer_to_server(Determiner(), server)
  server.add_insecure_port(bind_to)
  server.start()
  print("Listening on " + bind_to)
  server.wait_for_termination()

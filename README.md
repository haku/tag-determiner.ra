Tag Determiner: RecognizeAnything
=================================

This wraps [RecognizeAnything](https://github.com/xinyu1205/recognize-anything)
in a docker container with the GRPC interface needed for mediatoad.

Build
-----

You must download the model file `ram_plus_swin_large_14m.pth` and place it in
this directory before building the image:
https://huggingface.co/xinyu1205/recognize-anything-plus-model/blob/main/ram_plus_swin_large_14m.pth

```shell
docker build -t tag-determiner.ra .
```

Test
----

```shell
docker run -it --rm -p 127.0.0.1:30033:30033 --name tag-determiner.ra tag-determiner.ra
docker exec -it tag-determiner.ra bash
```

Run
---

```shell
docker run -p 127.0.0.1:30033:30033 --name tag-determiner.ra tag-determiner.ra
```

Dev
---

to update proto files:

```shell
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. tagdeterminer.proto
```

<!-- vim: textwidth=80 noautoindent nocindent
-->

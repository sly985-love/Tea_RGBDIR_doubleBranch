# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_add_apple.yaml --data data/multispectral/apple.yaml  --name s_add --device 0;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformer_apple.yaml --data data/multispectral/apple.yaml  --name s_tran --device 1;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformerx3_apple.yaml --data data/multispectral/apple.yaml  --name s_tran3 --device 1;
# python train.py  --weights yolov5l_transformerx3_llvip_s1024_bs32_e200 --cfg models/apple/yolov5l_fusion_transformerx3_apple.yaml --data data/multispectral/apple.yaml  --name s_tran3 --device 0;


# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_add_apple.yaml --data data/multispectral/apple_d_RGB.yaml  --name s_add_D_RGB --device 0;python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformerx3_apple.yaml --data data/multispectral/apple_d_RGB.yaml  --name s_tran3_D_RGB --device 0;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformer_apple.yaml --data data/multispectral/apple_d_RGB.yaml  --name s_tran_D_RGB --device 1;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformerx3_apple.yaml --data data/multispectral/apple_d_RGB.yaml  --name s_tran3_D_RGB --device 1;

# data/multispectral/apple_D_IR.yaml


# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_add_apple.yaml --data data/multispectral/apple_D_IR.yaml  --name s_add_D_IR --device 0;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformer_apple.yaml --data data/multispectral/apple_D_IR.yaml  --name s_tran_D_IR --device 1;
# python train.py  --weights best.pt --cfg models/apple/yolov5s_fusion_transformerx3_apple.yaml --data data/multispectral/apple_D_IR.yaml  --name s_tran3_D_IR --device 1;


# python


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     8.04G   0.02397   0.08108         0     0.105       161       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:19<00:00,  2.50it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  25%|███████████▎                                 | 1/4 [00:00<00:01,  1.52it/s]E
# xception in thread Thread-5:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-6:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  50%|██████████████████████▌                      | 2/4 [00:01<00:01,  1.39it/s]E
# xception in thread Thread-7:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-8:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.73it/s]
# Exception in thread Thread-9:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-10:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                  all          97        1389       0.918       0.884       0.938       0.679       0.594
# 300 epochs completed in 1.956 hours.
#
# Optimizer stripped from runs\train\s_tran\weights\last.pt, 90.4MB
# Optimizer stripped from runs\train\s_tran\weights\best.pt, 90.4MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     7.84G   0.02382   0.07827         0    0.1021       107       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:15<00:00,  3.10it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  25%|███████████▎                                 | 1/4 [00:00<00:01,  1.64it/s]E
# xception in thread Thread-5:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-6:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  50%|██████████████████████▌                      | 2/4 [00:01<00:01,  1.48it/s]E
# xception in thread Thread-7:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-8:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  75%|█████████████████████████████████▊           | 3/4 [00:02<00:00,  1.46it/s]E
# xception in thread Thread-9:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  2.09it/s]
#  File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.83it/s]
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-10:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                  all          97        1389       0.926        0.87       0.932       0.658       0.595
# 300 epochs completed in 1.569 hours.


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     8.04G   0.02397   0.08108         0     0.105       161       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:19<00:00,  2.50it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  25%|███████████▎                                 | 1/4 [00:00<00:01,  1.52it/s]E
# xception in thread Thread-5:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-6:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  50%|██████████████████████▌                      | 2/4 [00:01<00:01,  1.39it/s]E
# xception in thread Thread-7:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-8:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.73it/s]
# Exception in thread Thread-9:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-10:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                  all          97        1389       0.918       0.884       0.938       0.679       0.594
# 300 epochs completed in 1.956 hours.
#
# Optimizer stripped from runs\train\s_tran\weights\last.pt, 90.4MB
# Optimizer stripped from runs\train\s_tran\weights\best.pt, 90.4MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     7.84G   0.02382   0.07827         0    0.1021       107       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:15<00:00,  3.10it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  25%|███████████▎                                 | 1/4 [00:00<00:01,  1.64it/s]E
# xception in thread Thread-5:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-6:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  50%|██████████████████████▌                      | 2/4 [00:01<00:01,  1.48it/s]E
# xception in thread Thread-7:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-8:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  75%|█████████████████████████████████▊           | 3/4 [00:02<00:00,  1.46it/s]E
# xception in thread Thread-9:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  2.09it/s]
#  File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.83it/s]
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-10:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                  all          97        1389       0.926        0.87       0.932       0.658       0.595
# 300 epochs completed in 1.569 hours.


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     5.06G   0.02336   0.07669         0    0.1001        61       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:11<00:00,  4.18it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  25%|███████████▎                                 | 1/4 [00:00<00:02,  1.42it/s]E
# xception in thread Thread-5:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-6:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95:  50%|██████████████████████▌                      | 2/4 [00:01<00:01,  1.29it/s]E
# xception in thread Thread-7:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-8:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.65it/s]
# Exception in thread Thread-9:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
# Exception in thread Thread-10:
# Traceback (most recent call last):
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 932, in _bootstrap_inner
#     self.run()
#   File "C:\Users\shuailuyu\anaconda3\envs\tea\lib\threading.py", line 870, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main\utils\plots.py", line 164, in plot_images
#     mosaic[block_y:block_y + h, block_x:block_x + w, :] = img
# ValueError: could not broadcast input array from shape (458,640,6) into shape (458,640,3)
#                  all          97        1389       0.917       0.877       0.935       0.676       0.592
# 300 epochs completed in 1.580 hours.
#
# Optimizer stripped from runs\train\s_add2\weights\last.pt, 22.9MB
# Optimizer stripped from runs\train\s_add2\weights\best.pt, 22.9MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


# depth RGB add
#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     5.12G   0.02449   0.08114         0    0.1056        61       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:11<00:00,  4.22it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.72it/s]
#                  all          97        1389       0.913       0.872       0.921        0.62       0.568
# 300 epochs completed in 1.123 hours.
#
# Optimizer stripped from runs\train\s_add_D_RGB\weights\last.pt, 22.9MB
# Optimizer stripped from runs\train\s_add_D_RGB\weights\best.pt, 22.9MB


# depth RGB tran
#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     8.04G   0.02468   0.08386         0    0.1085       161       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:19<00:00,  2.46it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.56it/s]
#                  all          97        1389       0.896       0.875       0.925       0.645        0.58
# 300 epochs completed in 1.936 hours.
#
# Optimizer stripped from runs\train\s_tran_D_RGB\weights\last.pt, 90.4MB
# Optimizer stripped from runs\train\s_tran_D_RGB\weights\best.pt, 90.4MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


# depth RGB tran3
#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     7.77G   0.02483   0.08254         0    0.1074       107       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:15<00:00,  3.08it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.72it/s]
#                  all          97        1389       0.914       0.866        0.92       0.643       0.577
# 300 epochs completed in 1.569 hours.
#
# Optimizer stripped from runs\train\s_tran3_D_RGB\weights\last.pt, 89.6MB
# Optimizer stripped from runs\train\s_tran3_D_RGB\weights\best.pt, 89.6MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     5.06G   0.02736    0.0924         0    0.1198        61       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:11<00:00,  4.30it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.66it/s]
#                  all          97        1389       0.882       0.788       0.837       0.397       0.437
# 300 epochs completed in 2.174 hours.
#
# Optimizer stripped from runs\train\s_add_D_IR\weights\last.pt, 22.9MB
# Optimizer stripped from runs\train\s_add_D_IR\weights\best.pt, 22.9MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     8.04G   0.02648   0.09117         0    0.1176       161       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:20<00:00,  2.41it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.41it/s]
#                  all          97        1389       0.873       0.793       0.843       0.471        0.46
# 300 epochs completed in 1.963 hours.
#
# Optimizer stripped from runs\train\s_tran_D_IR\weights\last.pt, 90.4MB
# Optimizer stripped from runs\train\s_tran_D_IR\weights\best.pt, 90.4MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


#      Epoch   gpu_mem       box       obj       cls     total    labels  img_size
#    299/299     7.82G   0.02677   0.08992         0    0.1167       107       640: 100%|███████████████████████████████████████████████████████████████████| 49/49 [00:16<00:00,  2.93it/s]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 4/4 [00:02<00:00,  1.49it/s]
#                  all          97        1389       0.906       0.772       0.842       0.423       0.443
# 300 epochs completed in 1.587 hours.
#
# Optimizer stripped from runs\train\s_tran3_D_IR\weights\last.pt, 89.6MB
# Optimizer stripped from runs\train\s_tran3_D_IR\weights\best.pt, 89.6MB
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_RGB_IR.yaml  --name ts_add_RGB_IR --device 1;
# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_RGB_IR.yaml --name ts_tran_RGB_IR --device 1;
# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_RGB_IR.yaml  --name ts_tran3_RGB_IR --device 1;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_D_c2d.yaml  --name ts_add_D_c2d --device 0;
# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_D_c2d.yaml --name ts_tran_D_c2d --device 0;
# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_D_c2d.yaml  --name ts_tran3_D_c2d --device 0;
# data/multispectral/tea_IR_c2d.yaml


# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_RGB_IR.yaml  --name ts_add_RGB_IR --device 1;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_RGB_IR.yaml --name ts_tran_RGB_IR --device 1;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_RGB_IR.yaml  --name ts_tran3_RGB_IR --device 1;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_D_c2d.yaml  --name ts_add_D_c2d --device 0;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_D_c2d.yaml --name ts_tran_D_c2d --device 0;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_D_c2d.yaml  --name ts_tran3_D_c2d --device 0;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_RGB_D.yaml  --name ts_add_RGB_D --device 0;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_RGB_D.yaml --name ts_tran_RGB_D --device 0;python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_RGB_D.yaml  --name ts_tran3_RGB_D --device 0;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_IR_c2d.yaml  --name ts_add_IR_c2d --device 1; python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --data data/multispectral/tea_IR_c2d.yaml --name ts_tran_IR_c2d --device 1; python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_IR_c2d.yaml  --name ts_tran3_IR_c2d --device 1;


#
#
# ___________________________________________
# python  test.py --data data/multispectral/tea_RGB_IR.yaml --weights runs/train/ts_add_RGB_IR/weights/best.pt  --device 1 --name ts_add_RGB_IR ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:11<00:00,  5.75s/it]
#                  all         112        1696       0.751       0.745       0.786       0.323       0.379
# Speed: 22.6/1.3/23.9 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_add_RGB_IR
# 112 labels saved to runs\test\ts_add_RGB_IR\labels
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>

# python  test.py --data data/multispectral/tea_RGB_IR.yaml --weights runs/train/ts_tran_RGB_IR/weights/best.pt  --device 1 --name ts_tran_RGB_IR ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:10<00:00,  5.27s/it]
#                  all         112        1696       0.739       0.765       0.782       0.319       0.375
# Speed: 22.2/1.1/23.3 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_tran_RGB_IR
# 112 labels saved to runs\test\ts_tran_RGB_IR\labels
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>

# python  test.py --data data/multispectral/tea_RGB_IR.yaml --weights runs/train/ts_tran3_RGB_IR/weights/best.pt  --device 1 --name ts_tran3_RGB_IR ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:12<00:00,  6.40s/it]
#                  all         112        1696       0.745       0.756       0.785       0.316       0.376
# Speed: 24.3/1.5/25.8 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_tran3_RGB_IR
# 112 labels saved to runs\test\ts_tran3_RGB_IR\labels
# PS C:\Users\shuailuyu\PycharmProjects\multispectral-object-detection-main>


# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_add_D_c2d/weights/best.pt  --device 1 --name ts_add_D_c2d ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:19<00:00,  9.97s/it]
#                  all         112        1696      0.0992       0.119      0.0405     0.00504      0.0106
# Speed: 24.7/4.2/28.9 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_add_D_c2d

# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_tran_D_c2d/weights/best.pt  --device 1 --name ts_tran_D_c2d ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:20<00:00, 10.43s/it]
#                  all         112        1696      0.0796       0.117      0.0319     0.00511     0.00825
# Speed: 26.3/3.9/30.2 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_tran_D_c2d
# 112 labels saved to runs\test\ts_tran_D_c2d\labels

# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_tran3_D_c2d/weights/best.pt  --device 1 --name ts_tran3_D_c2d ;
#   return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
#                Class      Images      Labels           P           R      mAP@.5     mAP@.75  mAP@.5:.95: 100%|█████████████████████████████████████████████| 2/2 [00:20<00:00, 10.16s/it]
#                  all         112        1696       0.114      0.0879       0.033     0.00502     0.00781
# Speed: 20.6/3.9/24.5 ms inference/NMS/total per 640x640 image at batch-size 64
# Results saved to runs\test\ts_tran3_D_c2d
# 112 labels saved to runs\test\ts_tran3_D_c2d\labels
#


# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_add_D_c2d/weights/best.pt  --device 1 --name ts_add_D_c2d ;
# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_tran_D_c2d/weights/best.pt  --device 1 --name ts_tran_D_c2d ;
# python  test.py --data data/multispectral/tea_D_c2d.yaml --weights runs/train/ts_tran3_D_c2d/weights/best.pt  --device 1 --name ts_tran3_D_c2d ;

# 20230315


# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_add_tea.yaml --data data/multispectral/tea_IR_c2d.yaml  --name ts2_add_IR_c2d --device 1;
# python  test.py --data data/multispectral/tea_IR_c2d.yaml --weights runs/train/ts2_add_IR_c2d/weights/best.pt  --device 1 --name ts2_add_IR_c2d ;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epoch 500 --data data/multispectral/tea_IR_c2d.yaml --name ts2_t_IR_c2d --device 1;
# python  test.py --data data/multispectral/tea_IR_c2d.yaml --weights runs/train/ts2_t_IR_c2d/weights/best.pt  --device 1 --name ts2_t_IR_c2d ;

# python train.py  --weights best.pt --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --data data/multispectral/tea_IR_c2d.yaml  --name ts2_t3_IR_c2d --device 1;


# ################################################3230325#############
# python train.py --name tea_ir_depth --data data/mutil_feature/tea_ir_depth.yaml  --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name tea_c2d_depth --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth\weights\best.pt  --device 0 --name tea_c2d_depth;

# python train.py --name tea_c2d_ir --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_ir.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_ir\weights\best.pt  --device 0 --name tea_c2d_ir;

# python train.py --name tea_ir_depth_t --data data/mutil_feature/tea_ir_depth.yaml  --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name tea_c2d_depth_t --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth_t\weights\best.pt  --device 0 --name tea_c2d_depth_t;

# python train.py --name tea_c2d_ir_t --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_ir.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_ir_t\weights\best.pt  --device 0 --name tea_c2d_ir_t;

# python train.py --name tea_ir_depth_t3 --data data/mutil_feature/tea_ir_depth.yaml  --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name tea_c2d_depth_t3 --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth_t3\weights\best.pt  --device 0 --name tea_c2d_depth_t3;

# python train.py --name tea_c2d_ir_t3 --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_ir.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_ir_t3\weights\best.pt  --device 0 --name tea_c2d_ir_t3;

#

# python train.py --name c2dx_ir_depth_aw --data data/multi_pixle_feature/c2dx_ir_depth_aw.yaml  --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_add --data data/multi_pixle_feature/c2d2_ir_add.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_subtract --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_aw --data data/multi_pixle_feature/c2d2_ir_aw.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_depth_aw --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_depth --data data/multi_pixle_feature/c2d_buds_depth.yaml--cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_ir --data data/multi_pixle_feature/c2d_buds_ir.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 1500 --batch-size 4  --device 0;

# python train.py --name c2dx_ir_depth_aw_t --data data/multi_pixle_feature/c2dx_ir_depth_aw.yaml  --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_add_t --data data/multi_pixle_feature/c2d2_ir_add.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_subtract_t --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_aw_t --data data/multi_pixle_feature/c2d2_ir_aw.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_depth_aw_t --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_depth_t --data data/multi_pixle_feature/c2d_buds_depth.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_ir_t --data data/multi_pixle_feature/c2d_buds_ir.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 1500 --batch-size 4  --device 0;

# python train.py --name c2dx_ir_depth_aw_t3 --data data/multi_pixle_feature/c2dx_ir_depth_aw.yaml  --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_add_t3 --datadata/multi_pixle_feature/c2d2_ir_add.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_subtract_t3 --data data/multi_pixle_feature/c2d2_ir_subtract.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_aw_t3 --data data/multi_pixle_feature/c2d2_ir_aw.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d2_ir_depth_aw_t3 --data data/multi_pixle_feature/c2d2_ir_depth_aw.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_depth_t3 --data data/multi_pixle_feature/c2d_buds_depth.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_buds_ir_t3 --data data/multi_pixle_feature/c2d_buds_ir.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 1500 --batch-size 4  --device 0;



#

# python train.py --name tea_c2d_ir --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name tea_c2d_depth --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name tea_c2d_ir_t --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name tea_c2d_depth_t --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name tea_c2d_ir_t3 --data data/mutil_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 0; python train.py --name tea_c2d_depth_t3 --data data/mutil_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 0;






# python train.py --name tea2_c2d_depth --data data/mutil2_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth\weights\best.pt  --device 0 --name tea_c2d_depth;

# python train.py --name tea2_c2d_ir --data data/mutil2_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_add_tea.yaml --epochs 2000 --batch-size 4  --device 1;
# python  test.py --data data/mutil_feature/tea_c2d_ir.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_ir\weights\best.pt  --device 0 --name tea_c2d_ir;

# python train.py --name tea2_ir_depth_t --data data/mutil2_feature/tea_ir_depth.yaml  --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;# python train.py --name tea2_c2d_depth_t --data data/mutil2_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth_t\weights\best.pt  --device 0 --name tea_c2d_depth_t;

# python train.py --name tea2_c2d_ir_t --data data/mutil2_feature/tea_c2d_ir.yaml --cfg models/tea/yolov5s_fusion_transformer_tea.yaml --epochs 2000 --batch-size 4  --device 0;
# python  test.py --data data/mutil_feature/tea_c2d_ir.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_ir_t\weights\best.pt  --device 0 --name tea_c2d_ir_t;

# python train.py --name tea2_c2d_depth_t3 --data data/mutil2_feature/tea_c2d_depth.yaml --cfg models/tea/yolov5s_fusion_transformerx3_tea.yaml --epochs 2000 --batch-size 4  --device 1;
# python  test.py --data data/mutil_feature/tea_c2d_depth.yaml  --weights D:\帅璐宇\RGBD_TEA\multispectral_2\tea_c2d_depth_t3\weights\best.pt  --device 0 --name tea_c2d_depth_t3;

import numpy as np

from keras.utils import Sequence
from keras.utils.io_utils import HDF5Matrix


# triplet
class DataGenerator(Sequence):
    def __init__(self, data_path, data_type, batch_size=32, normalize=True):
        self.images = HDF5Matrix(data_path, data_type+'_images')
        self.index = np.array(HDF5Matrix(data_path, data_type+'_index'))
        self.count = np.array(HDF5Matrix(data_path, data_type+'_count'))

        self.batch_size = batch_size
        self.normalize = normalize

        self.pairs = []
        self.label = []
        
        self.on_epoch_end()

    def __init__(self, images, index, count, batch_size=32, normalize=True):
        self.images = images
        self.index = index
        self.count = count

        self.batch_size = batch_size
        self.normalize = normalize

        self.pairs = []
        self.label = []
        
        self.on_epoch_end()

    def __len__(self):
        return int(np.floor(len(self.pairs) / self.batch_size))

    def on_epoch_end(self):
        self.pairs = []
        for i, (idx, cnt) in enumerate(zip(self.index, self.count)):
            for c1 in range(cnt):
                base_index = idx + c1

                for c2 in range(c1+1, cnt):
                    # Genuine pair
                    genuine_index = idx + c2

                    # Imposter pair
                    imposter = np.random.randint(0, len(self.index)-1)
                    if imposter >= i:
                        imposter += 1
                    imposter_index = self.index[imposter] + np.random.randint(self.count[imposter])

                    self.pairs.append([base_index, genuine_index, imposter_index])
        self.pairs = np.array(self.pairs)
        np.random.shuffle(self.pairs)
        self.label = np.array([0] * len(self.pairs)) # dummy data

    def __getitem__(self, batch_index):
        ys = self.label[batch_index*self.batch_size: (batch_index+1)*self.batch_size]
        pair_list = self.pairs[batch_index*self.batch_size: (batch_index+1)*self.batch_size]

        x = [[], [], []]
        for idxs in pair_list:
            for i, idx in enumerate(idxs):
                img = self.images[idx]
                x[i].append(img)

        anchor_x = np.array(x[0], np.float32) / 255
        positive_x = np.array(x[1], np.float32) / 255
        negative_x = np.array(x[2], np.float32) / 255
        xs = [anchor_x, positive_x, negative_x]

        return xs, ys


# class DataGenerator(Sequence):
#     def __init__(self, data_path, data_type, batch_size=32, normalize=True):
#         self.images = HDF5Matrix(data_path, data_type+'_images')
#         self.index = np.array(HDF5Matrix(data_path, data_type+'_index'))
#         self.count = np.array(HDF5Matrix(data_path, data_type+'_count'))

#         self.batch_size = batch_size
#         self.normalize = normalize

#         self.genuine_pairs = []
#         self.imposter_pairs = []
#         self.pairs = []
        

#         self.on_epoch_end()

#     def __len__(self):
#         return len([])

#     def on_epoch_end(self):
#         if not self.genuine_pairs:
#             for i, (idx, cnt) in enumerate(zip(self.index, self.count)):
#                     for c1 in range(cnt):
#                         base_index = idx + c1

#                         # Genuine pair
#                         for c2 in range(c1+1, cnt):
#                             pair_index = idx + c2
#                             self.genuine_pairs.append((base_index, pair_index))
        
#         base = np.random.randint(0, len(self.index), len(self.genuine_pairs))
#         pair = np.random.randint(0, len(self.index)-1, len(self.genuine_pairs))
#         pair[pair >= base] += 1

#         base_idxs = self.index[base]
#         base_cnts = self.count[base]
#         pair_idxs = self.index[pair]
#         pair_cnts = self.count[pair]

#         for base_idx, base_cnt, pair_idx, pair_cnt in zip(base_idxs, base_cnts, pair_idxs, pair_cnts):
#             base_index = base_idx + np.random.randint(base_cnt)
#             pair_index = pair_idx + np.random.randint(pair_cnt)
#             self.imposter_pairs.append((base_index, pair_index))

#         self.pairs = self.genuine_pairs + self.imposter_pairs
#         self.label = [1]*len(self.genuine_pairs) + [0]*len(self.imposter_pairs)

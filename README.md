# Masked-Face-Authentication
> 눈 주변 영역(periocular) 이미지만 사용해 마스크 착용자의 얼굴 검증을 수행한다.

![image](https://img.shields.io/badge/language-python-blue?style=flat-square&logo=python)
![image](https://img.shields.io/badge/Latest%20Update-2020/09/19-9cf?style=flat-square)


## Authors

IHCI 2020 Authentication of Facial Images with Masks using Periocular Biometrics  (☞ﾟヮﾟ)☞ [논문 보러가기](https://drive.google.com/file/d/1ZDcSeAH8MFasMhfSBDxEkAQ5hlBS-tnD/view?usp=sharing)

**Han, N. Y.**, Seong, S. W., Ryu, J., Hwang, H., Joung, J., Lee, J., & Lee, E. C. (2020, November). Authentication of Facial Images with Masks Using Periocular Biometrics. In International Conference on Intelligent Human Computer Interaction (pp. 326-334). Springer, Cham.


|                 한나연               |                 성시원                |              류지혜               |
| :------------------------------------------: | :-----------------------------------------: | :----------------------------------------: |
| <img src="https://user-images.githubusercontent.com/33839093/129561824-7f779bf8-8036-4ab6-812e-4c7aa12c3d79.png" width=150px> | <img src="https://user-images.githubusercontent.com/33839093/134047468-1199ed43-cfb2-48a6-98e9-4b377cce131d.png" width=150px> | <img width="122" alt="jj" src="https://user-images.githubusercontent.com/33839093/134047117-353274f2-4594-42b8-ad15-cc745adfe33c.PNG" width=250px> |
|                   **[Github](https://github.com/HanNayeoniee)**                   |                   **[Github](https://github.com/SiWonSeong)**                   |               **[Github](https://github.com/jihyejjang)**               |


## Files

1. ratio of mask.ipynb

2. Periocular dataset generator.ipynb

3. Full-face dataset generator.ipynb

4. Siamese-networks_training.ipynb

5. Siamese-networks_testing.ipynb



## Approach

Siamese network 학습에 필요한 얼굴 이미지를 수집한 후 ROI인 periocular region과 전체 얼굴을 자르는 전처리 과정을 거친다. 

데이터셋은 periocular 이미지, 전체 얼굴 이미지 총 2가지 데이터셋을 활용하며 학습 데이터, 검증 데이터, 테스트 데이터를 약 70%, 15%, 15%의 비율로 나누어 구축한다. 

Periocular와 전체 얼굴 이미지의 성능 비교를 위해 동일한 조건(데이터 구성, 학습과정, 평가)에서 모델을 학습하고 genuine, imposter matching을 테스트하여 적절한 임계값을 도출한다.


## Dataset

- **Face Dataset**

① [RFW(Real Faces in-the-wild) dataset](http://www.whdeng.cn/RFW/index.html): Datasets consist of four different races for deep face recognition (African, Asian, Caucasian, Indian)

② [Face Spoofing DB](https://www.mdpi.com/2079-9292/9/4/661)

③ [IAS-Lab RGB-D Face](http://robotics.dei.unipd.it/reid/index.php/8-dataset/9-overview-face) The training dataset consists of 26 subjects captured in 13 different conditions (with pose, light and expression variations), standing 1 or 2 meters from the sensor. The testing dataset contains 19 subjects and just four of them were also present in the training dataset. 

④ [AT&T](https://git-disl.github.io/GTDLBench/datasets/att_face_dataset/): gray scale, 400 samples

⑤ [Cas-Peal pose](http://www.jdl.ac.cn/peal/index.html): Datasets consists of subjects captured in many different conditions (with pose, expression, accessory, and etc.), gray scale

- **Masked Face Dataset**

We collected 300 images from 50 persons(each 6 images) wearing masks

We set 2 scenarios of how people wear masks: wearing masks with the entire nose covered, when wearing masks with the nose tip visible, and then took pictures from above, front, and low

sample images

<img src="https://user-images.githubusercontent.com/33839093/92573827-48127300-f2c1-11ea-861c-4d932eff0131.PNG" width=60%>

<img src="https://user-images.githubusercontent.com/33839093/92573835-49dc3680-f2c1-11ea-86df-4af74e258a2c.PNG" width=60%>


## Face Image Pre-processing

- Full-face dataset generator.ipynb: code for pre-processing face images
- Priocular dataset generator.ipynb: code for for pre-processing periocular images
- pre-processing includes three steps: detecting facial landmarks, getting ROI images, and resizing

① detecting facial landmarks

   we used [Adrian's method](https://github.com/1adrianb/face-alignment) to detect facial landmarks
  
② getting ROI images

   7 landmarks(outer extrema, nose, chin) of the 68 points were used to detect periocular region
   
   (point 2, 3): use to get vertical eye to nose distance
  
   4 landmarks(both temples, mid-nose, and chin) of the 68 points were used to detect entire face images

③ resizing

   periocular regions are resized to 91*64
    
   entire face images are resized to 120*120
  

## Training

Siamese Network

<img src="https://user-images.githubusercontent.com/33839093/93066951-8dfe7b00-f6b5-11ea-941c-6cff2d9d463d.PNG" width=70%>

(105, 105, 1) size images were used to train model and the constructed Siamese Network extracts features vectors from two input images and reduce to 100x1 size vectors.

* We set the genuine matching pairs and imposter matching pairs same.

Siamese Network is from this paper: [Siamese neural networks for one-shot image recognition](http://www.cs.toronto.edu/~gkoch/files/msc-thesis.pdf)

Siamese Network code is originally from [here](https://github.com/harveyslash/Facial-Similarity-with-Siamese-Networks-in-Pytorch)


## Performance

After training the Siamese Network with the dataset without wearing masks, we measured the performance of the model using both datasets with and without a mask. 

<img src="https://user-images.githubusercontent.com/33839093/93326717-3a766380-f854-11ea-934d-644c44eb6c28.PNG" width=70%>

<img src="https://user-images.githubusercontent.com/33839093/93318020-22e5ad80-f849-11ea-88a8-3f74ccf7bbf0.png" width=40%>


## Weights

We trained the model with 3 optimizers(RMSprop, Adam, SGDMomentum) with 4 learning rates(1×10-2, 1×10-3, 1×10-4, 1×10-5), 300 epochs.

Both of the models (trained with full face images and periocular images) showed the least loss when trained with Adam optimizer at the learning rate of 1×10-5.

Followings are weight(.pkl) files


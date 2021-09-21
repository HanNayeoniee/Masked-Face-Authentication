# Masked-Face-Authentication
> 눈 주변 영역(periocular) 이미지를 사용해 마스크 착용자의 얼굴 검증을 수행한다.

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

1. [ratio of mask.ipynb](https://github.com/HanNayeoniee/Masked-Face-Authentication/blob/master/ratio%20of%20mask%20.ipynb)

2. [Periocular dataset generator.ipynb](https://github.com/HanNayeoniee/Masked-Face-Authentication/blob/master/Periocular%20dataset%20generator.ipynb) : periocular 이미지 전처리

3. [Full-face dataset generator.ipynb](https://github.com/HanNayeoniee/Masked-Face-Authentication/blob/master/Full-face%20dataset%20generator.ipynb) : 얼굴 이미지 전처리

4. [Siamese-networks_training.ipynb](https://github.com/HanNayeoniee/Masked-Face-Authentication/blob/master/Siamese-networks_training.ipynb)

5. [Siamese-networks_testing.ipynb](https://github.com/HanNayeoniee/Masked-Face-Authentication/blob/master/Siamese-networks_testing.ipynb)


## Dataset

- **Face Dataset**

① [RFW(Real Faces in-the-wild) dataset](http://www.whdeng.cn/RFW/index.html): Deep face recognition을 위한 4개 인종으로 구성된 데이터셋 (African, Asian, Caucasian, Indian)

② [Face Spoofing DB](https://www.mdpi.com/2079-9292/9/4/661)

③ [IAS-Lab RGB-D Face](http://robotics.dei.unipd.it/reid/index.php/8-dataset/9-overview-face): 센서에서 1-2 미터 떨어진 곳에서 서서 촬영.

Train dataset은 13가지 조건(각도, 빛, 표정 등)에서 촬영한 26명의 이미지
Test dataset은 19명의 이미지로 구성되며, 이 중 4명은 train dataset과 겹침

④ [AT&T](https://git-disl.github.io/GTDLBench/datasets/att_face_dataset/): 흑백 이미지 400장

⑤ [Cas-Peal pose](http://www.jdl.ac.cn/peal/index.html): 흑백 이미지이미 각도, 표정, 악세사리 등 다양한 조건에서 촬영함 

- **Masked Face Dataset**

마스크 착용한 사진을 사람별로 6장씩 50명, 총 300장의 얼굴 이미지를 수집함

마스크를 코끝까지 올려 완전히 착용한 경우, 코끝이 보이도록 착용한 경우 2가지 case를 3가지 각도(정면, 위, 아래)에서 촬영함

<img src="https://user-images.githubusercontent.com/33839093/92573827-48127300-f2c1-11ea-861c-4d932eff0131.PNG" width=60%>

<img src="https://user-images.githubusercontent.com/33839093/92573835-49dc3680-f2c1-11ea-86df-4af74e258a2c.PNG" width=60%>


## 전처리

① 얼굴 랜드마크 검출

  [1adrianb/face-alignment](https://github.com/1adrianb/face-alignment) 방법을 얼굴 랜드마크 검출에 사용

② ROI 정의

   총 68개 얼굴 랜드마크 중 7개(outer extrema, nose, chin)를 사용해 눈 주변 영역(periocular)을, 4개(both temples, mid-nose, and chin)를 사용해 얼굴 영역을 정의했다. 
   
③ resize

   periocular 이미지는 91x64 , 전체 얼굴 이미지는 120x120로 resize.  


## Training Siamese Network

<img src="https://user-images.githubusercontent.com/33839093/134172026-dc536fdd-3441-44a6-80de-1381cb1ffcc3.PNG" width=70%>

샴 네트워크는 (105, 105, 1)크기의 이미지를 입력받아 100x1 크기의 특징 벡터를 추출한다. 
Genuine pair, Imposter pair의 개수를 동일하게 맞추었다.


## Performance

샴 네트워크를 사용해 2개의 모델을 학습시키고 각각 2개의 데이터셋을 사용해 성능을 측정했다.

<img src="https://user-images.githubusercontent.com/33839093/134172590-e9ed7c0f-e0f4-4f58-b52d-a82ce70cc2b6.PNG" width="70%">

> - **Siamese-face** : 마스크를 안 쓴 데이터셋(Unmasked images)으로 학습시킨 모델
> - **Siamese-periocular** : 마스크를 쓴 데이터셋(Masked images)으로 학습시킨 모델
> - 근소하지만 Siamese-periocular 모델(0.26 하락)이 Siamese-face 모델(0.296 하락)보다 성능이 조금 하락한 것을 확인할 수 있다. 

<img src="https://user-images.githubusercontent.com/33839093/93318020-22e5ad80-f849-11ea-88a8-3f74ccf7bbf0.png" width=60%>

> 모델을 3가지 옵티마이저(RMSprop, Adam, SGDMomentum), 4가지 learning rate(1×10-2, 1×10-3, 1×10-4, 1×10-5)을 사용해 300 epoch동안 학습시켰을 때, 
> RMSprop optimizer + learning rate 1×10-5 의 조합이 가장 좋은 성능을 보였다.  


## Reference

- [Facial-Similarity-with-Siamese-Networks-in-Pytorch](https://github.com/harveyslash/Facial-Similarity-with-Siamese-Networks-in-Pytorch)

- [Siamese neural networks for one-shot image recognition](http://www.cs.toronto.edu/~gkoch/files/msc-thesis.pdf)

- [face-alignment](https://github.com/1adrianb/face-alignment) 

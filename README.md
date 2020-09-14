# Masked-Face-Authentication

![image](https://img.shields.io/badge/language-python-blue?style=flat-square&logo=python)
![image](https://img.shields.io/badge/Latest%20Update-2020/09/09-9cf?style=flat-square)
[![HitCount](http://hits.dwyl.com/HanNayeoniee/Masked-Face-Authentication.svg)](http://hits.dwyl.com/HanNayeoniee/Masked-Face-Authentication)



[Approach](#-Approach) 

[Dataset](#-Dataset) 

[Face Image Pre-processing](#-Face-Image-Pre-processing)

[Training](#-Training)  

[Testing](#-Testing)

[Performance](#-Performance)

[Developer](#-Developer)

---
## ◼ Approach

---
## ◼ Dataset

- Face Dataset

① [RFW(Real Faces in-the-wild) dataset](http://www.whdeng.cn/RFW/index.html): Datasets consist of four different races for deep face recognition (African, Asian, Caucasian, Indian)

② [Face Spoofing DB](https://www.mdpi.com/2079-9292/9/4/661)

③ [IAS-Lab RGB-D Face](http://robotics.dei.unipd.it/reid/index.php/8-dataset/9-overview-face) The training dataset consists of 26 subjects captured in 13 different conditions (with pose, light and expression variations), standing 1 or 2 meters from the sensor. The testing dataset contains 19 subjects and just four of them were also present in the training dataset. 

④ [AT&T](https://git-disl.github.io/GTDLBench/datasets/att_face_dataset/): gray scale, 400 samples

⑤ [Cas-Peal pose](http://www.jdl.ac.cn/peal/index.html): Datasets consists of subjects captured in many different conditions (with pose, expression, accessory, and etc.), gray scale

- Masked Face Dataset

We collected 300 images from 50 persons(each 6 images) wearing masks

We set 2 scenarios of how people wear masks: wearing masks with the entire nose covered, when wearing masks with the nose tip visible, and then took pictures from above, front, and low

sample images

<img src="https://user-images.githubusercontent.com/33839093/92573827-48127300-f2c1-11ea-861c-4d932eff0131.PNG" width=50%>

<img src="https://user-images.githubusercontent.com/33839093/92573835-49dc3680-f2c1-11ea-86df-4af74e258a2c.PNG" width=50%>

---
## ◼ Face Image Pre-processing

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
  
---
## ◼ Training

Siamese Network

<img src="![siamese_network_architecture_table](https://user-images.githubusercontent.com/33839093/93066951-8dfe7b00-f6b5-11ea-941c-6cff2d9d463d.PNG)" width=50%>

---
## ◼ Testing

---
## ◼ Performance

---
## ◼ Developer
- [Na Yeon Han(HanNayeoniee)](https://github.com/HanNayeoniee), [Ji Hye Ryu(jihyejjang)](https://github.com/jihyejjang), [Si Won Seong(SiwonSeong)](https://github.com/SiWonSeong)

---
## ◼ Performance



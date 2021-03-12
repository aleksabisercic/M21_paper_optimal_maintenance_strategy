# 
## Paper in progress

# Abstract 
+ With the increase in the maintenance of mining systems predicting failure rates became an essential aspect in optimizing the maintenance performance. Despite the increase of computational power, there is no significant development in improving the simulation and prediction of avalibilty and reliability of industrial systems. With this problem at hand machine learning algorithms, being an increasingly more important part of everyday life, have potential to become one of the key ingredients in simulation and prediction within the idustrial systems.. Therefore in this paper we introduce a novel methodology for offline and online simulation availibity and reliability prediction of industrial and mining systems. Whereas traditional methodology for simulating availability and reliability is a widely used industry standard statistical and probabilistic model that implements Monte Carlo method, our proposed methodology for simulating such a system is divided in three subsegments : 1. using deep learning to generate failure intensity together with an inhomogeneous poisson point process to  predict the number and probabilistic time of failure; 2. using various neural network architectures to predict length of repair (after failure) and time between failures; and lastly 3. using LSTM encoder-decoder network to classify types of failures that will happen. Taking the industrial mining system (Excavator-Belt Conveyor-Crusher EBC system) as a case study, we evaluate our proposed methodology on three highly competitive benchmark tasks: accuracy of prediction for failure and repair rate, length of failures and lastly accuracy of classification. Furthermore, the presented methodology is not limited to mining systems and can be implemented to other industrial systems, where failure and maintenance rate are applied and can, to the best of our knowledge, be used to further optimize proactive maintenance strategies.

## Methodology Algorithm
 +![FlowChart Metodologije - Frame](https://user-images.githubusercontent.com/64646644/110998369-ff766800-837e-11eb-9b5d-774c21f6a227.jpg)
 
## Simulation Algorithm
![FlowChart Statisticke Sim](https://user-images.githubusercontent.com/64646644/110998430-161cbf00-837f-11eb-9f9f-4ab1fee899fa.jpg)

Results:
Improvment of over 30% over currently used Industry application

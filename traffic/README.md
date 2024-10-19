# Traffic
This project would like to classify the traffic sign by the AI in order to improve the functionality of self-driving vehicles. To do this, it requires to establish a multilayer neural network by using tensorflow. The code of this project has been modified for several times after trial and error, and it started with the original basic code which is provided in the lecture 5.

The basic code consist of 1 convolutional layer with 32 filters and 3*3 kernel, 1 max-pooling layer with 2*2 pool size, 1 hidden layer with 128 nodes, 0.5 dropout rate, and an output layer. The testing accuracy is around 0.05 which is far below the acceptable standard. The code therefore has been changed in order to enhance the quality.

## Modification Records and Results
1. Original Code:
    * Loss: 15.2781
    * Accuracy: 0.0521
2. Original Code with One More Convolutional Layer (32 filters): 
    * Loss: 0.2019
    * Accuracy: 0.9437
3. Original Code with One More Convolutional Layer (64 filters): 
    * Loss: 0.1791
    * Accuracy: 0.9474
4. Code 3 with Convolutional Layers Swifted (First Layer with 64 filters and Second with 32 Filters): 
    * Loss: 0.1740
    * Accuracy: 0.9506
5. Code 2 with One More Max-pooling Layer (2*2):
    * Loss: 0.3328
    * Accuracy: 0.9031
6. Code 5 with 64 filters for the first Convolutional Layer:
    * Loss: 0.3328
    * Accuracy: 0.8911
7. Code 5 with 64 filters for the second Convolutional Layer:
    * Loss: 0.1597
    * Accuracy: 0.9568
8. Code 2 with kernal size changed to 4*4:
    * Loss: 0.2896
    * Accuracy: 0.9225
9. Code 2 with One More Hidden Layer (64 nodes):
    * Loss: 0.1900
    * Accuracy: 0.9461
10. Code 7 with One More Hidden Layer (64 nodes):
    * Loss: 0.2098
    * Accuracy: 0.9409
11. Code 2 with 0.2 Dropout Rate:
    * Loss: 0.0962
    * Accuracy: 0.9779
12. Code 9 with 0.2 Dropout Rate:
    * Loss: 0.0929
    * Accuracy: 0.9770
13. Code 10 with 0.2 Dropout Rate:
    * Loss: 0.0902
    * Accuracy: 0.9773

Apart from the above record, it has also changed the number of hidden node, dropout rate, added more hidden layer, and some other actions, but these actions did not significantly improved the accuracy. The result shows that adding one more Convolutional Layer is the most effective action to enhance the testing quality. However, sometimes the result is fluctuated. To optimise the testing result and keep avoiding overfitting, it is suggested to reduce the dropout rate to an acceptable level which is 0.2 in this case, and then insert an extra hidden layer right before the output layer with halved number of nodes as the previous hidden layer. Therefore, Code 12 or Code 13 should be the appropriate codes for this project.
# REPOSITORY MAINTAINER: [Yajush](https://github.com/geekyvyas) and [Vansh](https://github.com/vansh-arora18) <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px">

<img align="right" src="https://media4.giphy.com/media/10bjbpyWbVmDXq/giphy.gif?cid=ecf05e47v48yfuhs6td1hmmk6hwolvswm79tpadxw389osit&rid=giphy.gif" />

Got tired of attending online classes at early morning? Are your parents not letting you sleep due to these online classes?
Don’t you worry at all here we have brought a special gift for your by combining the knowledge of programming.
Sleep Tight is a programme based on [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) and [Firebase](firebase.google.com/official/site)
to sleep while automatically attending class XD. The use of GUI and API are equally responsible for successful execution of the current program. GUI stands for Graphical User Interface, a software platform that presents the back-end data in a visually coherent way to users ex. MacOS, Ubuntu. API stands for Application Program Interface, which has a set of routines and protocols that let your machines talk directly to other machines.
    
The program automatically opens up your scheduled online class by its own at its exact time and jumps to next class when the time for previous gets over. The program completely fits for the people those who want to take a break from their daily routine or take a quite decent nap but don’t want to be marked absent in classes.

We are sure that this unique thought and its application won’t disappoint you in any condition and will take on full responsibility and control for your frustrating online classes.



## Set up instructions
1. Clone the repo.
```sh
$ git clone https://github.com/geekyvyas/Sleep-Tight.git
```

2. Install the dependencies
```sh
$ pip install -r requirements.txt

$ pip install git+https://github.com/ozgur/python-firebase
```

3. Gather Images for each gesture (rock, paper and scissors and None):
In this example, we gather 200 images for the "rock" gesture
```sh
$ python3 gather_images.py rock 200
```

4. Train the model
```sh
$ python3 train.py
```

5. Test the model on some images
```sh
$ python3 test.py <path_to_test_image>
```

6. Play the game with your computer!
```sh
$ python3 play.py
```

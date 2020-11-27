# REPOSITORY MAINTAINER: [Yajush](https://github.com/geekyvyas) and [Vansh](https://github.com/vansh-arora18) <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px">

<img align="right" src="https://media4.giphy.com/media/10bjbpyWbVmDXq/giphy.gif?cid=ecf05e47v48yfuhs6td1hmmk6hwolvswm79tpadxw389osit&rid=giphy.gif" />

Sleep Tight is a programme based on [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) and [Firebase](firebase.google.com/official/site)
to sleep while automatically attending class XD. It has a comprehensive, flexible ecosystem of
[tools](https://www.tensorflow.org/resources/tools),
[libraries](https://www.tensorflow.org/resources/libraries-extensions), and
[community](https://www.tensorflow.org/community) resources that lets
researchers push the state-of-the-art in ML and developers easily build and
deploy ML-powered applications.


TensorFlow was originally developed by researchers and engineers working on the
Google Brain team within Google's Machine Intelligence Research organization to
conduct machine learning and deep neural networks research. The system is
general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable [Python](https://www.tensorflow.org/api_docs/python)
and [C++](https://www.tensorflow.org/api_docs/cc) APIs, as well as
non-guaranteed backward compatible API for
[other languages](https://www.tensorflow.org/api_docs).

Keep up-to-date with release announcements and security updates by subscribing
to
[announce@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/announce).
See all the [mailing lists](https://www.tensorflow.org/community/forums).

## Install

### To install the current release, which dosen't includes timetable version *(Only Windows)*:

To install Libraries.

```
$ pip install pyautogui

$ pip install pickle-mixin

$ pip install requests

$ pip install git+https://github.com/ozgur/python-firebase

```

## Set up instructions
1. Clone the repo.
```sh
$ git clone https://github.com/SouravJohar/rock-paper-scissors.git
$ cd rock-paper-scissors
```

2. Install the dependencies
```sh
$ pip install -r requirements.txt
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

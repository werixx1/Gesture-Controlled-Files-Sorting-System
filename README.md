# Gesture-Controlled-Virtual-Files-Sorting-System

- [Tuto for hand tracking](https://www.youtube.com/watch?v=NZde8Xt78Iw)
- [Video capture](https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/)
- [Tuto for virtual cursor](https://www.youtube.com/watch?v=8gPONnGIPgw&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&index=8)
- [Drag and drop](https://youtu.be/uGmMsGOcBB0?si=1xz5jidaO07nkHBX)
- [Managing files in python](https://www.geeksforgeeks.org/python/python-directory-management/)
- [Images in tkinter](https://tkinter.com/images-in-customtkinter-tkinter-customtkinter-17/)
- [Mediapipe docs](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html)
- [Events in tkinter](https://python-course.eu/tkinter/events-and-binds-in-tkinter.php)
- [Webcam in tkinter](https://www.geeksforgeeks.org/python/how-to-show-webcam-in-tkinter-window-python/)
- [Images in tkinter](https://www.w3resource.com/python-exercises/tkinter/python-tkinter-dialogs-and-file-handling-exercise-8.php)
#### IDEA:
virtual mouse for sorting photos / files on computer ?
like a tiny program, with drag and drop (divided view) all photos on left, the ones you ‚pick’ and move with ai cursor on the right will get deleted 
<img width="1013" height="668" alt="idea_visualised" src="idea.png" />

---
wstepnie jak to ma dzialac:
1. wykonanie wirtualnego kursora (program), ktory otwiera sie rownoczesnie z
2. okienkiem gui tego eksploratora plikow (custom tkinter?), ktory laduje dostepne foldery na komputerze (zaimplementowac jakies zabezpieczenia aby nie wchodzil z kazdy folder aby nie usunac systemu niechacy ups), pozwala uzytkownikowi wybrac jakis jeden z scroll listy po czym wyswietla pliki w srodku (jakos ogarnac co jak sa tez foldery, na razie zignorowac<3). kolejna jest stronka drag and drop, wykrycie "barier" miedzy stronami okienka, aby te pliki, ktore zostana przesuniete za dany zakres zostana usuniete i potem guzik usuniecia ich:) seems simple enough 💪

---
#### todo:
- [ ] implement a virtual cursor with tuto, learn needed frameworks
- [ ] find how to optimally integrate these two programs, and if its even possible?
- [ ] design a simple GUI in a customtkinter (figma)
- [ ] implement a GUI in a custom tkinker with the code described earlier
- [ ] looots of testing
- [ ] deployment (maybe) :D

# HackRushCTF

A 3-day Jeopardy-style Capture the flag event. Your main goal is to collect as many flags as possible

Here is the document containing complete problem statement: 
https://docs.google.com/document/d/19C-Be4TExtx9mmhIq9FLi2in5ICwQQ87XPTkWRcmIX4/edit?usp=sharing


## Pwn challenges

If you want to play the Pwn challenges again, you can use my docker container to host the challenges locally and develop your exploits.

Use the command to pull the docker container:

```docker pull dishankgoel/hackrushctf:pwn```

Then run the container using:

```docker run -d -p 1337:1337 -p 12345:12345 -p 12346:12346 -p 12347:12347 --rm -it dishankgoel/hackrushctf:pwn```

The docker file is present in [Dockerfile](challenges/pwn/Dockerfile) if you want to know which port corresponds to which challenge

## Writeups

The writeups submitted by the participants is in [writeups](participant_writeups/)

Another excellent writeup by the winners: https://github.com/Harshit-Ramolia/HackRush-2021-CTF

The solution scripts for all the challenges is present in [solutions](solutions/)


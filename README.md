# concateaudio
for gaorong

# dependency

need ffmpeg, lame

# run

running under virtualenv

ffmpeg -i sample.m4a -acodec pcm_s16le -ac 2 -ar 44100 output.wav
lame -b128 output.wav yx.mp3

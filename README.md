# Dr. Pepper Robot

> Silly machine learning & robotics project for Dr. Pepper's benefit

## Usage examples

```
python3 code/multidevice_test.py
```

### motor test

spin `n` times for `on` seconds, with `off` seconds pause in between

```
python3 code/motor_test.py
python3 code/motor_test.py --on 2 --off 3 --n 3
```

### sound test

If `-i, --input-file` is given, play it; else play 440 Hz tone.  
If `-o, --output-file` is given, start recording (for `-d, --output-duration` seconds)

```
python3 code/sound_test.py
python3 code/sound_test.py -i test.wav
python3 code/sound_test.py -o test2.wav
python3 code/sound_test.py -o test3.wav -d 10
```

### display tests

```
python3 code/display_test.py
```

```
cd ../luma.examples
python3 examples/animated_gif.py --conf conf/st7735_128x128.conf
cd ../drpee
```
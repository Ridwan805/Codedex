import imageio.v3 as iio

filenames = ['clock_1.png', 
             'clock_3.png',
             'clock_4.png',
             'clock_5.png',
             'clock_6.png',
             'clock_7.png',
             'clock_8.png',
             'clock_9.png',
             'clock_10.png',
             'clock_11.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('clock.gif', images, duration = 500, loop = 0)


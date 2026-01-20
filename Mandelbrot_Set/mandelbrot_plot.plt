# Set output format and size
set terminal pngcairo size 1200,800 enhanced font 'Verdana,10'
set output 'mandelbrot_set.png'

# 1. FIX ASPECT RATIO
# Since X-range is 3 and Y-range is 2, we set ratio to 0.66 (2/3)
# This ensures a circle in the complex plane looks like a circle
set size ratio 0.666

# 2. ADD BREATHING ROOM (Margins)
# Data is [-2:1] and [-1:1]. We extend slightly so it doesn't touch borders.
set xrange [-2.2 : 1.2]
set yrange [-1.2 : 1.2]

# 3. REFINED VISUALS
set title "Mandelbrot Set Visualization" font ",14"
set xlabel "Re(z)"
set ylabel "Im(z)"
set grid linecolor rgb "#404040"  # Subtle grid

# 4. HIGH-CONTRAST PALETTE
# 'logscale' on the color bar often helps show detail in the fractal "hairs"
set logscale cb
# set palette defined ( 0 "black", 1 "blue", 5 "purple", 50 "red", 200 "orange", 1000 "yellow" )
set palette defined ( 0 "black", 0.1 "blue", 0.6 "red", 1 "yellow" )

# 5. PLOT
# 'with image' is best for this data density
plot "mandelbrot.txt" using 1:2:3 with image
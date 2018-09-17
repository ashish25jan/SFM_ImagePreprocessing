function d = tristate(img, name)
rgbImage = im2uint8(img);


% Get the dimensions of the image.  numberOfColorBands should be = 3.
[rows columns numberOfColorBands] = size(rgbImage);



% Extract the individual red, green, and blue color channels.
redChannel = rgbImage(:, :, 1);
greenChannel = rgbImage(:, :, 2);
blueChannel = rgbImage(:, :, 3);


% Median Filter the channels:
redMF = medfilt2(redChannel, [3 3]);
greenMF = medfilt2(greenChannel, [3 3]);
blueMF = medfilt2(blueChannel, [3 3]);

% Find the noise in the red.
noiseImage = (redChannel == 0 | redChannel == 255);
% Get rid of the noise in the red by replacing with median.
noiseFreeRed = redChannel;
noiseFreeRed(noiseImage) = redMF(noiseImage);
% Find the noise in the green.
noiseImage = (greenChannel == 0 | greenChannel == 255);
% Get rid of the noise in the green by replacing with median.
noiseFreeGreen = greenChannel;
noiseFreeGreen(noiseImage) = greenMF(noiseImage);
% Find the noise in the blue.
noiseImage = (blueChannel == 0 | blueChannel == 255);
% Get rid of the noise in the blue by replacing with median.
noiseFreeBlue = blueChannel;
noiseFreeBlue(noiseImage) = blueMF(noiseImage);

% Reconstruct the noise free RGB image
d = cat(3, noiseFreeRed, noiseFreeGreen, noiseFreeBlue);
imwrite(d, [name, '.png'])

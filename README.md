# Python
[7/8, 11:21 AM] Prafull 2(²³ Feb): star=imread("img.jpg");


I = rgb2gray(star);


%convert to double
I2 = im2double(I);
%do SVD
[u,s,v]=svd(I2);
%381 singular values
% 5% = 19

s2 = s;
s2(70:end, :) = 0; s2(:, 70:end) = 0;
%print image
D=u*s2*v';

in=imfinfo('img.jpg');
imwrite(star,'newStar.jpg');
k=imfinfo('newstar.jpg');
ib=in.FileSize;
cb=k.FileSize;

cr=ib/cb;
cr;

imshow(D);
[7/8, 11:24 AM] prasanna333🖤: clc;
close all;
clear all;


% Read the test Image
% Convert the image to binary image

myorigimg = imread('test.jpg');
myorigimg = im2bw(rgb2gray(myorigimg));
subplot(3, 3, 1);
imshow(myorigimg);title('Originalimage');


% Create Structuring Element
se = strel('disk', 9);

% Perform dilation operation using imdilate command
% Display the dilated image

mydilatedimg = imdilate(myorigimg, se);
subplot(3, 3, 2);
imshow(mydilatedimg);title('Dilated image');

% Perform Erosion operation using imerode command
% Display the Eroded image

myerodedimg = imerode(myorigimg, se);
subplot(3, 3, 3);
imshow(myerodedimg);title('Eroded image');


% Find Internal Boundary 
% Internal Boundary = Dilated Image AND Not of Eroded Image  
% Display Internal Boundary 

internalboundimg = mydilatedimg & ~ myerodedimg;
subplot(3, 3, 4);
imshow(internalboundimg,[]);title('Internal Boundary');


% Find External Boundary 
% External Boundary = Dilated Image AND Not of Eroded Image  
% Display External Boundary  

externalboundimg = mydilatedimg & ~myorigimg;
subplot(3, 3, 5);
imshow(externalboundimg,[]);title('External Boundary');

% Find Morphological Gradient  
% Morphological Gradient = Dilated Image AND Not of Eroded Image  
% Display External Boundary  

mymorphgradimg = imsubtract(myorigimg,myerodedimg);
subplot(3, 3, 6);
imshow(mymorphgradimg,[]);title('Morphological Gradient');

% Perform Thinning operation using bwmorph() command
% Display the dilated image

thinf = bwmorph(myorigimg,'thin');
subplot(3,3,7);
imshow(thinf);title('Thinning of the Image');

% Perform Thickening operation using bwmorph()command
% Display the dilated image

thickf = bwmorph(myorigimg,'thicken');
subplot(3,3,8);
imshow(thickf);title('Thickening of the Image');


% Perform Skeletonozation operation using bwmorph()command
% with 8 iterations and display the dilated image

skelf100 = bwmorph(myorigimg,'skel',9); 
subplot(3,3,9);
imshow(skelf100);title('Skeletonization - 9 iterations');
[7/8, 11:28 AM] prasanna333🖤: %loading the video
the_Image      = imread('nzfaruqui.jpg');
[width, height] = size(the_Image);

if width>320
the_Image = imresize(the_Image,[320 NaN]);
end

% Create a cascade detector object.
faceDetector = vision.CascadeObjectDetector();

%finding the bounding box that encloses the face on video frame
face_Location = step(faceDetector, the_Image);

% Draw the returned bounding box around the detected face.
the_Image = insertShape(the_Image, 'Rectangle', face_Location);
figure; 
imshow(the_Image); 
title('Detected face');
[7/8, 11:29 AM] prasanna333🖤: i = imread('satellite_Image.png');
ih = histeq(i);

subplot(2,2,1), imshow(i), title('Original Image');
subplot(2,2,2), imshow(ih), title('Histogram Equalized Image');
subplot(2,2,3), imhist(i), title('Histogram of Original Image');
subplot(2,2,4), imhist(ih), title('Histogram of Equalized Image');
[7/8, 11:30 AM] Prafull 2(²³ Feb): clc;
clear;
close;
% Read the image 
a=imread('D:\tuts\d1.jpg');

% Convert to grayscale incase it is color
a = rgb2gray(a);
b=size(a);
a=double(a);

% Loop for Getting the Histogram of the image
hist1 = zeros(1,256);
for i=1:b(1)
    for j=1:b(2)
        for k=0:255
            if a(i,j)==k
                hist1(k+1)=hist1(k+1)+1;
            end
        end
    end
end

%Generating PDF out of histogram by diving by total no. of pixels
pdf=(1/(b(1)*b(2)))*hist1;

%Generating CDF out of PDF
cdf = zeros(1,256);
cdf(1)=pdf(1);
for i=2:256
    
    cdf(i)=cdf(i-1)+pdf(i);
end
cdf = round(255*cdf);

ep = zeros(b);
for i=1:b(1)                                        %loop tracing the rows of image
    for j=1:b(2)                                    %loop tracing thes columns of image
        t=(a(i,j)+1);                               %pixel values in image
        ep(i,j)=cdf(t);                             %Making the ouput image using cdf as the transformation function
    end                                             
end

% Loop for Getting the Histogram of the image
hist2 = zeros(1,256);
for i=1:b(1)
    for j=1:b(2)
        for k=0:255
            if ep(i,j)==k
                hist2(k+1)=hist2(k+1)+1;
            end
        end
    end
end

subplot(2,2,1);
imshow(uint8(a));
subplot(2,2,3);
imshow(uint8(ep));
subplot(2,2,2);
stem(hist1);
subplot(2,2,4);
stem(hist2);
[7/8, 11:30 AM] prasanna333🖤: I = imread('sky.jpg');
N=imnoise(I,'salt & pepper', 0.03);
mf = ones(3, 3)/9;
noise_free = imfilter(N,mf);

subplot(2,2,1),imshow(I), title('Original Image');
subplot(2,2,2),imshow(N), title('Noisy Image');
subplot(2,2,3),imshow(noise_free), title('After Removing Noise');
[7/8, 11:31 AM] prasanna333🖤: I = imread('Blue Sky.jpg');
N = imnoise(I, 'salt & pepper', 0.3);

red_channel = N(:, :, 1);
green_channel = N(:, :, 2);
blue_channel = N(:, :, 3);

red_channel = medfilt2(red_channel, [3 3]);
green_channel = medfilt2(green_channel, [3 3]);
blue_channel = medfilt2(blue_channel, [3 3]);

F = cat(3, red_channel, green_channel, blue_channel);

subplot(2, 1, 1);
imshow(N);
title('Noisy Image');

subplot(2, 1, 2);
imshow(F);
title('Image After Noise Removal');
[7/8, 11:31 AM] prasanna333🖤: I = imread('Blue Sky.jpg');
N = imnoise(I, 'salt & pepper', 0.05);

red_channel = N(:, :, 1);
green_channel = N(:, :, 2);
blue_channel = N(:, :, 3);

the_Filter = fspecial('gaussian', [10 10], 4);

red_channel = imfilter(red_channel, the_Filter);
green_channel = imfilter(green_channel, the_Filter);
blue_channel = imfilter(blue_channel, the_Filter);

F = cat(3,red_channel, green_channel, blue_channel);

subplot(2, 1, 1);
imshow(N);
title('Noisy Image');

subplot(2, 1, 2);
imshow(F);
title('Image After Noise Removal');
[7/8, 11:31 AM] prasanna333🖤: I = imread('Road.jpg');
G = rgb2gray(I);
F = edge(G, 'sobel');
figure; imshow(F); title('Detected Edges');
figure; imshow(I); title('Original Image');
[7/8, 11:32 AM] prasanna333🖤: i = imread('satellite_Image.png');
matching = 0:255;
ih = histeq(i,matching);

subplot(2,3,1), imshow(i), title('Original Image');
subplot(2,3,2), imshow(ih), title('Histogram Matched Image');
subplot(2,3,3), plot(matching), title('Plot of the Matching Value Range');
subplot(2,3,4), imhist(i), title('Histogram of Original Image');
subplot(2,3,5), imhist(ih), title('Histogram of Matched Image');
[7/8, 11:33 AM] prasanna333🖤: %Arithmatic Operation on Image Using Matlab
image_variable=imread('C:/orange.jpg');

image_multiplication = immultiply(image_variable, 1.5);
image_division = imdivide(image_variable, 4);

subplot(2,2,1), imshow(image_variable); title('Original Image');
subplot(2,2,2), imshow(image_multiplication); title('Multiplied Image');
subplot(2,2,3), imshow(image_division); title('Dividied Image');
[7/8, 11:33 AM] prasanna333🖤: %Arithmatic Operation on Image Using Matlab
image_variable1=imread('C:/bottle1.jpg');
image_variable2 = imread('C:/bottle2.jpg');

subtracted_image = image_variable1-image_variable2;

subplot(1,3,1), imshow(image_variable1); title('First Image');
subplot(1,3,2), imshow(image_variable2); title('Second Image');
subplot(1,3,3), imshow(subtracted_image); title('Subtracted Image');
[7/8, 11:33 AM] prasanna333🖤: %Image Complement
original_image  = imread('C:/orange.jpg');
gray_image = rgb2gray(original_image);

complemented_image = imcomplement(gray_image);

subplot(2,2,1), imshow(original_image); title('Original Image');
subplot(2,2,2), imshow(gray_image); title('Gray Image');
subplot(2,2,3), imshow(complemented_image); title('Complemented Image')
[7/8, 11:34 AM] prasanna333🖤: %xor Operation on Images
image_variable1  = imread('C:/bird1.jpg');
image_variable2 = imread('C:/bird2.jpg');

binary1 = im2bw(image_variable1);
binary2 = im2bw(image_variable2);

output = xor(binary1, binary2);

subplot(3,2,1), imshow(image_variable1); title('First Image');
subplot(3,2,2), imshow(image_variable2); title('Second Image');
subplot(3,2,3), imshow(binary1); title('First Binary Image');
subplot(3,2,4), imshow(binary2); title('Second Binary Image');
subplot(3,2,5), imshow(output); title('Output');
[7/8, 11:34 AM] prasanna333🖤: % Binary Image Threshold
image_variable=imread('C:/cattle.jpg'); 
binary_image = im2bw(image_variable);

threshold_01=im2bw(image_variable, 0.1);
threshold_04 = im2bw(image_variable, 0.4); 
threshold_08 = im2bw(image_variable, 0.8); 

subplot(2,2,1), imshow(binary_image); title('Binray Image');
subplot(2,2,2), imshow(threshold_01); title('Threshold 0.1');
subplot(2,2,3), imshow(threshold_04); title('Threshold 0.4');
subplot(2,2,4), imshow(threshold_08); title('Threshold 0.8');
[7/8, 11:34 AM] prasanna333🖤: %Logarithmic Transformation
image_variable=imread('C:/orange.jpg'); 
gray_image = rgb2gray(image_variable);

double_value=im2double(gray_image);
Output1=2*log(1+double_value);
Output2=2.5*log(1+double_value);
Output3=3*log(1+double_value);

subplot(2,2,1), imshow(gray_image); title('Original Image');
subplot(2,2,2), imshow(Output1); title('Output Scaling Factor 2');
subplot(2,2,3), imshow(Output2); title('Output Scaling Factor 2.5');
subplot(2,2,4), imshow(Output3); title('Output Scaling Factor 3');
[7/8, 11:34 AM] prasanna333🖤: I = imread('image.jpg');
 
Id = im2double(I);
 
output1 = 4*(((1+0.3).^(Id))-1);
output2 = 4*(((1+0.4).^(Id))-1);
output3 = 4*(((1+0.6).^(Id))-1);
 
subplot(2,2,1), imshow(I); title('Original Image');
subplot(2,2,2), imshow(output1); title('for 0.3');
subplot(2,2,3), imshow(output2); title('for 0.4');
subplot(2,2,4), imshow(output3); title('for 0.6');
[7/8, 11:35 AM] prasanna333🖤: I = imread('image.png');
Id = im2double(I);

output1 = 2*(Id.^0.5);
output2 = 2*(Id.^1.5);
output3 = 2*(Id.^3.0);

subplot(2,2,1), imshow(I);
subplot(2,2,2), imshow(output1);
subplot(2,2,3), imshow(output2);
subplot(2,2,4), imshow(output3);
[7/8, 11:36 AM] prasanna333🖤: i = imread('cars.jpg');
[counts,bins] = imhist(i);
counts(100)
[7/8, 11:39 AM] prasanna333🖤: %Accessing Pixel Values
image_variable = imread('C:/orange.jpg');
gray_image = rgb2gray(image_variable);

pixel_value = gray_image(60,70);
sprintf('The value of the pixel is %d', pixel_value)
[7/8, 11:43 AM] prasanna333🖤: Haar wavelet compression is an efficient way to perform both lossless and lossy image compression. It relies
on averaging and differencing values in an image matrix to produce a matrix which is sparse or nearly sparse.
A sparse matrix is a matrix in which a large portion of its entries are 0. A sparse matrix can be stored in an
efficient manner, leading to smaller file sizes.
[7/8, 11:45 AM] Prafull 2(²³ Feb): %Gray level Thresolding

a=imread('coins.png');

level=graythresh(a);

c=im2bw(a,level);

figure; subplot(1,2,1), imshow(a),title('original image'); subplot(1,2,2), imshow(c),title('threshold image');
[7/8, 11:47 AM] Prafull 2(²³ Feb): a=imread('jump.jpg');
subplot(2,2,1), imshow(a),title('original image');
[LL LH HL HH]=dwt2(im2double(a),'haar');
subplot(2,2,2), imshow([LL LH ; HL HH],[]),title('Wavelet Decomposition');
[LL1 LH1 HL1 HH1]=dwt2(im2double(LL),'haar');
c=[LL1 LH1 ; HL1 HH1];
subplot(2,2,3), imshow([c LH ; HL HH],[]),title('2nd level Wavelet Decomposition');
[7/8, 11:51 AM] Prafull 2(²³ Feb): %Image Compression
star=imread("img.jpg");


I = rgb2gray(star);


%convert to double
I2 = im2double(I);
%do SVD
[u,s,v]=svd(I2);
%381 singular values
% 5% = 19

s2 = s;
s2(70:end, :) = 0; s2(:, 70:end) = 0;
%print image
D=u*s2*v';

in=imfinfo('img.jpg');
imwrite(star,'newStar.jpg');
k=imfinfo('newstar.jpg');
ib=in.FileSize;
cb=k.FileSize;

cr=ib/cb;
cr;

imshow(D);

